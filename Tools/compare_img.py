import time
import os
import numpy as np
import cv2
from tqdm import *


output_path = './gt'
output2_path = './det'
write_path = './out'

def create_folder(folder):
    """ Create a folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


def pic_stitch(imgA, imgB, f):
    """
        合成图片A、B
    """
    img_array_A = cv2.imread(imgA)
    img_array_B = cv2.imread(imgB)
    img_array_AB = np.hstack((img_array_A, img_array_B))
    output_img_path = os.path.join(write_path, "{}".format(f))
    cv2.imwrite(output_img_path, img_array_AB)


create_folder(write_path)
filesName = os.listdir(output_path)
for f in tqdm(filesName):
  output_img_path = os.path.join(output_path, f)
  output2_img_path = os.path.join(output2_path,f)
  pic_stitch(output_img_path, output2_img_path, f)
