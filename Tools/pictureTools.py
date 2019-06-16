#!/usr/local/bin/ python3
# coding: utf-8
from math import *
import cv2
import os
from PIL import Image
import numpy as np


# 图片的旋转、曝光、缩放
class PictureProcessing():

    def __init__(self, old_image, new_image):
        self.img = old_image
        self.res = new_image

    # 模糊
    def blur(self):
        img = cv2.imread(self.img)
        res_img = cv2.GaussianBlur(img, ksize=(39, 39), sigmaX=0, sigmaY=0)
        # print(type(res_img_))
        cv2.imwrite(self.res, res_img)

    # 旋转
    def rotate(self):
        img = cv2.imread(self.img)
        height, width = img.shape[:2]
        degree = 20
        # 旋转后的尺寸
        heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
        widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
        matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
        matRotation[0, 2] += (widthNew - width) / 2  # 重点在这步，目前不懂为什么加这步
        matRotation[1, 2] += (heightNew - height) / 2  # 重点在这步
        res_img = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))
        cv2.imwrite(self.res, res_img)

    # 曝光
    def exposure(self, c=1.5, b=66):  # 亮度就是每个像素所有通道都加上b
        img = cv2.imread(self.img)
        rows, cols, chunnel = img.shape
        blank = np.zeros([rows, cols, chunnel], img.dtype)  # np.zeros(img1.shape, dtype=uint8)
        dst = cv2.addWeighted(img, c, blank, 1 - c, b)
        cv2.imwrite(self.res, dst)


def old_file_exists():
    g = os.walk(os.path.dirname(os.path.abspath(__file__)))
    # print(os.path.dirname(__file__))
    for c, d, filelist in g:
        for filename in filelist:
            if filename.endswith('jpg') or filename.endswith("png"):
                # print("图片绝对路径" + os.path.join(c, filename))
                # print(c)
                # print(filename)
                return filename


if __name__ == '__main__':
    print("欢迎使用图片编辑工具")
    while True:
        path = os.path.abspath(__file__)
        # print(path)
        old_file = old_file_exists()
        # print(old_file)
        if old_file is None:
            print("请在%s目录下添加 .jpg或者 .png图片文件" % path)
            break
        res = int(input("请输入操作：1(模糊)  2(旋转)  3(曝光)   4(退出)"))
        if res >= 4:
            if res == 4:
                print("exit")
                break
            else:
                print("输入有误，请重新输入：")
                continue
        new_file_name = input("new_file_name：(包含文件后缀名)")
        picture = PictureProcessing(old_file, new_file_name)
        if res == 1:
            picture.blur()
            break
        elif res == 2:
            picture.rotate()
            break
        elif res == 3:
            picture.exposure()
            break
