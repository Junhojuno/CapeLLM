#!/bin/bash

if [ -z $1 ]
then
    echo "No split passed"
else
    echo "Split = $1"
fi

split=$1

IDX=0,1,2,3

export PYTHONPATH=$PYTHONPATH:./

data_dir=/data/datasets/original

output_dir=./checkpoints/ckpts/mp100/llm/llama-3_1-8b/plain_llava_inst/${split}

output_eval_dir=${output_dir}/eval_again
if [ -d ${output_eval_dir} ];then
    echo "dir already exists"
else
    mkdir ${output_eval_dir}
fi

CUDA_VISIBLE_DEVICES=$IDX OMP_NUM_THREADS=1 torchrun --nnodes=1 --nproc_per_node=4 --master_port=25007 \
    utils/valid.py \
    --model-name ${output_dir} \
    --question-file ${data_dir}/mp100/annotations/mp100_${split}_test.json \
    --image-folder ${data_dir}/mp100/images \
    --output-dir ${output_eval_dir} \
    --nkg 15 \
    2>&1 | tee ${output_eval_dir}/eval.txt