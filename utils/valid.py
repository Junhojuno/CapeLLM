"""MP100Dataset -> MP100DatasetExtended"""
from __future__ import annotations
from pprint import pprint
from pathlib import Path

import argparse
import os
import re
from dataclasses import dataclass

import numpy as np
from tqdm import tqdm

import torch
from torch.utils.data import DataLoader

from transformers import AutoTokenizer

from models.capellm import CapeLLMModel, CapeLLMConfig
from datasets.mp100 import MP100, QUESTION_LIST, DEFAULT_IMAGE_PATCH_TOKEN
from datasets.conversation import conv_cape_llava
from datasets.constants_cape import (
    CAPE_KEYPOINT_NAME,
    CAPEKeypointLocationDescription
)
from datasets.utils import transform_preds
from utils.valid_utils import (
    run_inference_separately,
    decode_output,
    save_result_per_rank,
    integrate_results,
    disable_torch_init
)


@dataclass
class DataCollatorForSupervisedDataset(object):
    """outputs 모두 batch_size=num_keypoints로 처리되어 출력되는 형태"""

    def __init__(self, image_token_len):
        self.image_token_len = image_token_len

    def __call__(self, instances) -> tuple[list, list, list, list]:
        """Collate examples for supervised fine-tuning.

        # NOTE
            - batch_size = 1로 고정되어있다.
            - 따라서, 아래의 batch의 의미는 객체의 keypoint 개수를 의미한다.
        """
        batch_prompts = []
        batch_images = []
        batch_has_images = []
        result_dicts = []

        conv = conv_cape_llava.copy()

        for i, line in enumerate(instances):  # batch size(=1)
            result_dict = {}
            images = line['images'].unsqueeze(0)
            image_id = line['image_id']
            c = line['c']
            s = line['s']
            bbox = line['bbox']
            joints = line['joints']
            joints_vis = line['joints_vis']
            category_id = line['category_id']
            category = line['category']
            supercategory = line['supercategory']
            keypoint_names = CAPE_KEYPOINT_NAME[category_id]
            keypoint_descs = CAPEKeypointLocationDescription[category_id]
            for kpt_name in keypoint_names:
                kpt_des = keypoint_descs[kpt_name]

                conv.messages = []
                question = QUESTION_LIST[0]
                question = question.format(keypoint=kpt_name)
                # User, Reference, Assistant
                conv.append_message(conv.roles[0], question)
                conv.append_message(conv.roles[1], kpt_des)
                conv.append_message(conv.roles[2], None)

                # NOTE - Text prompt 생성
                text_inputs = conv.get_prompt()
                cur_prompt = \
                    self.image_token_len * DEFAULT_IMAGE_PATCH_TOKEN + "\n" \
                    + text_inputs

                has_images = True

                result_dict['initial_prompt'] = cur_prompt
                result_dict['image_id'] = image_id
                result_dict['c'] = c
                result_dict['s'] = s
                result_dict['category_id'] = category_id
                result_dict['category'] = category
                result_dict['supercategory'] = supercategory
                result_dict['bbox'] = bbox
                result_dict['joints'] = joints
                result_dict['joints_vis'] = joints_vis[:, 0] > 0
                batch_prompts.append(cur_prompt)
                batch_images.append(images)
                batch_has_images.append(has_images)
                result_dicts.append(result_dict)

        return result_dicts, batch_prompts, batch_images, batch_has_images


@torch.no_grad()
def worker(model, tokenizer, dataset, args, output_dir):
    output_dir = Path(output_dir).resolve()

    crop_size = model.config.crop_size
    image_token_len = model.config.num_patches

    rank = int(os.environ["LOCAL_RANK"])
    world_size = int(os.environ["WORLD_SIZE"])
    indices = list(range(rank, len(dataset), world_size))
    print(f"==> Worker {rank} Started, responsible for {len(indices)} images")

    sub_dataset = torch.utils.data.Subset(dataset, indices)
    batch_size = 1
    data_loader = DataLoader(
        sub_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=4,
        collate_fn=DataCollatorForSupervisedDataset(image_token_len)
    )

    pattern = re.compile(r'0\.\d+')

    preds = []
    gts = []
    masks = []
    threshold_bbox = []
    data_loader = tqdm(data_loader)
    for result_dicts, batch_prompts, batch_images, batch_has_images in data_loader:
        torch.cuda.empty_cache()

        num_joints = len(result_dicts)
        outputs, output_scores = run_inference_separately(
            [batch_prompts, batch_images, batch_has_images],
            model,
            tokenizer,
            num_joints,
            n_limits=args.nkg
        )

        c = result_dicts[0]['c']
        s = result_dicts[0]['s']
        bbox = result_dicts[0]['bbox']
        gt_joint_vis = result_dicts[0]['joints_vis']
        gt_joints = result_dicts[0]['joints'][:, :2]

        bbox_thr = np.max(bbox[2:])
        thr_bbox = np.array([bbox_thr, bbox_thr])

        decoded_kpt = decode_output(outputs,
                                    output_scores,
                                    pattern,
                                    num_joints,
                                    crop_size=crop_size)

        decoded_kpt[:, :2] = transform_preds(
            coords=decoded_kpt[:, :2],
            center=c,
            scale=s,
            output_size=(crop_size, crop_size)
        )
        preds.append(decoded_kpt[:, :2])
        gts.append(gt_joints)
        masks.append(gt_joint_vis)
        threshold_bbox.append(thr_bbox)

    keys = save_result_per_rank(preds,
                                gts,
                                masks,
                                threshold_bbox,
                                rank,
                                output_dir)

    torch.distributed.barrier()  # Make sure all JSON files are saved

    if rank == 0:
        # manually sleep to wait all file are saved
        integrate_results(keys, world_size, output_dir, args.model_name)


def eval_model(args=None, seed=42):
    import random
    import numpy as np
    import transformers
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    transformers.set_seed(seed)

    # os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:1024"
    torch.distributed.init_process_group(backend='nccl')
    rank = int(os.environ["LOCAL_RANK"])
    world_size = int(os.environ["WORLD_SIZE"])

    print(f"Init process group: world_size: {world_size}, rank: {rank}")
    torch.cuda.set_device(rank)

    disable_torch_init()
    model_name = os.path.expanduser(args.model_name)
    # SECTION - Load fine-tuned LLM
    # (1) load base architecture
    from peft import PeftModel
    from safetensors.torch import load_file
    config = CapeLLMConfig.from_pretrained(model_name)
    model = CapeLLMModel(config)
    model = PeftModel.from_pretrained(model, model_name)

    # SECTION - LLM 이외의 모듈 load
    model_dir = Path(model_name).resolve()
    vision_state_dict = load_file(str(model_dir / "vision_model.safetensors"))
    model.base_model.model.vision_model.load_state_dict(vision_state_dict,
                                                        strict=True)
    proj_state_dict = load_file(str(model_dir / "mm_projector.safetensors"))
    model.base_model.model.mm_projector.load_state_dict(proj_state_dict,
                                                        strict=True)

    for name, param in model.model.model.named_parameters():
        if "lora_" not in name.lower():
            param.data = param.data.bfloat16()
    model.lm_head.to(torch.bfloat16)
    model = model.cuda()

    params_lora = [name
                   for name, _ in model.named_parameters()
                   if 'lora_' in name]
    print("="*30)
    print("params_lora")
    print("="*30)
    pprint(params_lora)

    # SECTION - 학습에서 사용된 tokenizer Load
    tokenizer = AutoTokenizer.from_pretrained(model_name,
                                              use_fast=False,
                                              padding_side='left')
    # Setting `pad_token_id` to `eos_token_id`:2 for open-end generation.
    # tokenizer.pad_token = tokenizer.eos_token
    # tokenizer.pad_token_id = tokenizer.eos_token_id
    # model.generation_config.pad_token_id = tokenizer.eos_token_id

    # FIXME - crop_size is same as image_size
    dataset = MP100(
        tokenizer=None,
        data_path=os.path.join(args.question_file),
        multimodal_cfg=dict(image_folder=args.image_folder,
                            image_size=config.crop_size,
                            crop_size=config.crop_size),
        image_size=config.crop_size,
        cur_token_len=config.num_patches,
        is_train=False
    )

    worker(model,
           tokenizer,
           dataset,
           args,
           args.output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", type=str, default="facebook/opt-350m")
    parser.add_argument("--image-folder", type=str, default="")
    parser.add_argument("--question-file", type=str,
                        default="tables/question.json")
    parser.add_argument("--answers-file", type=str, default="answer.jsonl")
    parser.add_argument("--output-dir", type=str, default="")
    parser.add_argument("--nkg", type=int, default=15)
    args = parser.parse_args()

    eval_model(args)
