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
cursor.execute("SELECT * FROM tmarkTable WHERE examNo LIKE '%170%'")
#cursor.execute("SELECT * FROM tmarkTable WHERE examNo = '00017029'")
row = cursor.fetchone()
for row in cursor:
    print(row)

tmarkdb.close()

