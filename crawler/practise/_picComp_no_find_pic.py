# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
#
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
import imutils
import sys
import mysql.connector
import re
import shutil

def getMatchNum(matches,ratio):
    '''number of matched features and relation'''
    matchesMask=[[0,0] for i in range(len(matches))]
    matchNum=0
    for i,(m,n) in enumerate(matches):
        if m.distance<ratio*n.distance: #select the distance > ratio
            matchesMask[i]=[1,0]
            matchNum+=1
    return (matchNum,matchesMask)

tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()
cop = re.compile("[^.^/^A-Z^a-z^0-9^-]")
    
cmd_users = "SELECT imageData1 FROM tmarkTable WHERE goodsclassCode " + sys.argv[2]
cursor.execute(cmd_users)
tmark_list = cursor.fetchall()

files = []
for i in range(0, len(tmark_list)):
    #if len(cop.sub('', str(tmark_list[i]))) == 24:
    files.append(cop.sub('', str(tmark_list[i])))
    
samplePath = sys.argv[1] #input sample
#sift extractpr
sift = cv2.xfeatures2d.SIFT_create() 
#FLANN matching
FLANN_INDEX_KDTREE=0
indexParams=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
searchParams=dict(checks=50)
flann=cv2.FlannBasedMatcher(indexParams,searchParams)

ratio_l=[]
vis_l=[]

outputPath='./Output/' #path of database
tmpfiles = os.listdir(outputPath)
for f in tmpfiles:
    os.remove('./Output/'+str(f))

sampleImage=cv2.imread(samplePath,0)
sampleImage = imutils.resize(sampleImage, width = 500)
sampleImage = cv2.GaussianBlur(sampleImage, (5, 5), 0)
sampleImage = cv2.Canny(sampleImage, 30, 150)
kp1, des1 = sift.detectAndCompute(sampleImage, None) #detect the features of sample
for f in files:
    print(str(f))
    
    queryImage=cv2.imread(f,0)
    try:
        queryImage = imutils.resize(queryImage, width = 500)
    except AttributeError:
        continue
    else:
        queryImage = cv2.GaussianBlur(queryImage, (5, 5), 0)
        queryImage = cv2.Canny(queryImage, 30, 150)
        kp2, des2 = sift.detectAndCompute(queryImage, None) #detect the features of img in database
        try:
            matches=flann.knnMatch(des1,des2,k=2) #matched features, assign k=2 to return 2 matched features.
        except:
            continue
        else:
            (matchNum,matchesMask)=getMatchNum(matches,0.9) #set ratio = 0.9 to calculate the matching level
            matchRatio=matchNum*100/len(matches)
            drawParams=dict(matchColor=(0,255,0),  singlePointColor=(0,0,255), matchesMask=matchesMask, flags=0)
            sampleImage=cv2.imread(samplePath)
            queryImage=cv2.imread(f)
            sampleImage=cv2.imread(samplePath)
            sampleImage = imutils.resize(sampleImage, width = 500)
            queryImage=cv2.imread(f)
            queryImage = imutils.resize(queryImage, width = 500)
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
                        #print ("i = " + str(i))
                        #print ("j= " + str(j))
            #print ("len(ratio_l) =" +str(len(ratio_l)))
            if len(ratio_l) > 30:
                del ratio_l[30]
                del vis_l[30]

for k in range(0,len(ratio_l)):
    outpath = "./Output/" + str(k+1) + "-" +"("+str(round(ratio_l[k],3)) + ").jpg"
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