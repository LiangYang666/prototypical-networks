#!/usr/bin/env bash

python train.py \
--arch resnet50 \
--epochs 5000 \
--pretrained \
--weight-decay 0.00001 \
--print-freq 20 \
--lr 0.001 \
--optimizer 'adam' \
--gamma 0.5 \
--alpha 0.5 \
--step_size 30 \
--workers 24 \
--subtract_mean 0.485 0.456 0.406 \
--subtract_std 0.229 0.224 0.225 \
--image_size 224 \
--n_query_train 100 \
--n_query_val 100 \
--n_support 100 \
--n_way_train 2 \
--n_way_val 2 \
--n_episodes_train 80 \
--n_episodes_val 80 \
--train /media/D_4TB/YL_4TB/BaoDetection/data/Chanel/ClassificationFilter/sign/train.csv \
--val /media/D_4TB/YL_4TB/BaoDetection/data/Chanel/ClassificationFilter/sign/val.csv \
--model_name R50_fc512_euc_1 \
--out_dim 512
