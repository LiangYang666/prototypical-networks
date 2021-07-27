#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :tool1_divide_data.py
# @Time      :2021/7/11 下午4:08
# @Author    :Yangliang
import sys
import os
import shutil
from tqdm import tqdm
sys.path.append('.')

dataDir = '/media/D_4TB/YL_4TB/BaoDetection/data/Burberry/ClassificationFilter'
def checkDirsAndCreate(paths):
    if isinstance(paths, str):
        paths = [paths]
    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)
            print(f'Created {path} !')



if __name__ == "__main__":
    for subDir in os.listdir(dataDir):
        subDir = os.path.join(dataDir, subDir)
        subDir1 = os.path.join(dataDir, subDir+'_1')
        subDir2 = os.path.join(dataDir, subDir+'_2')
        checkDirsAndCreate([subDir1, subDir2])
        for imgFile in tqdm(os.listdir(subDir)):
            src = os.path.join(subDir, imgFile)
            temp = imgFile.split('-', 2)[1]     # 1 or 2
            if temp == '1':
                dst = os.path.join(subDir1, imgFile)
            elif temp == '2':
                dst = os.path.join(subDir2, imgFile)
            else:
                print('File name error')
            shutil.move(src, dst)
        shutil.move(subDir1, subDir)
        shutil.move(subDir2, subDir)





