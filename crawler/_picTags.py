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

tmpfiles = os.listdir('./picBase')
tmpfiles.sort()

print(len(tmpfiles))
tmark_list1 = []
for f in tmpfiles:   


    cmd_users = "SELECT tmarkName FROM tmarkTable WHERE applNo='"+ f[0:-6] +"'"
    cursor.execute(cmd_users)
    tmark_list1 = cursor.fetchone()
    try:
        nPos = tmark_list1[0].index("圖")
    except ValueError:
        continue
    else:
        shutil.copyfile('./picBase/'+str(f),'./tagPic/'+str(f))
        os.remove('./picBase/'+str(f))
        os.system('python flow --model cfg/yolo.cfg --load bin/yolov2.weights --imgdir tagPic/')
   
    try:
        nPos = tmark_list1[0].index("標章")
    except ValueError:
        continue
    else:
        print(tmark_list1)
            
    try:
        nPos = tmark_list1[0].index("Logo")
    except ValueError:
        continue
    else:
        print(tmark_list1)
        
    try:
        nPos = tmark_list1[0].index("LOGO")
    except ValueError:
        continue
    else:
        print(tmark_list1)
        
    try:
        nPos = tmark_list1[0].index("設計圖")
    except ValueError:
        continue
    else:
        print(tmark_list1)
        

'''
tmark_list1.extend(tmark_list2)
tmark_list1 = list(set(tmark_list1))

tmark_list0 = []
for i in tmark_list1:
    tmark_list0.append((i[0]))
    
cmd_users = "SELECT tag FROM tmarkTable4 WHERE applno = 106044540"
cursor.execute(cmd_users)
typical = cursor.fetchone()   
list0 = typical[0].split(",")

result = []
len_tmark_list0 = len(tmark_list0)
index=0
for f in tmark_list0:
    index = index + 1
    print("index: " + str(index))
    predict = 0
    cmd_users = "SELECT tag FROM tmarkTable4 WHERE applno = '" + f + "'"
    cursor.execute(cmd_users)
    tags = cursor.fetchone()
    try:
        tags_list0 = tags[0].split(",")
        string = ""
        for i in tags_list0:
            if i != "":
                if i in list0:
                    print("======================Yes!!!")
                    predict = predict + 5
                    string = string + "-" + i
                else:
                    pass
        if predict != 0:
            subtotal = {"applno":f,"ratio":predict, "name":str(predict)+"-"+str(f)+string+".png"}
            result.append(subtotal)
    except:
        continue
    else:
        continue
#######
for i in result:
    shutil.copyfile('./picBase2/'+i["applno"]+'-1.png','./763-1/'+i["name"])    
'''

    

    

