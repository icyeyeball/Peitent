# -*- coding: utf-8 -*-
import cv2
import numpy

src = cv2.imread('1111.png')
mask = cv2.imread('2222.png')
src = cv2.resize(src,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
mask = cv2.resize(mask,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
save = numpy.zeros(src.shape, numpy.uint8) #创建一张空图像用于保存

for row in range(src.shape[0]):
    for col in range(src.shape[1]):
        for channel in range(src.shape[2]):
            if mask[row, col, channel] == 0:
                val = 0
            else:
                reverse_val = 255 - src[row, col, channel]
                val = 255 - reverse_val * 256 / mask[row, col, channel]
                if val < 0: val = 0
            save[row, col, channel] = val

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('save', save)
cv2.waitKey(0)
cv2.destroyAllWindows()