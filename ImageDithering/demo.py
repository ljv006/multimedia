#coding=utf-8
from skimage import io,data
from FSHalftoning import *
from numpy import *
import matplotlib.pyplot as plt
from orderDithering import *
from colorDithering import *
#8bits pictures
#img = io.imread('dlj.bmp')
#img = io.imread('Image01.jpg')
img = io.imread('Image02.jpg')
img_gray = rgb2gray(img)
# wid = img_grey.shape[0]
# hei = img_grey.shape[1]
# img_out = rgb2gray(img)
# io.imshow(img_out)
# plt.show()
# img_out = FS(img_out)
# max =  np.max(img_out)
# img_out = (img_out > 0.5) * 255
# img_out1 = orderDither(img_gray, 2)
# img_gray = rgb2gray(img)
# img_out2 = orderDither(img_gray, 4)
# io.imshow(img_out)
# plt.show()
#io.imsave("Image01Result.jpg", img_out)
# io.imsave("Image02Result.jpg", img_out)
# io.imsave("orderDither2.jpg", img_out1)
# io.imsave("orderDither4.jpg", img_out2)

#24bits pictures
#采用均等划分的调色板
# R = [0, 32, 64, 96, 128, 160, 192, 224, 255]
# G = [0, 32, 64, 96, 128, 160, 192, 224, 255]
# B = [0, 32, 64, 96, 128, 160, 192, 224, 255]
# LUT=[R, G, B]
# img_out3 = colorDither(img, LUT)
# io.imsave("colorDitherEquallyDivided.jpg", img_out3)
#采用中值划分的调色板
# img_out4 = colorDitherWithoutLUT(img)
# io.imsave("colorDitherMedianCut.jpg", img_out4)