# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# Usage: python ana.py input_img data_img
from os import listdir
from os.path import isfile, isdir, join
import sys
import cv2
import numpy as np
import imutils
from ana2 import *

mypath = "./data/"
files = listdir(mypath)
path = sys.argv[1]
dis_l = []
vis_l = []

for f in files:
    data_img = cv2.imread(f)
    (dis, vis) = PIC_ANA(path , f)
    if len(dis_l) <= 10:
        dis_l.append(dis)
        vis_l.append(vis)
    else:
        for i in range(0, 9):
            if dis > dis_l[i]:
                dis_l[i] = dis
                vis_l[i] = vis
temp = 0.0

for i in range(0,len(dis_l)-1):
    if i+1 < len(dis_l)-1:
        for j in range(0,len(dis_l)-1-i):
            if dis_l[j] > dis_l[j+1]:
                temp = dis_l[j+1]
                dis_l[j+1] = dis_l[j]
                dis_l[j] = temp
                tempv = vis_l[j+1].shape
                vis_l[j+1] = vis_l[j]
                vis_l[j] = tempv
                
for i in range(0,len(dis_l)-1):
    print (dis_l[i])
    outpath = "./Output/" + i + "jpg"
    cv2.imwrite(outpath, vis_l[i])
