#!/usr/bin/env bash

python train.py \
--arch resnet50 \
--epochs 500 \
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
--image_size 124 \
--n_query_train 5 \
--n_query_val 5 \
--n_support 5 \
--n_way_train 100 \
--n_way_val 20 \
--n_episodes_train 80 \
--n_episodes_val 80 \
--train_dir /media/D_4TB/YL_4TB/Competitions/ZNLSG_21_XinYe/data/cssjj/train/meta_learning/train_crop_images/all/ \
--val_dir /media/D_4TB/YL_4TB/Competitions/ZNLSG_21_XinYe/data/cssjj/train/meta_learning/train_crop_images/test/ \
--model_name 3ResNet50_w100_dataaug_fc512_cos \
--resume /media/D_4TB/YL_4TB/Competitions/ZNLSG_21_XinYe/data/cssjj/rundata/metalearning/models_trained/3ResNet50_w100_dataaug_fc512_cos/checkpoints/checkpoint_70.pt \
--out_dim 512
