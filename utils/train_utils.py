from typing import Dict

import transformers

from models.locllm_v2 import LocLLMConfig
from datasets.mp100 import MP100DatasetExtended

from utils.collate_fn import DataCollatorForSupervisedDataset


def disabled_train(self, mode=True):
    """Overwrite model.train with this function to make sure train/eval mode
    does not change anymore."""
    return self


def safe_save_model_for_hf_trainer(trainer: transformers.Trainer,
                                   output_dir: str):
    """Collects the state dict and dump to disk."""
    state_dict = trainer.model.state_dict()
    if trainer.args.should_save:
        cpu_state_dict = {
            key: value.cpu()
            for key, value in state_dict.items()
        }
        del state_dict
        trainer._save(output_dir, state_dict=cpu_state_dict)  # noqa


def make_supervised_data_module(tokenizer: transformers.PreTrainedTokenizer,
                                data_args) -> Dict:
    """Make dataset and collator for supervised fine-tuning.

    # NOTE - DinoV2 use a default image_means/stds
        - means = [0.485, 0.456, 0.406]
        - stds  = [0.229, 0.224, 0.225]
    """
    dataset_cls = MP100DatasetExtended
    train_dataset = dataset_cls(tokenizer=tokenizer,
                                data_path=data_args.data_path,
                                multimodal_cfg=dict(
                                    image_folder=data_args.image_folder,
                                    data_augmentation=data_args.data_augmentation,
                                    image_size=data_args.image_size,
                                    crop_size=data_args.crop_size,
                                    conv_format=data_args.conv_format),
                                image_size=data_args.image_size,
                                cur_token_len=data_args.image_token_len,
                                n_inst_kpts=data_args.n_inst_kpts)
    data_collator = DataCollatorForSupervisedDataset(tokenizer=tokenizer)
    return dict(train_dataset=train_dataset,
                eval_dataset=None,
                data_collator=data_collator)


def print_trainable_parameters(model):
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(
        f"trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param:.2f}"
    )


def save_with_pretrained_config(config: LocLLMConfig, save_dir):
    config.save_pretrained(save_dir)
