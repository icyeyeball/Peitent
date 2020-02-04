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
    '''Return matched features and mateched subnet mask'''
    matchesMask=[[0,0] for i in range(len(matches))]
    matchNum=0
    for i,(m,n) in enumerate(matches):
        if m.distance<ratio*n.distance: #Select the features of matched point < ratio
            matchesMask[i]=[1,0]
            matchNum+=1
    return (matchNum,matchesMask)


def pic(word1, word2):
    pygame.init()

    sift = cv2.xfeatures2d.SIFT_create() 
    #Create FLANN matched object
    FLANN_INDEX_KDTREE=0
    indexParams=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
    searchParams=dict(checks=50)
    flann=cv2.FlannBasedMatcher(indexParams,searchParams)

    text1 = word1
    text2 = word2

    font = pygame.font.Font("Fonts/LiHei_ProPC.ttf", 50)

    ftext1 = font.render(text1, True, (0, 0, 0),(255, 255, 255))
    ftext2 = font.render(text2, True, (0, 0, 0),(255, 255, 255))

    pygame.image.save(ftext1, "./pic/1.jpg")#圖片儲存地址
    pygame.image.save(ftext2, "./pic/2.jpg")#圖片儲存地址

    sampleImage=cv2.imread("./pic/1.jpg",0)
    queryImage=cv2.imread("./pic/2.jpg",0)
    kp1, des1 = sift.detectAndCompute(sampleImage, None) #Extract the features of this picture
    kp2, des2 = sift.detectAndCompute(queryImage, None) #Extract the features of another picture
    try:
        matches=flann.knnMatch(des1,des2,k=2) #matched points，to select them，assign k = 2，that will return 2 matched points for each feature of this picture
    except:
        return 0.
    else:        
        (matchNum,matchesMask)=getMatchNum(matches,0.9) #zdepends on ratio to caculate how match
        matchRatio1=matchNum*100/len(matches)
        
    try:
        matches=flann.knnMatch(des2,des1,k=2) #matched points，to select them，assign k = 2，that will return 2 matched points for each feature of this picture
    except:
        return 0.
    else:        
        (matchNum,matchesMask)=getMatchNum(matches,0.9) #zdepends on ratio to caculate how match
        matchRatio2=matchNum*100/len(matches)

        matchRatio = (matchRatio1 + matchRatio2)/2.

        drawParams=dict(matchColor=(0,255,0),  singlePointColor=(0,0,255), matchesMask=matchesMask, flags=0)

        sampleImage=cv2.imread("./pic/1.jpg")
        queryImage=cv2.imread("./pic/2.jpg")
        comparisonImage=cv2.drawMatchesKnn(sampleImage,kp1,queryImage,kp2,matches,None,**drawParams)

        print ("相似度: " + str(matchRatio) + "%")
        cv2.imwrite("./pic/comp.jpg", comparisonImage)
        return matchRatio

if __name__=="__main__":
    pic(sys.argv[1],sys.argv[2])
