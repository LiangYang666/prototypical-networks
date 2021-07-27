#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :too2_splitTrainTest.py
# @Time      :2021/7/11 下午4:52
# @Author    :Yangliang
import os
import pandas as pd
import random

tempDir = '/media/D_4TB/YL_4TB/BaoDetection/data/Chanel/ClassificationFilter/sign'

if __name__ == "__main__":
    random.seed(0)
    partName = os.path.basename(tempDir)
    ratio = 0.7
    files_1 = os.listdir(os.path.join(tempDir, partName+'_1'))
    files_1 = [os.path.join(partName+'_1', x) for x in files_1]
    files_2 = os.listdir(os.path.join(tempDir, partName+'_2'))
    files_2 = [os.path.join(partName+'_2', x) for x in files_2]

    random.shuffle(files_1)
    random.shuffle(files_2)
    train_1 = pd.DataFrame({'filename': files_1[:int(len(files_1)*ratio)], 'label': 1})
    val_1 = pd.DataFrame({'filename': files_1[int(len(files_1)*ratio):], 'label': 1})

    train_2 = pd.DataFrame({'filename': files_2[:int(len(files_2)*ratio)], 'label': 2})
    val_2 = pd.DataFrame({'filename': files_2[int(len(files_2)*ratio):], 'label': 2})

    train = pd.concat([train_1, train_2])
    val = pd.concat([val_1, val_2])

    train.to_csv(os.path.join(tempDir, 'train.csv'), index=False)
    val.to_csv(os.path.join(tempDir, 'val.csv'), index=False)






