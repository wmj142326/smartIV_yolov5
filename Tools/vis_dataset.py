import json
import os
import cv2
import numpy as np
from tqdm import *
from enum import Enum
import shutil

def create_folder(folder):
    """ Create a folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

img_file_path = "/home/meijun/Projects/CIAC_project/Task1Dataset/dataset_3/valid/images"
json_file_path = "/home/meijun/Projects/CIAC_project/Task1Dataset/dataset_3/valid/label/"
output_path = "/home/meijun/Projects/CIAC_project/yolov5/Tools/gt/"
filesName = os.listdir(img_file_path)

create_folder(output_path)
shutil.rmtree(output_path)
create_folder(output_path)

category_tranlate = {"轿车": "car",
                     "SUV": "SUV",
                     'suv': 'suv',
                     "面包车": "van",
                     "成人": "dult",
                     "电动车/摩托车": "motorcycle",
                     "自行车": "bicycle",
                     "大客车": "bus",
                     "大货车": "Big_truck",
                     "电动三轮车/摩托三轮车": "Motor_tricycle",
                     "小货车": "small_van",
                     "微型车": "Mini_car",
                     "专业作业车": "Professional_operation_vehicle",
                     "儿童": "child",
                     "其他": "other",
                     "人力三轮车": "Human_tricycles",
                     "非机动车其他": "non_motor_vehicles_other",
                     "模糊或变形严重车辆": "Vehicle_with_blurring_or_severe_deformation",
                     'unknow': "unknow"
                     }


class Color(Enum):
    car = (0, 0, 255)
    van = (0, 255, 0)
    dult = (255, 0, 0)
    motorcycle = (255, 255, 0)
    bicycle = (0, 255, 255)
    bus = (255, 0, 255)
    Big_truck = (255, 255, 255)
    Motor_tricycle = (0, 0, 0)
    small_van = (255, 128, 0)
    Mini_car = (25, 25, 112)
    Professional_operation_vehicle = (153, 51, 250)
    child = (199, 97, 20)
    other = (160, 82, 45)
    Human_tricycles = (116, 0, 0)
    non_motor_vehicles_other = (255, 153, 18)
    SUV = (156, 102, 31)
    suv = (188, 108, 20)
    Vehicle_with_blurring_or_severe_deformation = (218, 122, 214)
    unknow = (222, 122, 214)


def is_str(x):
    return isinstance(x, str)


def color_val(color):
    if is_str(color):
        return Color[color].value
    else:
        raise TypeError(f'Invalid type for color: {type(color)}')


for f in tqdm(filesName):

    bbox_list = []
    category_list = []
    id_list = []
    img = cv2.imread(os.path.join(img_file_path, f))
    f = f.split('.')[0]
    output_path_result = output_path + f + ".jpg"
    json_path = json_file_path + f + ".json"
    with open(json_path, "rb") as fd:
        annots = json.load(fd)
        for i in range(len(annots)):
            id = annots[i]["id"]
            bbox = annots[i]["bbox"]
            category = annots[i]["category_name"]

            category = category_tranlate[category]

            id_list.append(id)
            bbox_list.append(bbox)
            category_list.append(category)

            # x,y,w,h
        for j, coordinate in enumerate(bbox_list):
            x, y, w, h = coordinate
            category = category_list[j]
            color = color_val(category)
            cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), color, 1)

            cv2.putText(img, id_list[j] + ":" + category_list[j], (int(x - w / 2), int(y - h / 2) - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, color, 1)

        cv2.imwrite(output_path_result, img)
