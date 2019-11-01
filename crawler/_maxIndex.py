# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import sys
import re
import mysql.connector
import time
import datetime
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()
cop = re.compile("[^0-9^]")

search_users = "SELECT indexNo  FROM tmarkTable"
cursor.execute(search_users)
tmark_list = cursor.fetchall()
num = 0
for i in tmark_list:
    #index = cop.sub('', i)
    string1 = str(i)
    tmp = cop.sub('', string1)
    if int(tmp) > num:
        num = int(tmp)
print(datetime.datetime.today())    
print(num)
