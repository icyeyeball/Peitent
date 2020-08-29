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
import time

localtime_init = time.asctime( time.localtime(time.time()))
print("開始時間: "+ localtime_init) 

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
copNo = re.compile("[^0-9^]")

#print(judge1)
#print(judge2)

# for instance: (1)"LIKE '45%'"  (2)"LIKE '%、45%'" (3)"LIKE '3519%'" (4)"LIKE '%、3519%'"
tmark_l = []

cmd_users = "SELECT imageData1, tmarkName, applNo tag FROM tmarkTable4 WHERE goodsGroup LIKE '0102%'"
cursor.execute(cmd_users)
tmark_list1 = cursor.fetchall()
cmd_users = "SELECT imageData1, tmarkName, applNo tag FROM tmarkTable4 WHERE goodsGroup LIKE '%、0102%'"
cursor.execute(cmd_users)
tmark_list2 = cursor.fetchall()
tmark_list1.extend(tmark_list2)
tmark_list0 = list(set(tmark_list1))


for i in range(len(tmark_list0)):
    try:
        nPos = tmark_list0[i][1].index("圖")
    except ValueError:
        continue
    else:
        if nPos > 1:
            tmark = {'applno': tmark_list0[i][2],'file':tmark_list0[i][0]}
            tmark_l.append(tmark)
            continue
    try:
        nPos = tmark_list0[i][1].index("標章")
    except ValueError:
        continue
    else:
        if nPos > 1:
            tmark = {'applno': tmark_list0[i][2],'file':tmark_list0[i][0]}
            tmark_l.append(tmark)
            continue
    try:
        nPos = tmark_list0[i][1].index("設計字")
    except ValueError:
        continue
    else:
        if nPos > 1:
            tmark = {'applno': tmark_list0[i][2],'file':tmark_list0[i][0]}
            tmark_l.append(tmark)
            continue
    try:
        nPos = tmark_list0[i][1].index("Logo")
    except ValueError:
        continue
    else:
        if nPos > 1:
            tmark = {'applno': tmark_list0[i][2],'file':tmark_list0[i][0]}
            tmark_l.append(tmark)
            continue
    try:
        nPos = tmark_list0[i][1].index("LOGO")
    except ValueError:
        continue
    else:
        if nPos > 1:
            tmark = {'applno': tmark_list0[i][2],'file':tmark_list0[i][0]}
            tmark_l.append(tmark)
            continue
    try:
        nPos = tmark_list0[i][1].index("設計圖")
    except ValueError:
        continue
    else:
        if nPos > 1:
            tmark = {'applno': tmark_list0[i][2],'file':tmark_list0[i][0]}
            tmark_l.append(tmark)
            continue

samplePath = './3.png' #input sample
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


outputPath='./7163-3/' #path of database
tmpfiles = os.listdir(outputPath)
for f in tmpfiles:
    os.remove('./7163-3/'+str(f))

sampleImage = cv2.imread(samplePath,0)
sampleImage1 = imutils.resize(sampleImage, width = 300)
sampleImage1 = cv2.GaussianBlur(sampleImage1, (5, 5), 0)
kp1_1, des1_1 = sift.detectAndCompute(sampleImage1, None) #detect the features of sample

sampleImage = cv2.imread(samplePath,0)
sampleImage2 = imutils.resize(sampleImage, width = 300)
sampleImage2 = cv2.GaussianBlur(sampleImage2, (1, 1), 0)
ret,sampleImage2 = cv2.threshold(sampleImage2,220,255,cv2.THRESH_BINARY)
#sampleImage = cv2.Canny(sampleImage, 30, 150)
kp1_2, des1_2 = sift.detectAndCompute(sampleImage2, None) #detect the features of sample
index = 0

cmd_users = "SELECT tag FROM tmarkTable4 WHERE applno = 106075444"
cursor.execute(cmd_users)
typical = cursor.fetchone()   
list0 = typical[0].split(",")

for t in tmark_l:
    index = index + 1
    print(index)
    predict = 0
    string = ""
    cmd_users = "SELECT tag FROM tmarkTable4 WHERE applno = '" + t["applno"] + "'"
    cursor.execute(cmd_users)
    tags = cursor.fetchone()
    try:
        tags_list0 = tags[0].split(",")
        for i in tags_list0:
            if i != "":
                if i in list0:
                    print("======================Yes!!!")
                    print(i)
                    predict = predict + 5
                    string = string + "-" + i
                else:
                    pass
        f = t['file']
        queryImage=cv2.imread(f,0)
        try:
            queryImage = imutils.resize(queryImage, width = 300)
        except:
            continue
        else:
            queryImage1 = cv2.GaussianBlur(queryImage, (5, 5), 0)
            kp2_1, des2_1 = sift.detectAndCompute(queryImage1, None) #detect the features of img in database

            queryImage2 = cv2.GaussianBlur(queryImage, (1, 1), 0)
            ret,queryImage2 = cv2.threshold(queryImage2,220,255,cv2.THRESH_BINARY)
            kp2_2, des2_2 = sift.detectAndCompute(queryImage2, None) #detect the features of img in database
        
            try:
                matches2=flann.knnMatch(des2_2,des1_2,k=2) #matched features, assign k=2 to return 2 matched features.
            except:
                continue
            else:
                (matchNum2,matchesMask2)=getMatchNum(matches2,0.9) #set ratio = 0.9 to calculate the matching level
                if len(matches2) != 0:
                    matchRatio2_2=matchNum2*100/len(matches2)
                else:
                    matchRatio2_2=0.
            try:
                matches2=flann.knnMatch(des1_2,des2_2,k=2) #matched features, assign k=2 to return 2 matched features.
            except:
                continue
            else:
                (matchNum2,matchesMask2)=getMatchNum(matches2,0.9) #set ratio = 0.9 to calculate the matching level
                if len(matches2) != 0:
                    matchRatio1_2=matchNum2*100/len(matches2)
                else:
                    matchRatio1_2=0.           
                matchRatio2 = (matchRatio1_2 + matchRatio2_2)/2.
            
            try:
                matches1=flann.knnMatch(des2_1,des1_1,k=2) #matched features, assign k=2 to return 2 matched features.
            except:
                continue
            else:
                (matchNum1,matchesMask1)=getMatchNum(matches1,0.9) #set ratio = 0.9 to calculate the matching level
                if len(matches1) != 0:
                    matchRatio2_1=matchNum1*100/len(matches1)
                else:
                    matchRatio2_1=0.
            try:
                matches1=flann.knnMatch(des1_1,des2_1,k=2) #matched features, assign k=2 to return 2 matched features.
            except:
                continue
            else:
                (matchNum1,matchesMask1)=getMatchNum(matches1,0.9) #set ratio = 0.9 to calculate the matching level
                if len(matches1) != 0:
                    matchRatio1_1=matchNum1*100/len(matches1)
                else:
                    matchRatio1_1=0.           
                matchRatio1 = (matchRatio1_1 + matchRatio2_1)/2.
           
                drawParams=dict(matchColor=(0,255,0),  singlePointColor=(0,0,255), matchesMask=matchesMask1, flags=0)
                sampleImage=cv2.imread(samplePath)
                queryImage=cv2.imread(f)
                sampleImage=cv2.imread(samplePath)
                sampleImage = imutils.resize(sampleImage, width = 300)
                queryImage=cv2.imread(f)
                queryImage = imutils.resize(queryImage, width = 300)
                #(hA, wA) =sampleImage.shape[:2]  
                #(hB, wB) = queryImage.shape[:2]
                #comparisonImage=cv2.drawMatchesKnn(sampleImage,kp1_1,queryImage,kp2_1,matches1,None,**drawParams)
                #cv2.putText(comparisonImage,str(matchRatio) + "%",(int(wA+wB/2.),int(3.*hB/4.)),cv2.FONT_HERSHEY_PLAIN,int(1.*hB/50.),(0,0,255),4)
                subtotal_1 = {"applno":t["applno"],"ratio":matchRatio1+predict, "picture":queryImage, "name":string}
                subtotal_2 = {"applno":t["applno"],"ratio":matchRatio2+predict, "picture":queryImage, "name":string}
                #print(f + " = " + str(matchRatio))
                if subtotal_1["ratio"] > subtotal_2["ratio"]:
                    subtotal = subtotal_1
                else:
                    subtotal = subtotal_2
                
                if subtotal["ratio"] > 30.0:
                    result.append(subtotal)
                    for i in range(0,len(result)-1):
                        for j in range(0,len(result)-1-i): 
                            if result[j]["ratio"] < result[j+1]["ratio"]:
                                tmp = result[j]
                                result[j]= result[j+1]
                                result[j+1] = tmp
                    if len(result) > 100:
                        del result[100]
                else:
                    continue
    except:
        continue
    else:
        continue
                
#print("tmark_l = " + str(len(tmark_l)))

data = []
#print(len(result))
for i in result:
    #print (str(i["applno"])+","+str(i["ratio"]))
    data.append({"applno":i["applno"], "ratio":i["ratio"]})
   
app_json = json.dumps(data)
print(app_json)
for k in range(0,len(result)):
    outpath = "./7163-3/" + str(k+1) + "-" +"("+str(round(result[k]["ratio"],3)) + "-" + str(result[k]["applno"]) +")"+result[k]["name"]+"-.jpg"
    #print ("===========================")
    #print (outpath)
    cv2.imwrite(outpath, result[k]["picture"])

# initial time and end time
#print("總筆數 = " + str(len(tmark_list11)))
localtime_end = time.asctime( time.localtime(time.time()))
print("開始時間: "+ localtime_init)     
print("結束時間: "+ localtime_end)