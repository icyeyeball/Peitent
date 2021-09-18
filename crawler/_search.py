# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import sys
import mysql.connector
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()


# Read

#delete_users = "DELETE FROM tmarkTable WHERE examNo = 11111"
find = str(sys.argv[1])
judge1 = "= '" + str(sys.argv[2]) + "%'"
judge2 = "= '%、" + str(sys.argv[2]) + "%'"


cmd_users = "SELECT "+find+" FROM tmarkTable WHERE applNo "+ judge1
cursor.execute(cmd_users)
tmark_list11 = cursor.fetchall()
cmd_users = "SELECT "+find+" FROM tmarkTable WHERE applNo "+ judge1
cursor.execute(cmd_users)
tmark_list12 = cursor.fetchall()
cmd_users = "SELECT "+find+" FROM tmarkTable2 WHERE applNo "+ judge1
cursor.execute(cmd_users)
tmark_list21 = cursor.fetchall()
cmd_users = "SELECT "+find+" FROM tmarkTable2 WHERE applNo "+ judge1
cursor.execute(cmd_users)
tmark_list22 = cursor.fetchall()
cmd_users = "SELECT "+find+" FROM tmarkTable3 WHERE applNo "+ judge1
cursor.execute(cmd_users)
tmark_list31 = cursor.fetchall()
cmd_users = "SELECT "+find+" FROM tmarkTable3 WHERE applNo "+ judge1
cursor.execute(cmd_users)
tmark_list32 = cursor.fetchall()
cmd_users = "SELECT "+find+" FROM tmarkTable4 WHERE applNo "+ judge1
cursor.execute(cmd_users)
tmark_list41 = cursor.fetchall()
cmd_users = "SELECT "+find+" FROM tmarkTable4 WHERE applNo "+ judge1
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

print(tmark_list11)
