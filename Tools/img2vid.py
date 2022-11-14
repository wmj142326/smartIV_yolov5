# -*- coding = utf-8 -*-
# @time:2021/3/3 10:46
# Author:wmj
# @File:pic2vid.py
# @Software:PyCharm
# @Function:将图片合成视频

import cv2
import os

# 确定图片和视频的存放路径
pic_path = 'img/'
vid_path = 'vid/'

# 视频输出参数
vid_fps = 25
vid_name = 'out3.mp4'

if not os.path.exists(vid_path):
    os.makedirs('vid')

dir_path_list = os.listdir(pic_path)

# img_new_sort = dir_path_list  # 方式一：乱序
# img_new_sort = dir_path_list.sort()  # 方式二：错误排序
img_new_sort = dir_path_list.sort(key=lambda i: int(i.split('.')[0]))  # 方式三：正确排序

pic_num = len(dir_path_list)

# 获取一张图片的宽高作为视频的宽高
first_pic = pic_path + dir_path_list[0]
image = cv2.imread(first_pic)
image_info = image.shape
height = image_info[0]
width = image_info[1]
size = (height, width)
print('vid_name: ', vid_name)
print('out_size: ', size)

# 确定视频参数
fps = vid_fps
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(vid_path + vid_name,
                        fourcc,
                        fps,
                        (width, height))

"""
参数1 即将保存的文件路径
参数2 VideoWriter_fourcc为视频编解码器
    fourcc意为四字符代码（Four-Character Codes），顾名思义，该编码由四个字符组成,下面是VideoWriter_fourcc对象一些常用的参数,注意：字符顺序不能弄混
    cv2.VideoWriter_fourcc('I', '4', '2', '0'),该参数是YUV编码类型，文件名后缀为.avi
    cv2.VideoWriter_fourcc('P', 'I', 'M', 'I'),该参数是MPEG-1编码类型，文件名后缀为.avi
    cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),该参数是MPEG-4编码类型，文件名后缀为.avi
    cv2.VideoWriter_fourcc('T', 'H', 'E', 'O'),该参数是Ogg Vorbis,文件名后缀为.ogv
    cv2.VideoWriter_fourcc('F', 'L', 'V', '1'),该参数是Flash视频，文件名后缀为.flv
    cv2.VideoWriter_fourcc('m', 'p', '4', 'v')    文件名后缀为.mp4
参数3 为帧播放速率
参数4 (width,height)为视频帧大小
"""
num = 0
for pic in dir_path_list:
    print(' ', pic)
    file_name = os.path.join(pic_path, pic)
    image = cv2.imread(file_name)
    video.write(image)
    num += 1
    print("\r" + "完成进度: %d / %d" % (num, pic_num), end="")

print("已完成")
