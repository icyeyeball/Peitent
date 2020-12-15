        # -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import sys
import mysql.connector
import re
import os
import shutil
import pymysql
import time

tmarkdb = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor(buffered=True)
copAB = re.compile("[^0-9^.^-^a-z^A-Z]")

outputPath1='../../peitent/crawler/yoloout/' #path of database
tmpfiles = os.listdir(outputPath1)
for f in tmpfiles:
    os.remove('../../peitent/crawler/yoloout/'+str(f))
    
outputPath2='../../peitent/crawler/yoloout2/' #path of database
tmpfiles = os.listdir(outputPath2)
for f in tmpfiles:
    os.remove('../../peitent/crawler/yoloout2/'+str(f))
################
index1 = 0
tmpfiles = os.listdir('../../peitent/crawler/yoloin/')

for f in tmpfiles:
    print("==================================================")
    print("======================"+f+"===========================")
    print("==================================================")
    if index1 == 5:
        break
    print("FILE = " + f)
    print("index1: " + str(index1))
    shutil.copyfile('../../peitent/crawler/yoloin/'+str(f),'../../peitent/crawler/yoloout/'+str(f))
    os.system('python flow --model cfg/yolo.cfg --load bin/yolov2.weights --imgdir ../../peitent/crawler/yoloout/')
    with open ("./result.txt",'r',encoding = 'utf-8') as f1:
        string_list = []
        for line in f1.readlines():
            line = copAB.sub('', line)
            string_list.append(line)
        string_list=(set(string_list))
    string1 = ""
    for i in string_list:
        string1 = string1 + str(i) + ","
    index1 = index1 + 1
    
    
    
    outputPath1='../../peitent/crawler/yoloout/' #path of database
    tmpfiles = os.listdir(outputPath1)
    for f in tmpfiles:
        os.remove('../../peitent/crawler/yoloout/'+str(f))    
    outputPath2='../../peitent/crawler/yoloout2/' #path of database
    tmpfiles = os.listdir(outputPath2)
    for f in tmpfiles:
        os.remove('../../peitent/crawler/yoloout2/'+str(f))
        
        
        
    sql1 = "UPDATE tmarkTable SET tag='"+string1+"' WHERE applno='"+str(f[0:-6])+"'"
    cursor.execute(sql1)
    tmarkdb.commit()
    sql2 = "UPDATE tmarkTable2 SET tag='"+string1+"' WHERE applno='"+str(f[0:-6])+"'"
    cursor.execute(sql2)
    tmarkdb.commit()
    sql3 = "UPDATE tmarkTable3 SET tag='"+string1+"' WHERE applno='"+str(f[0:-6])+"'"
    cursor.execute(sql3)
    tmarkdb.commit()
    sql4 = "UPDATE tmarkTable4 SET tag='"+string1+"' WHERE applno='"+str(f[0:-6])+"'"
    cursor.execute(sql4)
    tmarkdb.commit()
    

#################
index2 = 0
tmpfiles = os.listdir('../../peitent/crawler/yoloin2/')

for f in tmpfiles:
    print("==================================================")
    print("======================"+f+"===========================")
    print("==================================================")
    if index2 == 5:
        break
    print("FILE = " + f)
    print("index2: " + str(index2))
    shutil.copyfile('../../peitent/crawler/yoloin2/'+str(f),'../../peitent/crawler/yoloout2/'+str(f))
    os.system('python flow --model cfg/yolo.cfg --load bin/yolov2.weights --imgdir ../../peitent/crawler/yoloout2/')
    with open ("./result.txt",'r',encoding = 'utf-8') as f2:
        string_list = []
        for line in f2.readlines():
            line = copAB.sub('', line)
            string_list.append(line)
        string_list=(set(string_list))
    string2 = ""
    for i in string_list:
        string2 = string2 + str(i) + ","
    index2 = index2 + 1
    
    
    outputPath1='../../peitent/crawler/yoloout/' #path of database
    tmpfiles = os.listdir(outputPath1)
    for f in tmpfiles:
        os.remove('../../peitent/crawler/yoloout/'+str(f))    
    outputPath2='../../peitent/crawler/yoloout2/' #path of database
    tmpfiles = os.listdir(outputPath2)
    for f in tmpfiles:
        os.remove('../../peitent/crawler/yoloout2/'+str(f))
        
        
    sql1 = "UPDATE tmarkTable SET tag='"+string2+"' WHERE applno='"+str(f[0:-6])+"'"
    cursor.execute(sql1)
    tmarkdb.commit()
    sql2 = "UPDATE tmarkTable2 SET tag='"+string2+"' WHERE applno='"+str(f[0:-6])+"'"
    cursor.execute(sql2)
    tmarkdb.commit()
    sql3 = "UPDATE tmarkTable3 SET tag='"+string2+"' WHERE applno='"+str(f[0:-6])+"'"
    cursor.execute(sql3)
    tmarkdb.commit()
    sql4 = "UPDATE tmarkTable4 SET tag='"+string2+"' WHERE applno='"+str(f[0:-6])+"'"
    cursor.execute(sql4)
    tmarkdb.commit()
