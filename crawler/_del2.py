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
delete_users = "DELETE FROM tmarkTable WHERE examNo = 'A%'"
cursor.execute(delete_users)
tmarkdb.commit()