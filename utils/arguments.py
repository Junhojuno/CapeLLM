from typing import Optional

from dataclasses import dataclass, field

import transformers


@dataclass
class ModelArguments:
    # model_name_or_path: Optional[str] = field(default="facebook/opt-125m")
    llm_path: Optional[str] = field(default="")
    vision_path: Optional[str] = field(default=None)
    pretrain_mm_mlp_adapter: Optional[str] = field(default=None)
    tune_mm_mlp_adapter: bool = field(default=True)
    freeze_vit: bool = field(default=True)
    freeze_llm: bool = field(default=True)


@dataclass
class DataArguments:
    data_path: str = field(default=None,
                           metadata={"help": "Path to the training data."})
    image_token_len: int = field(default=256)
    image_folder: Optional[str] = field(default=None)
    image_size: int = field(default=224)
    crop_size: int = field(default=224)
    data_augmentation: bool = field(default=False)
    conv_format: str = field(default="cape")
    n_inst_kpts: int = field(default=4)


@dataclass
class TrainingArguments(transformers.TrainingArguments):
    cache_dir: Optional[str] = field(default=None)
    optim: str = field(default="adamw_torch")
    remove_unused_columns: bool = field(default=False)
    force_fsdp: bool = field(default=False)
    model_max_length: int = field(
        default=512,
        metadata={
            "help":
            "Maximum sequence length. Sequences will be right padded (and possibly truncated)."
        },
    )
    seed: int = field(default=42)


@dataclass
class LoRAArguments:
    lora_vision_r: int = field(default=8)
    lora_vision_alpha: float = field(default=16)
    lora_vision_dropout: float = field(default=0.05)
    lora_vision_enable: bool = field(default=False)
    lora_llm_r: int = field(default=8)
    lora_llm_alpha: float = field(default=16)
    lora_llm_dropout: float = field(default=0.05)
    lora_llm_enable: bool = field(default=False)
