# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190908
############################
# python _googles.py input

import sys
import pygame
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import math
import imutils

def getMatchNum(matches,ratio):
    '''返回特征点匹配数量和匹配掩码'''
    matchesMask=[[0,0] for i in range(len(matches))]
    matchNum=0
    for i,(m,n) in enumerate(matches):
        if m.distance<ratio*n.distance: #将距离比率小于ratio的匹配点删选出来
            matchesMask[i]=[1,0]
            matchNum+=1
    return (matchNum,matchesMask)
    
pygame.init()

sift = cv2.xfeatures2d.SIFT_create() 
#创建FLANN匹配对象
FLANN_INDEX_KDTREE=0
indexParams=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
searchParams=dict(checks=50)
flann=cv2.FlannBasedMatcher(indexParams,searchParams)

text1 = sys.argv[1]
text2 = sys.argv[2]

font = pygame.font.Font("Fonts/LiHei ProPC.ttf", 200)

ftext1 = font.render(text1, True, (0, 0, 0),(255, 255, 255))
ftext2 = font.render(text2, True, (0, 0, 0),(255, 255, 255))

pygame.image.save(ftext1, "./pic/1.jpg")#圖片儲存地址
pygame.image.save(ftext2, "./pic/2.jpg")#圖片儲存地址



sampleImage=cv2.imread("./pic/1.jpg",0)
queryImage=cv2.imread("./pic/2.jpg",0)
kp1, des1 = sift.detectAndCompute(sampleImage, None) #提取样本图片的特征
kp2, des2 = sift.detectAndCompute(queryImage, None) #提取比对图片的特征
matches=flann.knnMatch(des1,des2,k=2) #匹配特征点，为了删选匹配点，指定k为2，这样对样本图的每个特征点，返回两个匹配
(matchNum,matchesMask)=getMatchNum(matches,0.9) #通过比率条件，计算出匹配程度
matchRatio=matchNum*100/len(matches)
drawParams=dict(matchColor=(0,255,0),  singlePointColor=(0,0,255), matchesMask=matchesMask, flags=0)

sampleImage=cv2.imread("./pic/1.jpg")
queryImage=cv2.imread("./pic/2.jpg")
comparisonImage=cv2.drawMatchesKnn(sampleImage,kp1,queryImage,kp2,matches,None,**drawParams)

print ("相似度: " + str(matchRatio))
cv2.imwrite("./pic/comp.jpg", comparisonImage)


