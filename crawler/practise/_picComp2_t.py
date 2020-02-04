# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
#
import os
from os import *
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
import imutils
import sys
import mysql.connector
import re
import shutil
import json

def getMatchNum(matches,ratio):
    '''number of matched features and relation'''
    matchesMask=[[0,0] for i in range(len(matches))]
    matchNum=0
    for i,(m,n) in enumerate(matches):
        if m.distance<ratio*n.distance: #select the distance > ratio
            matchesMask[i]=[1,0]
            matchNum+=1
    return (matchNum,matchesMask)
#connect to database
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()
cop = re.compile("[^.^/^A-Z^a-z^0-9^-]")

# for instance: (1)"LIKE '45%'"  (2)"LIKE '%、45%'" (3)"LIKE '3519%'" (4)"LIKE '%、3519%'"
cmd_users = "SELECT imageData1, tmarkName, applNo FROM tmarkTable WHERE goodsGroup " + sys.argv[2]
cursor.execute(cmd_users)
tmark_list11 = cursor.fetchall()
cmd_users = "SELECT imageData1, tmarkName, applNo FROM tmarkTable WHERE goodsGroup " + sys.argv[3]
cursor.execute(cmd_users)
tmark_list12 = cursor.fetchall()
cmd_users = "SELECT imageData1, tmarkName, applNo FROM tmarkTable2 WHERE goodsGroup " + sys.argv[2]
cursor.execute(cmd_users)
tmark_list21 = cursor.fetchall()
cmd_users = "SELECT imageData1, tmarkName, applNo FROM tmarkTable2 WHERE goodsGroup " + sys.argv[3]
cursor.execute(cmd_users)
tmark_list22 = cursor.fetchall()
cmd_users = "SELECT imageData1, tmarkName, applNo FROM tmarkTable3 WHERE goodsGroup " + sys.argv[2]
cursor.execute(cmd_users)
tmark_list31 = cursor.fetchall()
cmd_users = "SELECT imageData1, tmarkName, applNo FROM tmarkTable3 WHERE goodsGroup " + sys.argv[3]
cursor.execute(cmd_users)
tmark_list32 = cursor.fetchall()
cmd_users = "SELECT imageData1, tmarkName, applNo FROM tmarkTable4 WHERE goodsGroup " + sys.argv[2]
cursor.execute(cmd_users)
tmark_list41 = cursor.fetchall()
cmd_users = "SELECT imageData1, tmarkName, applNo FROM tmarkTable4 WHERE goodsGroup " + sys.argv[3]
cursor.execute(cmd_users)
tmark_list42 = cursor.fetchall()
#combine these two lists
tmark_list11.extend(tmark_list12)
tmark_list11.extend(tmark_list21)
tmark_list11.extend(tmark_list22)
tmark_list11.extend(tmark_list31)
tmark_list11.extend(tmark_list32)
tmark_list11.extend(tmark_list41)
tmark_list11.extend(tmark_list42)
tmark_list11 = list(set(tmark_list11))
#標章圖 標章 及圖 圖 及少女圖 及圖案 設計圖
tmark_list = []
for i in range(len(tmark_list11)):
    try:
        nPos = tmark_list11[i][1].index("圖")
    except ValueError:
        continue
    else:
        tmark_list.append(tmark_list11[i])
        continue
    try:
        nPos = tmark_list11[i][1].index("標章")
    except ValueError:
        continue
    else:
        tmark_list.append(tmark_list11[i])

tmark_l = []
otherpath = './data/' #path of database
others = listdir(otherpath)
#print(otherpath)
#print(others)
for i in range(0,10):
    otherpic = "./data/" + others[i]
    tmark = {'applno': "000000000",'file':otherpic}
    tmark_l.append(tmark)

for i in range(0, len(tmark_list)):
    #if len(cop.sub('', str(tmark_list[i]))) == 24:
    tmark = {'applno': tmark_list[i][2],'file':tmark_list[i][0]}
    tmark_l.append(tmark)

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
applno_l=[]
result = []


outputPath='./Output/' #path of database
tmpfiles = os.listdir(outputPath)
for f in tmpfiles:
    os.remove('./Output/'+str(f))

sampleImage = cv2.imread(samplePath,0)
sampleImage = imutils.resize(sampleImage, width = 300)
sampleImage = cv2.GaussianBlur(sampleImage, (1, 1), 0)
ret,sampleImage = cv2.threshold(sampleImage,220,255,cv2.THRESH_BINARY)
kp1, des1 = sift.detectAndCompute(sampleImage, None) #detect the features of sample
index = 0
for t in tmark_l:
    index = index + 1
    print("index = " + str(index))
    f = t['file']
    queryImage=cv2.imread(f,0)
    try:
        queryImage = imutils.resize(queryImage, width = 300)
    except AttributeError:
        continue
    else:
        queryImage = cv2.GaussianBlur(queryImage, (1, 1), 0)
        ret,queryImage = cv2.threshold(queryImage,220,255,cv2.THRESH_BINARY)
        #queryImage = cv2.Canny(queryImage, 30, 150)
        kp2, des2 = sift.detectAndCompute(queryImage, None) #detect the features of img in database
        
        try:
            matches=flann.knnMatch(des2,des1,k=2) #matched features, assign k=2 to return 2 matched features.
        except:
            continue
        else:
            (matchNum,matchesMask)=getMatchNum(matches,0.8) #set ratio = 0.9 to calculate the matching level
            if len(matches) != 0:
                matchRatio2=matchNum*100/len(matches)
            else:
                matchRatio2=0.
            
        try:
            matches=flann.knnMatch(des1,des2,k=2) #matched features, assign k=2 to return 2 matched features.
        except:
            continue
        else:
            (matchNum,matchesMask)=getMatchNum(matches,0.9) #set ratio = 0.9 to calculate the matching level
            if len(matches) != 0:
                matchRatio1=matchNum*100/len(matches)
            else:
                matchRatio1=0.
            
            matchRatio = (matchRatio1 + matchRatio2)/2.
            
            drawParams=dict(matchColor=(0,255,0),  singlePointColor=(0,0,255), matchesMask=matchesMask, flags=0)
            sampleImage=cv2.imread(samplePath)
            queryImage=cv2.imread(f)
            sampleImage=cv2.imread(samplePath)
            sampleImage = imutils.resize(sampleImage, width = 300)
            queryImage=cv2.imread(f)
            queryImage = imutils.resize(queryImage, width = 300)
            #(hA, wA) =sampleImage.shape[:2]  
            #(hB, wB) = queryImage.shape[:2]
            comparisonImage=cv2.drawMatchesKnn(sampleImage,kp1,queryImage,kp2,matches,None,**drawParams)
            #cv2.putText(comparisonImage,str(matchRatio) + "%",(int(wA+wB/2.),int(3.*hB/4.)),cv2.FONT_HERSHEY_PLAIN,int(1.*hB/50.),(0,0,255),4)
            subtotal = {"applno":t["applno"],"ratio":matchRatio, "picture":comparisonImage}
            result.append(subtotal)
            for i in range(0,len(result)-1): 
                for j in range(0,len(result)-1-i): 
                    if result[j]["ratio"] < result[j+1]["ratio"]:
                        tmp = result[j]
                        result[j]= result[j+1]
                        result[j+1] = tmp
                        #print ("i = " + str(i))
                        #print ("j= " + str(j))
            #print ("len(ratio_l) =" +str(len(ratio_l)))
            if len(result) > 50:
                del result[50]
                
print("tmark_l = " + str(len(tmark_l)))

data = []

for i in result:
    print (str(i["applno"])+","+str(i["ratio"]))
    data.append({"applno":i["applno"], "ratio":i["ratio"]})
   
app_json = json.dumps(data)
print(app_json)
for k in range(0,len(result)):
    outpath = "./Output/" + str(k+1) + "-" +"("+str(round(result[k]["ratio"],3)) + "-" + str(result[k]["applno"]) +").jpg"
    print ("===========================")
    print (outpath)
    cv2.imwrite(outpath, result[k]["picture"])


"""
column=4
row=5
#Draw the plots
figure,ax=plt.subplots(row,column)
for index in range(0,20):
    ax[int(index/column)][index%column].set_title('Similiarity %.2f%%' % ratio_l[index])
    ax[int(index/column)][index%column].imshow(vis_l[index])
plt.show()
""" 