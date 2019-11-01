# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import mysql.connector
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "patent", database = "tmarkdb",  )
cursor=tmarkdb.cursor()

"""
# Create db
cursor.execute("CREATE DATABASE maxdb")


# Create table
cursor.execute("CREATE TABLE fff (name VARCHAR(255), age INTEGER(99), user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
"""
# Insert Multiple Records
"""
sqlStuff = "INSERT INTO users (name, age) VALUES (%s,%s)"
records = [("Steve", 24),
           ("Max", 25),
           ("Chang" ,26),]
cursor.executemany(sqlStuff, records)
tmarkdb.commit()
"""
sqlStuff = "INSERT INTO tmarkTable (examNo, applNo, tmarkName, tmarkClassDesc, imageData1, imageData2, imageData3, imageData4, imageData5, imageData6, tmarkType, tmarkTypeDesc, tmarkColor, tmarkColorDesc, tmarkDraftC, tmarkDraftE, tmarkDraftJ, tmarkSign, wordDescription, goodsclassCode, goodsName, goodsGroup, deadline,volNo1, volNo2, processorName, holderChineseName, holderEnglishName, holderJapaneseName, holderAddress, countryCode, chineseCountryName, agentChineseName, agentAddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
records = [("11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11", "11111", "11111", "11111","11", "11", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111", "11111"),]
cursor.executemany(sqlStuff, records)
tmarkdb.commit() 
 # Read
cursor.execute("SELECT * FROM tmarkTable Where examNo Like '1%'")
result = cursor.fetchall()
for row in result:
    print(row)