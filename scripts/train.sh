#!/bin/bash

if [ -z $1 ]
then
    echo "No split passed"
else
    echo "Split = $1"
fi

split=$1

IDX=0,1,2,3,4,5,6,7

export PYTHONPATH=$PYTHONPATH:./

data_dir=/data/datasets/original

output_dir=./checkpoints/ckpts/mp100/llm/llama-3_1-8b/plain_llava_inst/${split}


if [ -d ${output_dir} ];then
    echo "dir already exists"
else
    mkdir -p ${output_dir}
fi

if [ -d ${output_dir}/src ];then
    echo "src dir already exists"
else
    echo "save codes to src"
    mkdir ${output_dir}/src
    cp -r datasets ${output_dir}/src
    cp -r models ${output_dir}/src
    cp -r utils ${output_dir}/src
    cp -r scripts ${output_dir}/src
fi

ckpt_dir=./checkpoints/model_weights/Meta-Llama-3.1-8B
vision_path=./checkpoints/model_weights/dinov2_vitl14_pretrain.pth

CUDA_VISIBLE_DEVICES=$IDX OMP_NUM_THREADS=1 torchrun --nnodes=1 --nproc_per_node=8 --master_port=25007 \
    utils/train.py \
    --llm_path ${ckpt_dir} \
    --data_path ${data_dir}/mp100/annotations/mp100_${split}_train.json \
    --image_folder ${data_dir}/mp100/images \
    --vision_path ${vision_path} \
    --image_size 224 \
    --crop_size 224 \
    --conv_format cape \
    --data_augmentation True \
    --tune_mm_mlp_adapter True \
    --freeze_llm False \
    --lora_llm_enable True \
    --lora_llm_r 8 \
    --lora_llm_alpha 16 \
    --lora_llm_dropout 0.05 \
    --freeze_vit False \
    --lora_vision_enable True \
    --lora_vision_r 8 \
    --lora_vision_alpha 16 \
    --lora_vision_dropout 0.05 \
    --bf16 True \
    --output_dir ${output_dir} \
    --num_train_epochs 12 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --eval_strategy "no" \
    --save_strategy "steps" \
    --save_steps 500000 \
    --save_total_limit 1 \
    --learning_rate 5e-4 \
    --weight_decay 0.01 \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --dataloader_num_workers 4 \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing False \
    --seed 42 \
    2>&1 | tee ${output_dir}/log.txt

output_eval_dir=${output_dir}/eval
if [ -d ${output_eval_dir} ];then
    echo "dir already exists"
else
    mkdir ${output_eval_dir}
fi

CUDA_VISIBLE_DEVICES=$IDX OMP_NUM_THREADS=1 torchrun --nnodes=1 --nproc_per_node=8 --master_port=25007 \
    utils/valid_llava_inst.py \
    --model-name ${output_dir} \
    --question-file ${data_dir}/mp100/annotations/mp100_${split}_test.json \
    --image-folder ${data_dir}/mp100/images \
    --output-dir ${output_eval_dir} \
    --nkg 15 \
    2>&1 | tee ${output_eval_dir}/eval.txt