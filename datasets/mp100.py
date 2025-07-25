"""instruction 다양하게 구성"""
from __future__ import annotations

import logging
import os
import random
from copy import deepcopy

import cv2
import numpy as np
import torch
import transformers
from pycocotools.coco import COCO
from torch.utils.data import Dataset
from torchvision import transforms

from .constants_cape import CAPE_KEYPOINT_NAME, CAPEKeypointLocationDescription
from .conversation import conv_cape_llava
from .utils import get_affine_transform, affine_transform


DEFAULT_IMAGE_PATCH_TOKEN = "<im_patch>"
IGNORE_INDEX = -100


QUESTION_LIST = [
    "Where is the {keypoint} of this object in this image? Please provide its coordinates.",
    "Can you find out the {keypoint} of this object following the reference in this image?",
    "Can you search the {keypoint} of this object in this image, based on the following reference?",
    "where is the {keypoint} of this object in this image? Please find them with following the reference.",
    "where is the {keypoint} of this object in this image? Please figure out them based on the reference",
    # claude 3.5
    "Based on the provided reference, could you help me locate the {keypoint} of this object?",
    "Using the reference as a guide, can you identify where the {keypoint} is positioned on this object?",
    "I need assistance finding the {keypoint} of this object - please use the reference to help locate it.",
    "Following the given reference, please point out the {keypoint} location for this particular object.",
    "Can you determine the position of this object's {keypoint} by consulting the provided reference?",
    "Referring to the given example, please identify and locate the {keypoint} on this object.",
    "With the help of the reference material, could you pinpoint the {keypoint} of the object shown?",
    "Please examine the reference and indicate where the {keypoint} can be found on this object.",
    "Looking at the reference for guidance, can you show me where to find the {keypoint} on this object?",
    "By following the reference provided, please help identify the location of this object's {keypoint}.",
    # ChatGPT-o1
    "Could you locate the {keypoint} of this object in the image? Please find it using the reference provided.",
    "Please identify where the {keypoint} of this object is in this picture, following the given reference.",
    "Where can the {keypoint} of this object be found in this image? Use the reference to locate them.",
    "Locate the {keypoint} of this object in the image by following the reference.",
    "Please find the {keypoint} of this object in the image, using the provided reference.",
    "Can you show me where the {keypoint} of this object is in this image? Refer to the reference to find them.",
    "Using the reference, please identify the {keypoint} of this object within this image.",
    "Find the location of the object's {keypoint} in this image, following the reference.",
    "Where are the {keypoint} of this object located in this image? Please use the reference to find them.",
    "Please point out the {keypoint} of this object in this picture, using the reference for guidance.",
]


class MP100(Dataset):
    """Dataset for supervised fine-tuning.

    #NOTE - LLaVA-style의 instruction 구성 + Reference

    <img_patch><img_patch><img_patch>...
    User: "Where is the {keypoint name} of this object in this image? Please provide its coordinates."
    Reference: {keypoint description}
    Assistant: "[0.123,0.456]"

    # NOTE
        - image-text(instruction) pair 구성방식 변경
            * [AS-IS] 1객체-5키포인트로 instruction 구성(객체 중복 허용x)
            * [TO-BE] 1객체-4키포인트로 instruction 구성(객체 중복 허용o, 학습에서 누락되는 키포인트 없도록)

    """

    def __init__(
        self,
        data_path: str,
        tokenizer: transformers.PreTrainedTokenizer,
        multimodal_cfg: dict,
        cur_token_len=256,
        image_size: int = 224,
        image_means: list[float] = [0.485, 0.456, 0.406],
        image_stds: list[float] = [0.229, 0.224, 0.225],
        is_train=True,
        n_inst_kpts=4
    ):
        super().__init__()
        self.tokenizer = tokenizer
        self.multimodal_cfg = multimodal_cfg
        self.is_train = is_train

        logging.warning("Loading data...")
        self.size = image_size
        self.aspect_ratio = 1.0
        self.pixel_std = 200

        self.n_inst_kpts = n_inst_kpts  # 객체별 instruction을 구성할 keypoint 개수
        self.cur_token_len = cur_token_len

        list_data_dict = self._get_db(data_path)
        logging.warning(
            f"The number of samples is {len(list_data_dict)}",
        )
        self.list_data_dict = list_data_dict

        logging.warning("Formatting inputs...Skip in lazy mode")

        self.conv_format = self.multimodal_cfg.get("conv_format", "cape")
        self.conv = conv_cape_llava.copy()
        print("Use Conv Format ", self.conv_format)
        if "data_augmentation" in self.multimodal_cfg.keys():
            self.data_aug = self.multimodal_cfg["data_augmentation"]
        else:
            self.data_aug = False

        self.transforms = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(image_means, image_stds),
            ],
        )

    def __len__(self):
        return len(self.list_data_dict)

    def __getitem__(self, i):
        if self.is_train:
            while True:
                use_item, data_dict = self._parse_data_item(i)
                if use_item:
                    break
                else:
                    i = random.randint(0, self.__len__() - 1)
            return data_dict
        else:
            return self._parse_data_item_val(i)

    def _get_db(self, data_path):
        coco = COCO(data_path)
        list_data_dict = []
        instance_id = 0
        for index in coco.getImgIds():
            im_ann = coco.loadImgs(index)[0]
            width = im_ann["width"]
            height = im_ann["height"]
            annIds = coco.getAnnIds(imgIds=index, iscrowd=False)
            objs = coco.loadAnns(annIds)
            # sanitize bboxes
            valid_objs = []
            for obj in objs:
                x, y, w, h = obj["bbox"]
                x1 = np.max((0, x))
                y1 = np.max((0, y))
                x2 = np.min((width - 1, x1 + np.max((0, w - 1))))
                y2 = np.min((height - 1, y1 + np.max((0, h - 1))))
                if obj["area"] > 0 and x2 >= x1 and y2 >= y1:
                    obj["clean_bbox"] = [x1, y1, x2-x1, y2-y1]
                    valid_objs.append(obj)
            objs = valid_objs

            for obj in objs:
                category_id = obj["category_id"]
                category = coco.loadCats(category_id)[0]
                supercategory = category["supercategory"]
                category_name = category["name"]

                # ignore objs without keypoints annotation
                if max(obj["keypoints"]) == 0:
                    continue

                num_joints = len(obj["keypoints"]) // 3

                joints_3d = np.zeros(
                    [num_joints, 3],
                    dtype=np.float32,
                )
                joints_3d_vis = np.zeros(
                    [num_joints, 3],
                    dtype=np.float32,
                )
                # visible = np.zeros((num_joints), dtype=np.float32)
                for ipt in range(num_joints):
                    joints_3d[ipt, 0] = obj["keypoints"][ipt * 3 + 0]
                    joints_3d[ipt, 1] = obj["keypoints"][ipt * 3 + 1]
                    joints_3d[ipt, 2] = 0
                    t_vis = obj["keypoints"][ipt * 3 + 2]
                    # visible[ipt] = t_vis
                    if t_vis > 1:
                        t_vis = 1
                    joints_3d_vis[ipt, 0] = t_vis
                    joints_3d_vis[ipt, 1] = t_vis
                    joints_3d_vis[ipt, 2] = 0

                center, scale = self._box2cs(obj["clean_bbox"][:4])

                if self.is_train:
                    kpt_ids = list(range(num_joints))
                    # NOTE - shuffle keypoint indices
                    np.random.shuffle(kpt_ids)
                    grouped_kpt_ids = self._group_kpt_ids(kpt_ids)
                    for _kpt_ids in grouped_kpt_ids:
                        list_data_dict.append(
                            {
                                "file_name": im_ann["file_name"],
                                "image_id": index,
                                "center": center,
                                "scale": scale,
                                "joints_3d": joints_3d,
                                "joints_3d_vis": joints_3d_vis,
                                "instance_id": instance_id,
                                "bbox": obj["clean_bbox"][:4],
                                "num_joints": num_joints,
                                "supercategory": supercategory,
                                "category": category_name,
                                "category_id": category_id,
                                "kpt_ids": _kpt_ids,
                            },
                        )
                    instance_id += 1
                else:
                    list_data_dict.append(
                        {
                            "file_name": im_ann["file_name"],
                            "image_id": index,
                            "center": center,
                            "scale": scale,
                            "joints_3d": joints_3d,
                            "joints_3d_vis": joints_3d_vis,
                            "instance_id": instance_id,
                            "bbox": obj["clean_bbox"][:4],
                            "num_joints": num_joints,
                            "supercategory": supercategory,
                            "category": category_name,
                            "category_id": category_id,
                            'skeleton': coco.cats[category_id]['skeleton'],
                            'annotation_id': obj['id']
                        },
                    )
                    instance_id += 1

        return list_data_dict

    def _parse_data_item_val(self, i) -> dict:
        sources = self.list_data_dict[i]
        result_dict = {}
        image, joints, joints_vis, c, s = self._get_pose_item(
            deepcopy(sources))
        image_id = sources["image_id"]
        result_dict["images"] = image
        result_dict["image_id"] = image_id
        result_dict["file_name"] = sources["file_name"]
        result_dict["c"] = c
        result_dict["s"] = s
        result_dict["joints_inp"] = joints
        result_dict["joints_vis_inp"] = joints_vis
        result_dict["joints"] = sources["joints_3d"]
        result_dict["joints_vis"] = sources["joints_3d_vis"]
        result_dict["category"] = sources["category"]
        result_dict["category_id"] = sources["category_id"]
        result_dict["supercategory"] = sources["supercategory"]
        result_dict["num_joints"] = sources["num_joints"]
        result_dict["bbox"] = sources["bbox"]
        result_dict["skeleton"] = sources["skeleton"]
        result_dict["annotation_id"] = sources["annotation_id"]
        return result_dict

    def _group_kpt_ids(self, kpt_ids):
        n_joints = len(kpt_ids)

        def _chunk(ls: list, chunk_size: int):
            return [ls[i:i+chunk_size] for i in range(0, len(ls), chunk_size)]

        # n_groups, n_rests = divmod(n_joints, self.n_inst_kpts)
        n_rests = n_joints % self.n_inst_kpts
        if n_rests != 0:
            # 나누어 떨어지지 않는 경우, 나머지부분을 제외한 idxs에서 부족한만큼 random sampling!
            n_sampling = self.n_inst_kpts - n_rests
            additionals = random.sample(kpt_ids[:-n_rests], k=n_sampling)
        else:
            additionals = []

        # kpt_ids *= n_groups
        kpt_ids += additionals

        grouped_kpt_ids = _chunk(kpt_ids, self.n_inst_kpts)
        return grouped_kpt_ids

    def _parse_data_item(self, i) -> dict[str, torch.Tensor]:
        """training에 사용될 input 생성

        #ANCHOR - item의 정의가 변경됨
            - [AS-IS] item=객체
                * 객체별로 가진 키포인트중 최대 5개만 학습에 반영
                * 해당 객체는 한 번 학습에 사용 후 다음 epoch까지 사용 x
            - [TO-BE] item=키포인트 그룹 하나
                * 객체별로 정의된 키포인트를 일정 크기로 grouping
                * group마다 instruction 생성하여 input 구성(객체 이미지 중복 허용)
                * 이에 따라 객체는 하나의 epoch에서 여러 번 학습에 포함됨

        """
        use_item = False
        sources = deepcopy(self.list_data_dict[i])
        data_dict = {}

        image, joints, joints_vis, _, _ = self._get_pose_item(sources)

        data_dict["image"] = image
        data_dict["has_image"] = True

        category_id = sources["category_id"]
        kpt_ids = sources["kpt_ids"]

        is_select = False
        kpt_names = []
        kpt_descs = []
        captions = []
        keypoint_names = CAPE_KEYPOINT_NAME[category_id]
        # SECTION - 1개의 object의 visible keypoints에 대한 Q/A 설정
        for idx in kpt_ids:
            x, y, v = joints[idx, 0], joints[idx, 1], joints_vis[idx, 0]
            if v < 1:
                continue
            if x < 0 or x >= self.size or y < 0 or y >= self.size:
                continue

            # NOTE - Normalize the keypoint coordinates' scale to 0 ~ 1
            x = x / self.size
            y = y / self.size
            location_tokens = f"[{x:.3f},{y:.3f}]"

            kpt_name = keypoint_names[idx]
            kpt_names.append(kpt_name)
            kpt_descs.append(
                CAPEKeypointLocationDescription[category_id][kpt_name],
            )
            captions.append(location_tokens)
            is_select = True

        if not is_select:
            return use_item, {}

        self.conv.messages = []  # reset at each object
        for idx in range(self.n_inst_kpts):
            if idx >= len(kpt_descs):
                break
            question = QUESTION_LIST[0]
            question = question.format(keypoint=kpt_names[idx])
            # role: User / Reference / Assistant
            self.conv.append_message(self.conv.roles[0], question)

            kpt_desc = kpt_descs[idx]
            self.conv.append_message(self.conv.roles[1], kpt_desc)
            self.conv.append_message(self.conv.roles[2], captions[idx])

        text_inputs = self.conv.get_prompt()
        text_inputs = \
            self.cur_token_len * DEFAULT_IMAGE_PATCH_TOKEN + "\n" \
            + text_inputs

        inputs = self.tokenizer(text_inputs,
                                return_tensors="pt",
                                padding="longest",
                                max_length=self.tokenizer.model_max_length,
                                truncation=True).input_ids[0]
        target = inputs.clone()
        sep = self.conv.sep1 + self.conv.roles[2] + ": "  # "\nAssistant: "

        rounds = text_inputs.split(self.conv.sep2)
        cur_len = 1
        target[:cur_len] = IGNORE_INDEX
        for i, rou in enumerate(rounds):
            if rou == "":
                break
            # ["<image>User: where is ~\nReference: ~~~~", "[0.235, 0.497]"]
            parts = rou.split(sep)
            if len(parts) != 2:
                break
            # parts = ["<image>User: where is ~\nReference: ~~~~", "\nAssistant: [0.235, 0.497]"]
            parts[0] += sep
            round_len = len(self.tokenizer(rou).input_ids)

            instruction_len = len(self.tokenizer(parts[0]).input_ids) - 2

            target[cur_len: cur_len + instruction_len] = IGNORE_INDEX
            cur_len += round_len

        data_dict.update(
            dict(input_ids=inputs,
                 labels=target),
        )
        return True, data_dict

    def _get_pose_item(
        self,
        sources: dict,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, float]:
        file_name = sources["file_name"]
        image_folder = self.multimodal_cfg["image_folder"]
        image_file = os.path.join(image_folder, file_name)
        image = cv2.imread(
            image_file, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION,
        )
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # process image
        joints = sources["joints_3d"]
        joints_vis = sources["joints_3d_vis"]
        c = sources["center"]
        s = sources["scale"]
        num_joints = sources["num_joints"]
        r = 0

        if self.data_aug and self.is_train:
            sf = 0.3
            rf = 40
            s = s * np.clip(np.random.randn()*sf + 1, 1 - sf, 1 + sf)
            r = random.uniform(-rf, rf) if random.random() <= 0.5 else 0

        trans = get_affine_transform(c, s, r, (int(self.size), int(self.size)))
        image = cv2.warpAffine(image,
                               trans,
                               (int(self.size), int(self.size)),
                               flags=cv2.INTER_LINEAR)
        image = self.transforms(image)

        for i in range(num_joints):
            if joints_vis[i, 0] > 0.0:
                joints[i, 0:2] = affine_transform(joints[i, 0:2], trans)

        return image, joints, joints_vis, c, s

    def _box2cs(self, box):
        x, y, w, h = box[:4]
        return self._xywh2cs(x, y, w, h)

    def _xywh2cs(self, x, y, w, h):
        center = np.zeros((2), dtype=np.float32)
        center[0] = x + w * 0.5
        center[1] = y + h * 0.5

        if w > self.aspect_ratio * h:
            h = w * 1.0 / self.aspect_ratio
        elif w < self.aspect_ratio * h:
            w = h * self.aspect_ratio
        scale = np.array(
            [w * 1.0 / self.pixel_std, h * 1.0 / self.pixel_std],
            dtype=np.float32)
        if center[0] != -1:
            # scale = scale * 1.25
            scale = scale * 1.0

        return center, scale
