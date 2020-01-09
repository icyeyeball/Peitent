# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# Usage: python gray.py input_img
import sys
import cv2
import numpy as np


path = sys.argv[1]
outpath = path[0:-4] + "-gray" + path[-4:-1] + path[-1]

image = cv2.imread(path)

image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_CUBIC)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (1, 1), 0)

ret,th1 = cv2.threshold(blurred,220,255,cv2.THRESH_BINARY)

#canny = cv2.Canny(blurred, 30, 150)

result = np.hstack([gray, blurred, th1])




cv2.imshow("Result:", result)

cv2.waitKey(0)
cv2.imwrite(outpath, result)
