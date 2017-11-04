#coding=utf-8
from skimage import io,data
import matplotlib.pyplot as plt
from HuffmanCoding import *
from evaluator import *

#HuffmanCoding
img = io.imread('Image/Source/Gray/Image01.jpg')
#Encoder
encodedImg = HuffmanEncoder(img)
io.imshow(encodedImg)
plt.show()
io.imsave("Image/Result/HuffmanEncodedImg.jpg", encodedImg)
#Decoder
decodedImg = HuffmanDecoder(encodedImg)
io.imshow(decodedImg)
plt.show()
io.imsave("Image/Result/HuffmanDecodedImg.jpg", decodedImg)

print "Compression Rate: " + compressionRate(img, decodedImg)
print "SNR: " + SNR(img, decodedImg)