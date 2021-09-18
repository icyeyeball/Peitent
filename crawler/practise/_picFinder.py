# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import mysql.connector
import sys
import re
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()


 # Read
#delete_users = "DELETE FROM tmarkTable WHERE examNo = 11111"
cmd_users = "SELECT indexNo FROM tmarkTable WHERE examNo = " + sys.argv[1]
cursor.execute(cmd_users)
tmark_list = cursor.fetchall()
files = []
for i in range(len(tmark_list)):
    files.append(tmark_list[i])
    #files.append(cop.sub('', str(tmark_list[i])))
for f in files:
    print(f)