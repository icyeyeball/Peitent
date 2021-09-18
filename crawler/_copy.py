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

print()

index = 0

for f in tmark_list0:
    if not os.path.isfile('./picBase/'+f+'-1.png'):
        continue
    shutil.copyfile('./picBase/'+f+'-1.png','./picBase2/'+f+'-1.png')
    

