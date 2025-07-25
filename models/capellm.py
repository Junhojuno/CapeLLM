#    Copyright 2023 Haotian Liu
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from __future__ import annotations

from typing import Optional, Union

import torch
from torch import nn
from torch.nn import CrossEntropyLoss
from transformers import (
    AutoConfig, AutoModelForCausalLM,
)
from transformers import PreTrainedModel, PretrainedConfig
from transformers.modeling_outputs import (
    BaseModelOutputWithPast,
    CausalLMOutputWithPast
)
from transformers.utils import logging

from .dino import dinov2_vitl14, dinov2_vitl14_reg
from .lora import lora_dino


logger = logging.get_logger(__name__)


DEFAULT_IMAGE_PATCH_TOKEN = "<im_patch>"


def disabled_train(self, mode=True):
    """Overwrite model.train with this function to make sure train/eval mode
    does not change anymore.
    """
    return self


def convert_weights_to_dtype(model: nn.Module, dtype):
    """Convert applicable model parameters to fp16"""

    def _convert_weights_to_dtype(layer):
        if isinstance(layer, (nn.Conv1d, nn.Conv2d, nn.Linear)):
            layer.weight.data = layer.weight.data.to(dtype=dtype)
            if layer.bias is not None:
                layer.bias.data = layer.bias.data.to(dtype=dtype)

    model.apply(_convert_weights_to_dtype)


class CapeLLMConfig(PretrainedConfig):
    model_type = "cape-llm"

    def __init__(
        self,
        llm_path=None,
        vision_path=None,
        lora_vision_r=8,
        lora_vision_alpha=16,
        lora_vision_dropout=0.05,
        lora_vision_enable=False,
        lora_llm_enable=False,
        lora_llm_r=8,
        lora_llm_alpha=16.0,
        lora_llm_dropout=0.0,
        crop_size=224,
        **kwargs,
    ):
        self.llm_path = llm_path
        self.vision_path = vision_path
        self.lora_vision_r = lora_vision_r
        self.lora_vision_alpha = lora_vision_alpha
        self.lora_vision_dropout = lora_vision_dropout
        self.lora_vision_enable = lora_vision_enable
        self.lora_llm_enable = lora_llm_enable
        self.lora_llm_r = lora_llm_r
        self.lora_llm_alpha = lora_llm_alpha
        self.lora_llm_dropout = lora_llm_dropout
        self.crop_size = crop_size
        super().__init__(**kwargs)


class CapeLLMModel(PreTrainedModel):
    config_class = CapeLLMConfig

    def __init__(self, config: CapeLLMConfig):
        # NOTE - LLM에 맞는 config를 update
        llm_config = AutoConfig.from_pretrained(config.llm_path)
        config.update(llm_config.__dict__)
        super().__init__(config)
        # Initialize weights and apply final processing
        self._initialize_language_model(config)
        self._initialize_visual_encoder(config)

        num_features = self.vision_model.num_features
        self.mm_projector = nn.Linear(num_features, config.hidden_size)

        num_patches = (config.crop_size // self.vision_model.patch_size) ** 2
        self.config.num_patches = num_patches

    def _initialize_visual_encoder(self, config: CapeLLMConfig) -> None:
        # NOTE - Apply LoRA to visual encoder inside the model
        print("config.lora_vision_enable: ", config.lora_vision_enable)
        print("config.vision_path: ", config.vision_path)
        with lora_dino(r=config.lora_vision_r,
                       alpha=config.lora_vision_alpha,
                       dropout=config.lora_vision_dropout,
                       enabled=config.lora_vision_enable):
            if "_reg4" in config.vision_path:
                vision_model = dinov2_vitl14_reg(pretrained=False)
            else:
                vision_model = dinov2_vitl14(pretrained=False)
            state_dict = torch.load(config.vision_path)
            msg = vision_model.load_state_dict(state_dict, strict=False)
            print(f"dino init: {msg}")
            self.vision_model = vision_model
            for _, module in self.vision_model.named_modules():
                module._is_hf_initialized = True

    def _initialize_language_model(self, config: CapeLLMConfig) -> None:
        # NOTE - Not to Apply LoRA to Language model inside the model
        llm = AutoModelForCausalLM.from_pretrained(config.llm_path)
        self.model = llm.model
        self.vocab_size = llm.vocab_size
        self.lm_head = llm.lm_head

    def get_model(self):
        return self.model

    def encode_image(self, images):
        image_forward_out = self.vision_model(images)
        image_features = image_forward_out["x_norm_patchtokens"]
        image_features = self.mm_projector(image_features)
        return image_features

    def _init_weights(self, module):
        std = self.config.initializer_range
        if isinstance(module, nn.Linear):
            module.weight.data.normal_(mean=0.0, std=std)
            if module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.Embedding):
            module.weight.data.normal_(mean=0.0, std=std)
            if module.padding_idx is not None:
                module.weight.data[module.padding_idx].zero_()

    def forward(
        self,
        input_ids: torch.LongTensor = None,
        position_ids: Optional[torch.LongTensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        past_key_values: Optional[list[torch.FloatTensor]] = None,
        inputs_embeds: Optional[torch.FloatTensor] = None,
        labels: Optional[torch.LongTensor] = None,
        use_cache: Optional[bool] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        images: Optional[torch.FloatTensor] = None,
        has_images: Optional[bool] = None,
        return_dict: Optional[bool] = None,
    ) -> Union[tuple, BaseModelOutputWithPast]:

        assert inputs_embeds is None

        # False, False, True
        output_attentions = (
            output_attentions
            if output_attentions is not None
            else self.config.output_attentions
        )
        output_hidden_states = (
            output_hidden_states
            if output_hidden_states is not None
            else self.config.output_hidden_states
        )
        return_dict = (
            return_dict
            if return_dict is not None
            else self.config.use_return_dict
        )

        useful_images = []
        for image, has_image in zip(images, has_images):
            if has_image:
                useful_images.append(image)
        if len(useful_images) > 0:
            useful_images = torch.stack(useful_images, dim=0)
            image_features = self.encode_image(useful_images)

        new_inputs_embeds = []
        cur_image_index = 0
        batch_id = 0
        for input_id, has_image in zip(input_ids, has_images):
            if has_image and (input_id.shape[0] != 1 or self.training):
                image_feature = image_features[cur_image_index]
                cur_image_index += 1
                num_patches = image_feature.shape[0]
                if (input_id == self.config.im_patch_token).sum() != num_patches:
                    raise ValueError(
                        "The number of image patch tokens should be the same as the number of image patches. "
                        f"# image tokens in input_id(={(input_id == self.config.im_patch_token).sum()}) "
                        f"num_patches(={num_patches})"
                    )
                masked_indices = torch.where(
                    input_id == self.config.im_patch_token)[0]
                mask_index_start = masked_indices[0]
                if (masked_indices != torch.arange(mask_index_start, mask_index_start+num_patches, device=masked_indices.device, dtype=masked_indices.dtype)).any():
                    raise ValueError(
                        "The image patch tokens should be consecutive.")
                pre_input_embed = self.model.embed_tokens(
                    input_ids[batch_id:batch_id+1, :mask_index_start],
                )[0]
                nxt_input_embed = self.model.embed_tokens(
                    input_ids[batch_id:batch_id+1,
                              mask_index_start+num_patches:],
                )[0]

                image_feature = image_feature.to(pre_input_embed.dtype)

                new_inputs_embed = torch.cat(
                    (pre_input_embed, image_feature, nxt_input_embed), dim=0)
                new_inputs_embeds.append(new_inputs_embed)
            else:
                inputs_embed = self.model.embed_tokens(
                    input_ids[batch_id:batch_id+1])[0]
                new_inputs_embeds.append(inputs_embed)
            batch_id += 1

        new_inputs_embeds = torch.stack(new_inputs_embeds, dim=0)

        # decoder outputs consists of (dec_features, layer_state, dec_hidden, dec_attn)
        llm_output = self.model(
            input_ids=None,
            position_ids=position_ids,
            attention_mask=attention_mask,
            past_key_values=past_key_values,
            inputs_embeds=new_inputs_embeds,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        hidden_states = llm_output[0]
        logits = self.lm_head(hidden_states)

        loss = None
        if labels is not None:
            # Shift so that tokens < n predict n
            shift_logits = logits[..., :-1, :].contiguous()
            shift_labels = labels[..., 1:].contiguous()
            # Flatten the tokens
            loss_fct = CrossEntropyLoss()
            shift_logits = shift_logits.view(-1, self.config.vocab_size)
            shift_labels = shift_labels.view(-1)
            # Enable model/pipeline parallelism
            shift_labels = shift_labels.to(shift_logits.device)
            loss = loss_fct(shift_logits, shift_labels)

        if not return_dict:
            output = (logits,) + llm_output[1:]
            return (loss,) + output if loss is not None else output

        return CausalLMOutputWithPast(
            loss=loss,
            logits=logits,
            past_key_values=llm_output.past_key_values,
            hidden_states=llm_output.hidden_states,
            attentions=llm_output.attentions,
        )

    def prepare_inputs_for_generation(
        self,
        input_ids,
        past_key_values=None,
        attention_mask=None,
        inputs_embeds=None,
        **kwargs,
    ):
        if past_key_values:
            input_ids = input_ids[:, -1:]

        position_ids = kwargs.get("position_ids", None)
        if attention_mask is not None and position_ids is None:
            # create position_ids on the fly for batch generation
            position_ids = attention_mask.long().cumsum(-1) - 1
            position_ids.masked_fill_(attention_mask == 0, 1)
            if past_key_values:
                position_ids = position_ids[:, -1].unsqueeze(-1)

        # if `inputs_embeds` are passed, we only want to use them in the 1st generation step
        if inputs_embeds is not None and past_key_values is None:
            model_inputs = {"inputs_embeds": inputs_embeds}
        else:
            model_inputs = {"input_ids": input_ids}

        model_inputs.update(
            {
                "position_ids": position_ids,
                "past_key_values": past_key_values,
                "use_cache": kwargs.get("use_cache"),
                "attention_mask": attention_mask,
                "images": kwargs.get("images", None),
                "has_images": kwargs.get("has_images", None),
            },
        )
        return model_inputs

    def initialize_vision_tokenizer(self, tokenizer):
        tokenizer.add_tokens([DEFAULT_IMAGE_PATCH_TOKEN], special_tokens=True)
        self.config.im_patch_token = tokenizer.convert_tokens_to_ids(
            [DEFAULT_IMAGE_PATCH_TOKEN])[0]


AutoConfig.register(CapeLLMConfig.model_type, CapeLLMConfig)
AutoModelForCausalLM.register(CapeLLMConfig, CapeLLMModel)
