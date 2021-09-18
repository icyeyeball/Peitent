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
#delete_users = "DELETE FROM tmarkTable WHERE indexNo = 1175961"
delete_users = "DELETE FROM tmarkTable4 WHERE imageData1 = './picBase/000000000-1.png'"
cursor.execute(delete_users)
tmarkdb.commit()