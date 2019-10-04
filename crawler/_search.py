# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import mysql.connector
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()


 # Read
#delete_users = "DELETE FROM tmarkTable WHERE examNo = 11111"
search_users = "SELECT *FROM tmarkTable WHERE tmarkName LIKE '%黑松%'"
cursor.execute(search_users)
tmark_list = cursor.fetchall()
for i in range(0,len(tmark_list)):
    print(tmark_list[i])  
