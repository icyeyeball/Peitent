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
cursor=tmarkdb.cursor()
# Read


samplePath = './picBase/'
tmpfiles = os.listdir(samplePath)
tmpfiles.sort()
for f in tmpfiles:
    cmd_users = "SELECT tmarkName FROM tmarkTable WHERE applNo='"+ str(f[0:-6]) +"'"
    cursor.execute(cmd_users)
    tmark_list1 = cursor.fetchall()
    cmd_users = "SELECT tmarkName FROM tmarkTable WHERE applNo='"+ str(f[0:-6]) +"'"
    cursor.execute(cmd_users)
    tmark_list2 = cursor.fetchall()
    cmd_users = "SELECT tmarkName FROM tmarkTable WHERE applNo='"+ str(f[0:-6]) +"'"
    cursor.execute(cmd_users)
    tmark_list3 = cursor.fetchall()
    cmd_users = "SELECT tmarkName FROM tmarkTable WHERE applNo='"+ str(f[0:-6]) +"'"
    cursor.execute(cmd_users)
    tmark_list4 = cursor.fetchall()
    if tmark_list1 or tmark_list2 or tmark_list3 or tmark_list4:
        continue
    else:
        print(f)
        os.remove('./picBase/'+str(f))

