# coding = utf8
import os

import numpy as np

os.path.abspath("..")
"""
    @Project:PycharmProjects
    @File:depth2Visible.py
    @Author:十二点前要睡觉
    @Date:2021/12/29 17:18
"""
import cv2
import os.path
import glob
from PIL import Image


def convertPNG2RGB(pngfile, outdir):
    # Depth to RGB
    # 读取16位深度图（像素范围0～65535），并将其转化为8位（像素范围0～255）
    uint16_img = cv2.imread(pngfile, -1)  # 在cv2.imread参数中加入-1，表示不改变读取图像的类型直接读取，否则默认的读取类型为8位。
    uint16_img -= uint16_img.min()
    uint16_img = uint16_img / (uint16_img.max() - uint16_img.min())
    uint16_img *= 255
    # 使得越近的地方深度值越大，越远的地方深度值越小，以达到伪彩色图近蓝远红的目的。
    uint16_img = 255 - uint16_img

    # cv2 中的色度图有十几种，其中最常用的是 cv2.COLORMAP_JET，蓝色表示较高的深度值，红色表示较低的深度值。
    # cv.convertScaleAbs() 函数中的 alpha 的大小与深度图中的有效距离有关，如果像我一样默认深度图中的所有深度值都在有效距离内，并已经手动将16位深度转化为了8位深度，则 alpha 可以设为1。
    im_color = cv2.applyColorMap(cv2.convertScaleAbs(uint16_img, alpha=1), cv2.COLORMAP_JET)
    # convert to mat png
    im = Image.fromarray(im_color)
    im.save(os.path.join(outdir, os.path.basename(pngfile)))


def convertPNG2Gray(pngfile, outdir):
    # Depth to 灰度
    uint8_img = cv2.imread(pngfile)
    uint16_img = cv2.imread(pngfile, -1)
    uint16_img -= uint16_img.min()
    uint16_img = uint16_img / (uint16_img.max() - uint16_img.min())
    uint16_img *= 255
    new_uint16_img = uint16_img.astype(np.uint8)

    im = Image.fromarray(new_uint16_img)
    im.save(os.path.join(outdir, os.path.basename(pngfile)))


if __name__ == '__main__':
    for pngfile in glob.glob("./*.png"):  # C:/Users/BAMBOO/Desktop/source pics/rgbd_6/depth/*.png
        convertPNG2RGB(pngfile, "./transformerRGB/")  # C:/Users/BAMBOO/Desktop/source pics/rgbd_6/color
        convertPNG2Gray(pngfile, "./transformerGray/")  # C:/Users/BAMBOO/Desktop/source pics/rgbd_6/color
