from typing import Dict, Sequence

from dataclasses import dataclass
import torch
import transformers


IGNORE_INDEX = -100


@dataclass
class DataCollatorForSupervisedDataset(object):
    """Collate examples for supervised fine-tuning."""

    tokenizer: transformers.PreTrainedTokenizer

    def __call__(self, instances: Sequence[Dict]) -> Dict[str, torch.Tensor]:
        input_ids, labels = tuple(
            [instance[key] for instance in instances]
            for key in ("input_ids", "labels")
        )
        # NOTE - pad_token_id == unk_token_id(=0)
        # 원래 Mistral의 pad_token_id == eos_token_id(=2)
        # 본 코드 내에서 unk_token_id로 변경
        input_ids = torch.nn.utils.rnn.pad_sequence(
            input_ids,
            batch_first=True,
            padding_value=self.tokenizer.pad_token_id)
        labels = torch.nn.utils.rnn.pad_sequence(labels,
                                                 batch_first=True,
                                                 padding_value=IGNORE_INDEX)
        batch = dict(
            input_ids=input_ids,
            labels=labels,
            attention_mask=input_ids.ne(self.tokenizer.pad_token_id),
        )

        if 'image' in instances[0]:
            images = [instance['image'] for instance in instances]
            assert all(x is not None and x.shape ==
                       images[0].shape for x in images)
            batch['images'] = torch.stack(images)

        assert 'has_image' in instances[0].keys()
        has_images = [instance['has_image'] for instance in instances]
        batch['has_images'] = has_images

        return batch
