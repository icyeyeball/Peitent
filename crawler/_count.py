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

judge1 = "LIKE '" + str(sys.argv[1]) + "%'"
judge2 = "LIKE '%、" + str(sys.argv[1]) + "%'"
cmd_users = "SELECT applNo FROM tmarkTable WHERE goodsGroup " + judge1
cursor.execute(cmd_users)
tmark_list11 = cursor.fetchall()
cmd_users = "SELECT applNo FROM tmarkTable WHERE goodsGroup " + judge2
cursor.execute(cmd_users)
tmark_list12 = cursor.fetchall()
cmd_users = "SELECT applNo FROM tmarkTable2 WHERE goodsGroup " + judge1
cursor.execute(cmd_users)
tmark_list21 = cursor.fetchall()
cmd_users = "SELECT applNo FROM tmarkTable2 WHERE goodsGroup " + judge2
cursor.execute(cmd_users)
tmark_list22 = cursor.fetchall()
cmd_users = "SELECT applNo FROM tmarkTable3 WHERE goodsGroup " + judge1
cursor.execute(cmd_users)
tmark_list31 = cursor.fetchall()
cmd_users = "SELECT applNo FROM tmarkTable3 WHERE goodsGroup " + judge2
cursor.execute(cmd_users)
tmark_list32 = cursor.fetchall()
cmd_users = "SELECT applNo FROM tmarkTable4 WHERE goodsGroup " + judge1
cursor.execute(cmd_users)
tmark_list41 = cursor.fetchall()
cmd_users = "SELECT applNo FROM tmarkTable4 WHERE goodsGroup " + judge2
cursor.execute(cmd_users)
tmark_list42 = cursor.fetchall()
#combine these two lists
tmark_list11.extend(tmark_list12)
tmark_list11.extend(tmark_list21)
tmark_list11.extend(tmark_list22)
tmark_list11.extend(tmark_list31)
tmark_list11.extend(tmark_list32)
tmark_list11.extend(tmark_list41)
tmark_list11.extend(tmark_list42)
tmark_list11 = list(set(tmark_list11))
#for i in range(0,len(tmark_list)):
    #print(tmark_list[i])  
print(datetime.datetime.today())    
print(len(tmark_list11))
