# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import mysql.connector
import re
import os
import os 
import os.path
import shutil 
cop = re.compile("[^-^/^.^0-9^A-Z^a-z^]")
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()


 # Read
#delete_users = "DELETE FROM tmarkTable WHERE examNo = 11111"
cursor.execute("SELECT imageData1 FROM tmarktable")
_list = cursor.fetchall() 
pic_l = []
path2 = []
print(len(_list))
for i in range(len(_list)):
    pic_l.append(cop.sub('', str(_list[i])))
    path2.append(pic_l[i].strip().replace(u'picBase',u'picBase2'))
for i in range(len(pic_l)):
    try:
        shutil.copyfile(pic_l[i], path2[i])
    except FileNotFoundError:
        continue
    else:
        shutil.copyfile(pic_l[i], path2[i])
    
    
    
