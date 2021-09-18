# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# Usage: python run.py input_img
from os import listdir
from os.path import isfile, isdir, join
import sys
import cv2
import numpy as np
import imutils
from funcn import *

mypath = "./data/"
files = listdir(mypath)
path = sys.argv[1]
dis_l = []
vis_l = []

for f in files:
    (dis, vis, num) = PIC_ANA(path, mypath + f)
    dis_l.append(dis)
    vis_l.append(vis)
    for i in range(0,len(dis_l)-1): 
        for j in range(0,len(dis_l)-1-i): 
            if dis_l[j] > dis_l[j+1]: 
                tmp = dis_l[j]
                dis_l[j] = dis_l[j+1]
                dis_l[j+1] = tmp
                tmpv = vis_l[j]
                vis_l[j] = vis_l[j+1]
                vis_l[j+1] = tmpv
    if len(dis_l) > 10:
        del dis_l[10]
        del vis_l[10]
	           
for i in range(0,10):
    outpath = "./Output/" + str(i+1) + ".jpg"
    print ("===========================")
    print (dis_l[i])
    print (outpath)
    cv2.imwrite(outpath, vis_l[i])