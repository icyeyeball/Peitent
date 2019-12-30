# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import sys
import mysql.connector
import time
import datetime
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()


search_users = "SELECT COUNT(examNo) FROM tmarkTable4"
cursor.execute(search_users)
tmark_list = cursor.fetchall()
#for i in range(0,len(tmark_list)):
    #print(tmark_list[i])  
print(datetime.datetime.today())    
print(tmark_list)
