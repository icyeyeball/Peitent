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
if len(sys.argv) < 5:   
    print ("Usage: python 要搜索的欄位 條件欄位 條件型態 條件設定")
    print ("e.g.")
    print ("python _search.py tmarkName agentChineseName  LIKE '%長文%'")
    print ("python _search.py tmarkName agentChineseName = '陳長文'")
    print ("=========================")
#delete_users = "DELETE FROM tmarkTable WHERE examNo = 11111"
search_users = "SELECT " + sys.argv[1] +" FROM tmarkTable WHERE " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4]
cursor.execute(search_users)
tmark_list = cursor.fetchall()
for i in range(0,len(tmark_list)):
    print(tmark_list[i])  
