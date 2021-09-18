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


cmd_users = "SELECT applno FROM tmarkTable4 WHERE goodsGroup LIKE '0102%'"
cursor.execute(cmd_users)
tmark_list1 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable4 WHERE goodsGroup LIKE '%、0102%'"
cursor.execute(cmd_users)
tmark_list2 = cursor.fetchall()
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

    

    

