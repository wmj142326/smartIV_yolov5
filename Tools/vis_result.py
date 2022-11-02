import json
import os
import cv2
from tqdm import *
import numpy as np
from enum import Enum

import shutil


def create_folder(folder):
    """ Create a folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


img_file_path = "../../yolov5/task1/"
json_file_path = "../../yolov5/task1_result/smartIV/"
output_path = "output/"
filesName = os.listdir(img_file_path)

create_folder(output_path)
shutil.rmtree(output_path)
create_folder(output_path)

for f in tqdm(filesName):
    bbox_list = []
    score_list = []
    img = cv2.imread(os.path.join(img_file_path, f))
    f = f.split('.')[0]
    output_result = output_path + f + ".jpg"
    json_path = json_file_path + f + ".json"
    with open(json_path, "rb") as fd:
        annots = json.load(fd)
        annot = annots["annotations"]
        for i in range(len(annot)):
            bbox = annot[i]["bbox"]
            score = annot[i]["score"]
            bbox_list.append(bbox)
            score_list.append(score)
        for j, coordinate in enumerate(bbox_list):
            x, y, w, h = coordinate
            score_int = round(score_list[j], 2)
            cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (0, 255, 0), 1)
            cv2.putText(img, str(score_int), (int(x - w / 2), int(y - h / 2) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.35,
                        (0, 255, 0), 1)
        cv2.imwrite(output_result, img)
