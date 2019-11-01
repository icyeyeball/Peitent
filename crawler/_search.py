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
print ("=========================")
print ("column: examNo, applNo, tmarkName, tmarkClassDesc, imageData1, imageData2, imageData3, imageData4, imageData5, imageData6, tmarkType, tmarkTypeDesc, tmarkColor, tmarkColorDesc, tmarkDraftC, tmarkDraftE, tmarkDraftJ, tmarkSign, wordDescription, goodsclassCode, goodsName, goodsGroup, deadline,volNo1, volNo2, processorName, holderChineseName, holderEnglishName, holderJapaneseName, holderAddress, countryCode, chineseCountryName, agentChineseName, agentAddress")
print ("=========================")

#delete_users = "DELETE FROM tmarkTable WHERE examNo = 11111"
search_users = "SELECT tmarkName FROM tmarkTable WHERE tmarkName LIKE '巧鄰%'"
cursor.execute(search_users)
tmark_list = cursor.fetchall()
for i in range(0,len(tmark_list)):
    print(tmark_list[i])  
