"""LLaVA-instruction based training"""
from pprint import pprint
import pathlib
from typing import Dict, Optional

from dataclasses import dataclass, field
import torch
import transformers

from models.capellm import CapeLLMModel, CapeLLMConfig
from datasets.mp100 import MP100

from utils.arguments import (
    ModelArguments,
    TrainingArguments,
    LoRAArguments
)
from utils.collate_fn import DataCollatorForSupervisedDataset
from utils.train_utils import (
    print_trainable_parameters,
    save_with_pretrained_config,
    safe_save_model_for_hf_trainer,
    disabled_train
)


@dataclass
class DataArguments:
    data_path: str = field(default=None,
                           metadata={"help": "Path to the training data."})
    image_token_len: int = 0
    image_folder: Optional[str] = field(default=None)
    image_size: int = field(default=224)
    crop_size: int = field(default=224)
    data_augmentation: bool = field(default=False)
    conv_format: str = field(default="cape")
    n_inst_kpts: int = field(default=4)


def make_supervised_data_module(tokenizer: transformers.PreTrainedTokenizer,
                                data_args) -> Dict:
    """Make dataset and collator for supervised fine-tuning.

    # NOTE - DinoV2 use a default image_means/stds
        - means = [0.485, 0.456, 0.406]
        - stds  = [0.229, 0.224, 0.225]
    """
    dataset_cls = MP100
    train_dataset = dataset_cls(
        tokenizer=tokenizer,
        data_path=data_args.data_path,
        multimodal_cfg=dict(
            image_folder=data_args.image_folder,
            data_augmentation=data_args.data_augmentation,
            image_size=data_args.image_size,
            crop_size=data_args.crop_size,
            conv_format=data_args.conv_format
        ),
        image_size=data_args.image_size,
        cur_token_len=data_args.image_token_len,
        n_inst_kpts=data_args.n_inst_kpts,
    )
    data_collator = DataCollatorForSupervisedDataset(tokenizer=tokenizer)
    return dict(train_dataset=train_dataset,
                eval_dataset=None,
                data_collator=data_collator)


def train():
    from peft import get_peft_model, LoraConfig
    parser = transformers.HfArgumentParser(
        (ModelArguments, DataArguments, TrainingArguments, LoRAArguments)
    )
    model_args, data_args, training_args, lora_args = \
        parser.parse_args_into_dataclasses()

    # NOTE - for reproducabiility, fix the training randomness
    # FIXME - it is twice slower than before
    transformers.enable_full_determinism(training_args.seed)

    # SECTION - Create  tokenizer
    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_args.llm_path,
        cache_dir=training_args.cache_dir,
        model_max_length=training_args.model_max_length,
        padding_side="right",
        use_fast=False,
    )
    if model_args.llm_path.endswith("Meta-Llama-3.1-8B") \
            or model_args.llm_path.endswith("Llama-3.2-1B") \
            or model_args.llm_path.endswith("Llama-3.2-3B"):
        if tokenizer.pad_token is None:
            # NOTE - use eos_token as pad_token
            # https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct/discussions/101
            # update pad_token_id to eos_token_id
            tokenizer.pad_token = tokenizer.eos_token
    else:
        tokenizer.pad_token = tokenizer.unk_token

    # SECTION - Create  model
    config = CapeLLMConfig(
        llm_path=model_args.llm_path,
        vision_path=model_args.vision_path,
        lora_vision_r=lora_args.lora_vision_r,
        lora_vision_alpha=lora_args.lora_vision_alpha,
        lora_vision_dropout=lora_args.lora_vision_dropout,
        lora_vision_enable=lora_args.lora_vision_enable,
        lora_llm_enable=lora_args.lora_llm_enable,
        crop_size=data_args.crop_size,
    )
    model = CapeLLMModel(config)

    # NOTE - load mm projector weights
    if model_args.pretrain_mm_mlp_adapter is not None:
        print('Load pretrained mm_projector from: ',
              model_args.pretrain_mm_mlp_adapter)
        mm_projector_weights = torch.load(
            model_args.pretrain_mm_mlp_adapter, map_location='cpu')
        update_state = {}
        update_state['weight'] = mm_projector_weights['model.mm_projector.weight']
        update_state['bias'] = mm_projector_weights['model.mm_projector.bias']
        model.mm_projector.load_state_dict(update_state, strict=True)

    model.config.use_cache = False

    model.config.eos_token_id = tokenizer.eos_token_id
    model.config.bos_token_id = tokenizer.bos_token_id
    model.config.pad_token_id = tokenizer.pad_token_id
    model.initialize_vision_tokenizer(tokenizer=tokenizer)

    lora_config = LoraConfig(
        r=lora_args.lora_llm_r,
        lora_alpha=lora_args.lora_llm_alpha,
        lora_dropout=lora_args.lora_llm_dropout,
        target_modules=[
            "q_proj", "v_proj",
        ],
        bias="none",
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, lora_config)

    # NOTE - change LLM and head dtype to bfloat16
    dtype = torch.bfloat16
    model.model.to(dtype)
    model.lm_head.to(dtype)

    # SECTION - determine trainable parameters,
    # visual encoder and llm are trainable only on LoRA params
    for param in model.base_model.parameters():
        param.requires_grad_(False)

    # ANCHOR - (1) mm_projector -> Trainable
    if model_args.tune_mm_mlp_adapter:
        for p in model.base_model.model.mm_projector.parameters():
            p.requires_grad = True

    # ANCHOR - (2) Visual Encoder -> Partially trainable(LoRA)
    if not model_args.freeze_vit:
        assert model.config.lora_vision_enable
        for name, param in model.base_model.model.vision_model.named_parameters():
            if "lora_" not in name:
                param.requires_grad = False
            else:
                param.data = param.data.float()
                param.requires_grad = True
    else:
        model.vision_model.train = disabled_train
        model.vision_model.eval()

    # ANCHOR - (3) LLM -> Partially trainable(LoRA)
    if not model_args.freeze_llm:
        assert model.config.lora_llm_enable
        # NOTE - model.model means LLM
        for name, param in model.base_model.model.model.named_parameters():
            if "lora_" not in name.lower():
                param.requires_grad = False
            else:
                param.data = param.data.float()
                param.requires_grad = True

    data_args.image_token_len = model.config.num_patches
    data_module = make_supervised_data_module(tokenizer=tokenizer,
                                              data_args=data_args)

    # SECTION - check trainable params and start training
    params_grad = [n for n, p in model.named_parameters() if p.requires_grad]
    print("="*30)
    print("param_grad")
    print("="*30)
    pprint(params_grad)
    print_trainable_parameters(model)
    trainer = transformers.Trainer(model=model,
                                   tokenizer=tokenizer,
                                   args=training_args,
                                   **data_module)

    if list(pathlib.Path(training_args.output_dir).glob("checkpoint-*")):
        trainer.train(resume_from_checkpoint=True)
    else:
        trainer.train()

    # SECTION - save the fine-tuned weights and config, ..etc
    trainer.save_state()

    safe_save_model_for_hf_trainer(trainer=trainer,
                                   output_dir=training_args.output_dir)

    # NOTE - 학습에 사용한 config도 저장
    save_with_pretrained_config(config, training_args.output_dir)

    # NOTE - visual encoder(+LoRA)도 학습이 완료되면 별도로 저장
    from safetensors.torch import save_file
    output_dir = pathlib.Path(training_args.output_dir).resolve()
    save_file(
        trainer.model.base_model.model.vision_model.state_dict(),
        str(output_dir / "vision_model.safetensors")
    )
    # NOTE - mm_projector도 학습이 완료되면 별도로 저장
    save_file(
        trainer.model.base_model.model.mm_projector.state_dict(),
        str(output_dir / "mm_projector.safetensors")
    )


if __name__ == "__main__":
    train()
