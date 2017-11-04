#coding=utf-8
import numpy as np
from skimage import io,data
from skimage.color import *

def FS(img):
    wid = img.shape[0]
    hei = img.shape[1]
    img_out = img
    #将已经归一化到[0,1]之间的像素值还原到[0,255]
    for y in range(0, wid - 1):
        for x in range(0, hei - 1):
            img_out[y, x] = img_out[y, x] * 255
    #进行误差的计算以及误差传播
    for y in range(2, wid - 2):
        for x in range(0, hei - 2):
            th = (x + y) / 2
            oldpixel = img_out[y, x]
            newpixel = 255 * (oldpixel > th)
            quant_error = oldpixel - newpixel
            #原位置的像素值保持
            img_out[y, x] = newpixel
            #将误差按比例传播到右方、左下、右方、右下
            # img_out[y + 1, x] = img_out[y + 1, x] + 7.0 * quant_error / 16.0
            # img_out[y - 1, x + 1] = img_out[y - 1, x + 1] + 3.0 * quant_error / 16.0
            # img_out[y, x + 1] = img_out[y, x + 1] + 5.0 * quant_error / 16.0
            # img_out[y + 1, x + 1] = img_out[y + 1, x + 1] + 1.0 * quant_error / 16.0
            img_out[y + 1, x] = img_out[y + 1, x] + 7.0 * quant_error / 48.0
            img_out[y + 2, x] = img_out[y + 2, x] + 5.0 * quant_error / 48.0
            img_out[y - 2, x + 1] = img_out[y - 2, x + 1] + 3.0 * quant_error / 48.0
            img_out[y - 1, x + 1] = img_out[y - 1, x + 1] + 5.0 * quant_error / 48.0
            img_out[y, x + 1] = img_out[y, x + 1] + 7.0 * quant_error / 48.0
            img_out[y + 1, x + 1] = img_out[y + 1, x + 1] + 5.0 * quant_error / 48.0
            img_out[y + 2, x + 1] = img_out[y + 2, x + 1] + 3.0 * quant_error / 48.0
            img_out[y - 2, x + 2] = img_out[y - 2, x + 2] + 1.0 * quant_error / 48.0
            img_out[y - 1, x + 2] = img_out[y - 1, x + 2] + 3.0 * quant_error / 48.0
            img_out[y, x + 2] = img_out[y, x + 2] + 5.0 * quant_error / 48.0
            img_out[y + 1, x + 2] = img_out[y + 1, x + 2] + 3.0 * quant_error / 48.0
            img_out[y + 2, x + 2] = img_out[y + 2, x + 2] + 1.0 * quant_error / 48.0
    #使像素值归一化到[0,1]
    for y in range(0, wid - 1):
        for x in range(0, hei -1):
            if img_out[y, x] < 0.0:
                img_out[y, x] = (-1) * img_out[y, x]
            img_out[y, x] = img_out[y, x] / 255.0
            if img_out[y, x] > 1.0:
                img_out[y, x] = 1.0
    return img_out
