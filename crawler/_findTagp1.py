# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import sys
import mysql.connector
import os
import shutil
import re
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()

copAB = re.compile("[^A-Z^a-z^,^]")

tmpfiles = os.listdir('./yoloin3')
tmpfiles.sort()
print("tmpfiles:" + str(len(tmpfiles)))
tag_list=["aeroplane"]
len_tag_list = len(tag_list)
tag_total = []

index =0
for f in tmpfiles:
    index = index+1
    print(index)    
    """
    cmd_users = "SELECT tag FROM tmarkTable WHERE applNo='"+ f[0:-6] +"'"
    cursor.execute(cmd_users)
    tag_tuple = cursor.fetchall()
    print(tag_tuple)
    if not len(tag_tuple) == 0:
        tag_list_db = list(tag_tuple[0])
        tag_string = tag_list_db[0]
        str1 = tag_string.split(",")
    else:
        str1 = ""

    
    cmd_users = "SELECT tag FROM tmarkTable2 WHERE applNo='"+ f[0:-6] +"'"
    cursor.execute(cmd_users)
    tag_tuple = cursor.fetchall()
    print(tag_tuple)
    if not len(tag_tuple) == 0:
        tag_list_db = list(tag_tuple[0])
        tag_string = tag_list_db[0]
        str2 = tag_string.split(",")
    else:
        str2 = ""

    
    cmd_users = "SELECT tag FROM tmarkTable3 WHERE applNo='"+ f[0:-6] +"'"
    cursor.execute(cmd_users)
    tag_tuple = cursor.fetchall()
    print(tag_tuple)
    if not len(tag_tuple) == 0:
        tag_list_db = list(tag_tuple[0])
        tag_string = tag_list_db[0]
        str3 = tag_string.split(",")
    else:
        str3 = ""

    """
    cmd_users = "SELECT tag FROM tmarkTable4 WHERE applNo='"+ f[0:-6] +"'"
    cursor.execute(cmd_users)
    tag_tuple = cursor.fetchall()
    print(tag_tuple)
    if not len(tag_tuple) == 0:
        tag_list_db = list(tag_tuple[0])
        tag_string = tag_list_db[0]
        str4 = tag_string.split(",")
    else:
        str4 = ""
        
    str5 = str4
        
    tag_total = [i for i in str5 if i in tag_list]
    
    if len(tag_total)>=1:
        print(tag_total)
        shutil.copyfile('./yoloin3/'+str(f),'./yoloout3_1/'+str(f[0:-6]+".png"))
        
        
        