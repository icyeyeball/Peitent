# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import  pymysql 
conn  =  pymysql . connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "patent" ,  db = 'tmarkdb' ) 
cur  =  conn . cursor () 
cur . execute ( "SELECT Host,User FROM user" ) 
for  r  in  cur : 
    print ( r ) 
cur . close () 
conn . close()