from __future__ import annotations

from pathlib import Path
import pickle as pk
import time
from collections import OrderedDict

import numpy as np
import torch
import torch.nn.functional as F

from utils.metric import keypoint_pck_accuracy


def disable_torch_init():
    """
    Disable the redundant torch default initialization to accelerate model creation.
    """
    import torch
    setattr(torch.nn.Linear, "reset_parameters", lambda self: None)
    setattr(torch.nn.LayerNorm, "reset_parameters", lambda self: None)


def chunk_indices(n: int, k: int):
    """n개의 키포인트를 k개단위로 나눈다.

    예를 들어,
    n=17, k=10이면, [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16]]
    n=17, k=15이면, [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [15, 16]]
    """
    indices = list(range(n))
    return [indices[i:i + k] for i in range(0, len(indices), k)]


def run_inference_separately(batch: tuple | list,
                             model,
                             tokenizer,
                             num_joints: int,
                             n_limits: int = 15):
    batch_prompts, batch_images, batch_has_images = batch

    if num_joints > n_limits:
        indices_chunks = chunk_indices(num_joints, n_limits)
    else:
        indices_chunks = [list(range(num_joints))]

    outputs = []
    output_scores_concat = []
    for indices in indices_chunks:
        start, end = indices[0], indices[-1]

        prompts = batch_prompts[start:end+1]
        images = batch_images[start:end+1]
        has_images = batch_has_images[start:end+1]

        tokenized_output = tokenizer(
            prompts,
            return_tensors="pt",
            padding="longest",
            max_length=tokenizer.model_max_length,
            truncation=True,
        )
        # (K, 3, H, W)
        images = torch.cat(images, dim=0).cuda()

        input_ids = torch.as_tensor(
            tokenized_output.input_ids).cuda()  # (K, L)
        attention_mask = torch.as_tensor(
            tokenized_output.attention_mask).cuda()

        with torch.inference_mode():
            # NOTE - default: greedy search
            output_dict = model.generate(
                input_ids,
                images=images,
                has_images=has_images,
                attention_mask=attention_mask,
                do_sample=False,
                max_new_tokens=13,
                min_new_tokens=13,
                output_scores=True,
                return_dict_in_generate=True
            )

            output_ids = output_dict['sequences']
            # tuple of (K, vocab_size), len=max_new_tokens
            output_scores = output_dict['scores']

        # (13, k, vocab_size)
        output_scores_concat.append(
            torch.stack(output_scores[:-1], 0)
        )

        for i, (input_id, output_id) in enumerate(zip(input_ids, output_ids)):
            input_token_len = input_id.shape[0]
            n_diff_input_output = (
                input_id != output_id[:input_token_len]).sum().item()
            if n_diff_input_output > 0:
                print(
                    f'[Warning] Sample {i}: {n_diff_input_output}'
                    ' output_ids are not the same as the input_ids'
                )
            output = output_id[input_token_len:].unsqueeze(0)
            output = tokenizer.batch_decode(output,
                                            skip_special_tokens=True)[0]
            output = output.strip()
            outputs.append(output)

    # NOTE - 다시 키포인트 취합
    output_scores_concat = torch.cat(output_scores_concat, dim=1)
    return outputs, output_scores_concat


def decode_output(outputs,
                  output_scores,
                  pattern,
                  num_joints: int,
                  crop_size: int):
    decoded_kpt = np.zeros((num_joints, 3))
    for i in range(len(outputs)):
        # decode coordinates from token
        pred_kpt = outputs[i]
        res = pattern.findall(pred_kpt)
        if len(res) != 2:
            print('Format error', pred_kpt)
        if len(res) == 0:
            continue
        if len(res) == 1:
            x = float(res[0]) * crop_size
            x_pos = pred_kpt.find(res[0])
            x_s = output_scores[x_pos:x_pos+len(res[0]), i, :].cpu()
            x_s = F.softmax(x_s, dim=1)
            x_s = torch.max(x_s, dim=1)[0].mean().float().item()
            y = 0
            y_s = 0
        else:
            x, y = float(res[0]), float(res[1])
            x, y = x * crop_size, y * crop_size

            x_pos = pred_kpt.find(res[0])
            x_s = output_scores[x_pos:x_pos+len(res[0]), i, :].cpu()
            x_s = F.softmax(x_s, dim=1)
            x_s = torch.max(x_s, dim=1)[0].mean().float().item()
            y_pos = pred_kpt.find(res[1])
            y_s = output_scores[y_pos:y_pos+len(res[1]), i, :].cpu()
            y_s = F.softmax(y_s, dim=1)
            y_s = torch.max(y_s, dim=1)[0].mean().float().item()

        decoded_kpt[i, 0] = x
        decoded_kpt[i, 1] = y
        decoded_kpt[i, 2] = (x_s + y_s) / 2.0
    return decoded_kpt


def save_result_per_rank(preds,
                         gts,
                         masks,
                         threshold_bbox,
                         rank,
                         output_dir: Path) -> list[str]:
    pck_results = dict()
    PCK_threshold_list = [0.05, 0.1, 0.15, 0.2, 0.25]
    for pck_thr in PCK_threshold_list:
        pck_results[pck_thr] = []
    for (pred, gt, mask, thr_bbox) in zip(preds, gts, masks, threshold_bbox):
        for pck_thr in PCK_threshold_list:
            _, pck, _ = keypoint_pck_accuracy(np.expand_dims(pred, 0),
                                              np.expand_dims(gt, 0),
                                              np.expand_dims(mask, 0),
                                              pck_thr,
                                              np.expand_dims(thr_bbox, 0))
            pck_results[pck_thr].append(pck)
    mPCK = 0
    info_str = []
    for pck_thr in PCK_threshold_list:
        info_str.append(
            ['PCK@' + str(pck_thr), np.mean(pck_results[pck_thr])]
        )
        mPCK += np.mean(pck_results[pck_thr])
    info_str.append(['mPCK', mPCK / len(PCK_threshold_list)])

    name_value = OrderedDict(info_str)
    keys = list(name_value.keys())

    path = str(output_dir / f'test_pck_rank_{rank}.pkl')
    with open(path, 'wb') as fid:
        pk.dump(name_value, fid, pk.HIGHEST_PROTOCOL)

    return keys


def integrate_results(metric_keys,
                      world_size: int,
                      output_dir: Path,
                      model_name: str) -> None:
    while True:
        ready = True
        for r in range(world_size):
            path = output_dir / f'test_pck_rank_{r}.pkl'
            if not path.exists():
                ready = False
        if ready:
            break
        else:
            time.sleep(20)
    # sleep 30s to make sure all files are saved
    time.sleep(20)
    all_pck_results = OrderedDict()
    for key in metric_keys:
        all_pck_results[key] = []
    for r in range(world_size):
        path = output_dir / f'test_pck_rank_{r}.pkl'
        with open(str(path), 'rb') as fid:
            pck_results = pk.load(fid)

        for key in metric_keys:
            all_pck_results[key].append(pck_results[key])

    print('\n')
    for k, v in sorted(all_pck_results.items()):
        print(f'{k}: {np.mean(v)}')

    # save testing log
    test_log = str(output_dir / "test_pck_result.txt")
    with open(test_log, 'a') as f:
        f.write(f"Model: {model_name}")
        for k, v in sorted(all_pck_results.items()):
            f.write(f'\t {k}: {np.mean(v)}'+'\n')
        f.write(
            "********************************************************************\n"
        )
