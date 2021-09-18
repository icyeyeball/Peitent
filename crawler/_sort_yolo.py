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
copAB = re.compile("[^A-Z^a-z]")


    
tmpfiles = os.listdir('../../peitent/crawler/yoloout2/')
for f in tmpfiles:
    os.remove('../../peitent/crawler/yoloout2/'+str(f))


cmd_users = "SELECT applno FROM tmarkTable WHERE goodsGroup LIKE '0102%'"
cursor.execute(cmd_users)
tmark_list11_1 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable WHERE goodsGroup LIKE '%、0102%'"
cursor.execute(cmd_users)
tmark_list12_1 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable2 WHERE goodsGroup LIKE '0102%'"
cursor.execute(cmd_users)
tmark_list21_2 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable2 WHERE goodsGroup LIKE '%、0102%'"
cursor.execute(cmd_users)
tmark_list22_2 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable3 WHERE goodsGroup LIKE '0102%'"
cursor.execute(cmd_users)
tmark_list31_3 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable3 WHERE goodsGroup LIKE '%、0102%'"
cursor.execute(cmd_users)
tmark_list32_3 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable4 WHERE goodsGroup LIKE '0102%'"
cursor.execute(cmd_users)
tmark_list41_4 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable4 WHERE goodsGroup LIKE '%、0102%'"
cursor.execute(cmd_users)
tmark_list42_4 = cursor.fetchall()

tmark_list11_1.extend(tmark_list12_1) 
tmark_list11_1.extend(tmark_list21_2)
tmark_list11_1.extend(tmark_list22_2)
tmark_list11_1.extend(tmark_list31_3)
tmark_list11_1.extend(tmark_list32_3)
tmark_list11_1.extend(tmark_list41_4)
tmark_list11_1.extend(tmark_list42_4)
tmark_list11_1 = list(set(tmark_list11_1))
tmark_list1= []
tmark_list_num1 = []

for i in tmark_list11_1:
    if 'M' in str(i[0]):
        print("sleep 5")
        print(i[0])
        time.sleep(5)
        continue
    elif int(i[0]) < int(93050000):
        continue
    else:
        tmark_list1.append(int(i[0]))
tmark_list1.sort()
index1 = 0
for i in tmark_list1:
    if index1 == 1000:
        break
    if int(i) >= 100000000:
        print('../../peitent/crawler/picBase/'+str(i)+'-1.png -->'+'../../peitent/crawler/yoloin/'+str(i)+'-1.png')
        shutil.copyfile('../../peitent/crawler/picBase/'+str(i)+'-1.png','../../peitent/crawler/yoloin/'+str(i)+'-1.png')
    else:
        print('../../peitent/crawler/picBase/0'+str(i)+'-1.png --?'+'../../peitent/crawler/yoloin/0'+str(i)+'-1.png')
        shutil.copyfile('../../peitent/crawler/picBase/0'+str(i)+'-1.png','../../peitent/crawler/yoloin/0'+str(i)+'-1.png')
    index1 = index1+1

print("sleep 10")
time.sleep(10)

cmd_users = "SELECT applno FROM tmarkTable WHERE goodsGroup LIKE '0810%'"
cursor.execute(cmd_users)
tmark_list11_5 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable WHERE goodsGroup LIKE '%、0810%'"
cursor.execute(cmd_users)
tmark_list12_5 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable2 WHERE goodsGroup LIKE '0810%'"
cursor.execute(cmd_users)
tmark_list21_6 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable2 WHERE goodsGroup LIKE '%、0810%'"
cursor.execute(cmd_users)
tmark_list22_6 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable3 WHERE goodsGroup LIKE '0810%'"
cursor.execute(cmd_users)
tmark_list31_7 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable3 WHERE goodsGroup LIKE '%、0810%'"
cursor.execute(cmd_users)
tmark_list32_7 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable4 WHERE goodsGroup LIKE '0810%'"
cursor.execute(cmd_users)
tmark_list41_8 = cursor.fetchall()
cmd_users = "SELECT applno FROM tmarkTable4 WHERE goodsGroup LIKE '%、0810%'"
cursor.execute(cmd_users)
tmark_list42_8 = cursor.fetchall()
#print(tmark_list42_8)

tmark_list11_5.extend(tmark_list12_5) 
tmark_list11_5.extend(tmark_list21_6)
tmark_list11_5.extend(tmark_list22_6)
tmark_list11_5.extend(tmark_list31_7)
tmark_list11_5.extend(tmark_list32_7)
tmark_list11_5.extend(tmark_list41_8)
tmark_list11_5.extend(tmark_list42_8)
tmark_list11_5 = list(set(tmark_list11_5))
tmark_list2= []
tmark_list_num2 = []


#80044400
for i in tmark_list11_5:
    if 'M' in str(i[0]):
        print("tmark_list11_5")
        time.sleep(7)
        print("sleep")
        print(i[0])
        time.sleep(5)
        continue
    elif int(i[0]) < int(80044400):
        continue
    else:
        tmark_list2.append(int(i[0]))
tmark_list2.sort()
index2 = 0
for i in tmark_list2:
    if index2 == 1000:
        break
    if int(i) >= 100000000:
        print('../../peitent/crawler/picBase/'+str(i)+'-1.png -->'+'../../peitent/crawler/yoloin2/'+str(i)+'-1.png')
        shutil.copyfile('../../peitent/crawler/picBase/'+str(i)+'-1.png -->'+'../../peitent/crawler/yoloin2/0'+str(i)+'-1.png')
    else:
        print('../../peitent/crawler/picBase/0'+str(i)+'-1.png'+'../../peitent/crawler/yoloin2/0'+str(i)+'-1.png')
        shutil.copyfile('../../peitent/crawler/picBase/0'+str(i)+'-1.png','../../peitent/crawler/yoloin2/0'+str(i)+'-1.png')
    index2 = index2+1
        
print("sleep 10")

time.sleep(10)

