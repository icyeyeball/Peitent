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

tmpfiles = os.listdir('./yoloout')
tmpfiles.sort()
print("tmpfiles:" + str(len(tmpfiles)))
tag_list=["tie"]
len_tag_list = len(tag_list)
tag_total = []

index =0
for f in tmpfiles:
    index = index+1
    print(index)
    cmd_users = "SELECT tag FROM tmarkTable WHERE applNo='"+ f[0:-6] +"'"
    #print(cmd_users)
    cursor.execute(cmd_users)
    tag_tuple = cursor.fetchall()
    tag_list_db = list(tag_tuple[0])
    tag_string = tag_list_db[0]
    #print(tag_string)
    str0 = tag_string.split(",")
    tag_total = [i for i in str0 if i in tag_list]
    
    if len(tag_total)>=1:
        print(tag_total)
        shutil.copyfile('./picBase2/'+str(f),'./yoloout2/'+str(f[0:-6]+"-"+str(len(tag_total))+".png"))

        
        
    