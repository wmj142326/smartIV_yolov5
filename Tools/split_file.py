# -*- coding: utf-8 -*-
# @Time : 2022/10/25
# @Author : wmj
# @Email : wmj142326@163.com
# @File : split_file.py
# @Note : 数据集划分
# ---------------------------
import os
import random
import shutil
import numpy as np


def create_folder(folder):
    """ Create a folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


def clear_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)


def main():
    image_list = os.listdir(image_path)
    label_list = os.listdir(label_path)
    random.shuffle(image_list)
    random.shuffle(label_list)
    img_num = len(image_list)

    sum_ration = np.sum([rate[0], rate[1], rate[2]])
    train_num = int(rate[0] * img_num // sum_ration)
    val_num = int(rate[1] * img_num // sum_ration)
    test_num = int(rate[2] * img_num // sum_ration)

    train_list = image_list[:train_num]
    for image in train_list:
        label = image.replace('jpg', 'txt')
        shutil.copy(create_folder(os.path.join(image_path, image)),
                    create_folder(os.path.join(rank_0, rank_1[0], rank_2[0])))
        shutil.copy(create_folder(os.path.join(label_path, label)),
                    create_folder(os.path.join(rank_0, rank_1[0], rank_2[1])))
    print('train', train_num)

    val_list = image_list[train_num:(train_num + val_num)]
    for image in val_list:
        label = image.replace('jpg', 'txt')
        shutil.copy(create_folder(os.path.join(image_path, image)),
                    create_folder(os.path.join(rank_0, rank_1[1], rank_2[0])))
        shutil.copy(create_folder(os.path.join(label_path, label)),
                    create_folder(os.path.join(rank_0, rank_1[1], rank_2[1])))
    print('val', val_num)

    test_list = image_list[(train_num + val_num):]
    for image in test_list:
        label = image.replace('jpg', 'txt')
        shutil.copy(create_folder(os.path.join(image_path, image)),
                    create_folder(os.path.join(rank_0, rank_1[2], rank_2[0])))
        shutil.copy(create_folder(os.path.join(label_path, label)),
                    create_folder(os.path.join(rank_0, rank_1[2], rank_2[1])))
    print('test', test_num)


if __name__ == "__main__":
    image_path = 'images'
    label_path = 'labels'
    rank_0 = 'dataset'
    rank_1 = ['train', 'valid', 'test']
    rank_2 = ['images', 'labels']
    rate = [8, 2, 0]
    clear_folder(rank_0)
    main()
    print("finished!")
