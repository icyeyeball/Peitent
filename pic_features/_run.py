# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
#
from os import listdir
from os.path import isfile, isdir, join
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
import sys
import imutils

def getMatchNum(matches,ratio):
    '''number of matched features and relation'''
    matchesMask=[[0,0] for i in range(len(matches))]
    matchNum=0
    for i,(m,n) in enumerate(matches):
        if m.distance<ratio*n.distance: #select the distance > ratio
            matchesMask[i]=[1,0]
            matchNum+=1
    return (matchNum,matchesMask)

queryPath='./data/' #path of database
files = listdir(queryPath)
samplePath=sys.argv[1] #input sample
#sift extractpr
sift = cv2.xfeatures2d.SIFT_create() 
#FLANN matching
FLANN_INDEX_KDTREE=0
indexParams=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
searchParams=dict(checks=50)
flann=cv2.FlannBasedMatcher(indexParams,searchParams)

ratio_l=[]
vis_l=[]

sampleImage=cv2.imread(samplePath,0)
#sampleImage = imutils.resize(sampleImage, width = 200)
kp1, des1 = sift.detectAndCompute(sampleImage, None) #提取样本图片的特征+
print (len(files))
for f in files:
    f=queryPath+f
    print (str(f))
    queryImage=cv2.imread(f,0)
    #queryImage = imutils.resize(queryImage, width = 200)
    kp2, des2 = sift.detectAndCompute(queryImage, None) #提取比对图片的特征
    matches=flann.knnMatch(des1,des2,k=2) #匹配特征点，为了删选匹配点，指定k为2，这样对样本图的每个特征点，返回两个匹配
    (matchNum,matchesMask)=getMatchNum(matches,0.9) #通过比率条件，计算出匹配程度
    matchRatio=matchNum*100/len(matches)
    drawParams=dict(matchColor=(0,255,0),  singlePointColor=(0,0,255), matchesMask=matchesMask, flags=0)

    sampleImage=cv2.imread(samplePath)
    queryImage=cv2.imread(f)
    #(hA, wA) =sampleImage.shape[:2]  
    #(hB, wB) = queryImage.shape[:2]
    comparisonImage=cv2.drawMatchesKnn(sampleImage,kp1,queryImage,kp2,matches,None,**drawParams)
    #cv2.putText(comparisonImage,str(matchRatio) + "%",(int(wA+wB/2.),int(3.*hB/4.)),cv2.FONT_HERSHEY_PLAIN,int(1.*hB/50.),(0,0,255),4)
    ratio_l.append(matchRatio)
        
    vis_l.append(comparisonImage)
    
    for i in range(0,len(ratio_l)-1): 
        for j in range(0,len(ratio_l)-1-i): 
            if ratio_l[j] < ratio_l[j+1]: 
                tmp = ratio_l[j]
                ratio_l[j] = ratio_l[j+1]
                ratio_l[j+1] = tmp
                tmpv = vis_l[j]
                vis_l[j] = vis_l[j+1]
                vis_l[j+1] = tmpv
    if len(ratio_l) > 50:
        del ratio_l[50]
        del vis_l[50]

for k in range(0,len(ratio_l)):
    outpath = "./Output/" + str(k+1) + ".jpg"
    print ("===========================")
    print (str(ratio_l[k]) + "% 相似度" )
    print (outpath)
    cv2.imwrite(outpath, vis_l[k])

    
"""
column=4
row=5
#绘图显示
figure,ax=plt.subplots(row,column)

for index in range(0,20):
    ax[int(index/column)][index%column].set_title('Similiarity %.2f%%' % ratio_l[index])
    ax[int(index/column)][index%column].imshow(vis_l[index])
plt.show()
"""
