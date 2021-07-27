#!/usr/bin/env bash

python test.py \
--gpu 1 \
--arch resnet50 \
--workers 24 \
--batch_size 64 \
--subtract_mean 156.2336961908687 122.03200584422879 109.9825961313363 \
--subtract_std 46.39668432 42.3512562 41.54967605 \
--image_size 224 \
--train /media/D_4TB/YL_4TB/BaoDetection/data/Chanel/ClassificationFilter/sign/train.csv \
--test /media/D_4TB/YL_4TB/BaoDetection/data/Chanel/ClassificationFilter/sign/val.csv \
--checkpoint '/media/D_4TB/YL_4TB/BaoDetection/data/Chanel/ClassificationFilter/sign/R50_fc512_euc/checkpoints/checkpoint_500.pt' \
--evaluation_name 'Resnet50_evaluation' \
--results_name 'testing' \
--save_prototypes \
--out_dim 512
