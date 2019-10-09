# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
import os
import requests
import time
from lxml import etree
from io import BytesIO
import requests.packages.urllib3
import urllib3
import urllib
from urllib.request import urlretrieve
from urllib.error import HTTPError
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pymysql
import time
import mysql.connector
import datetime
import sys
import re
import xml.sax
from bs4 import BeautifulSoup

tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()

class tmarkHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.examno = ""
        self.applno = ""
        self.tmarkname = ""
        self.tmarkClassDesc = ""
        self.imagedata1 = ""
        self.imagedata2 = ""
        self.imagedata3 = ""
        self.imagedata4 = ""
        self.imagedata5 = ""
        self.imagedata6 = ""
        self.tmarktype = ""
        self.tmarktypedesc = ""
        self.tmarkcolor = ""
        self.tmarkcolordesc = ""
        self.tmarkdraftc = ""
        self.tmarkdrafte = ""
        self.tmarkdraftj = ""
        self.tmarksign = ""
        self.worddescription = ""
        self.goodsclasscode = ""
        self.goodsname = ""
        self.goodsgroup = ""
        self.deadline = ""
        self.volno1 = ""
        self.volno2 = ""
        self.processorname = ""
        self.chinesename = ""
        self.englishname = ""
        self.japanesename = ""
        self.address = ""
        self.countrycode = ""
        self.chinesecountryname = ""
        self.agentchinesename = ""
        self.agentaddress = ""
      
    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "tmarkcontent ":
            print ("tmarkcontent")
            sequence = attributes["sequence"]
            print ("sequence:", sequence)
            self.examno = ""
            self.applno = ""
            self.tmarkname = ""
            self.tmarkClassDesc = ""
            self.imagedata1 = ""
            self.imagedata2 = ""
            self.imagedata3 = ""
            self.imagedata4 = ""
            self.imagedata5 = ""
            self.imagedata6 = ""
            self.tmarktype = ""
            self.tmarktypedesc = ""
            self.tmarkcolor = ""
            self.tmarkcolordesc = ""
            self.tmarkdraftc = ""
            self.tmarkdrafte = ""
            self.tmarkdraftj = ""
            self.tmarksign = ""
            self.worddescription = ""
            self.goodsclasscode = ""
            self.goodsname = ""
            self.goodsgroup = ""
            self.deadline = ""
            self.volno1 = ""
            self.volno2 = ""
            self.processorname = ""
            self.chinesename = ""
            self.englishname = ""
            self.japanesename = ""
            self.address = ""
            self.countrycode = ""
            self.chinesecountryname = ""
            self.agentchinesename = ""
            self.agentaddress = ""
            
            """
            sqlStuff = "INSERT INTO ttable (indexNo, examNo, applNo, tmarkName, tmarkClassDesc, imageData1, imageData2, imageData3, imageData4, imageData5, imageData6, tmarkType, tmarkTypeDesc, tmarkColor, tmarkColorDesc, tmarkDraftC, tmarkDraftE, tmarkDraftJ, tmarkSign, wordDescription, goodsclassCode, goodsName, goodsGroup, deadline,volNo1, volNo2, processorName, holderChineseName, holderEnglishName, holderJapaneseName, holderAddress, countryCode, chineseCountryName, agentChineseName, agentAddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            records = [(str(index), str(examNo[0]), str(applNo[0]), str(tmarkName[0]), str(tmarkClassDesc[0]), path1[0], path2[0], path3[0], path4[0], path5[0], path6[0], str(tmarkType[0]), str(tmarkTypeDesc[0]), str(tmarkColor[0]), str(tmarkColorDesc[0]), str(tmarkDraftC[0]), str(tmarkDraftE[0]), str(tmarkDraftJ[0]), str(tmarkSign[0]), str(wordDescription[0]), newGoodsClassCode, str(goodsName[0]), str(goodsGroup[0]), deadline, str(volNo1[0]), str(volNo2[0]), str(processorName[0]), newHolderChineseName, newHolderEnglishName, newHolderJapaneseName, newHolderAddress, str(countryCode[0]), str(chineseCountryName[0]), newAgentChineseName, newAgentAddress),]
            #records = [(str(examNo[0]), str(applNo[0]), str(tmarkName[0]), str(tmarkClassDesc[0]), img1, img2, img3, img4, img5, img6, str(tmarkType[0]), str(tmarkTypeDesc[0]), str(tmarkColor[0]), str(tmarkColorDesc[0]), str(tmarkDraftC[0]), str(tmarkDraftE[0]), str(tmarkDraftJ[0]), str(tmarkSign[0]), str(wordDescription[0]), str(goodsclassCode[0]), str(goodsName[0]), str(goodsGroup[0]), deadline ,str(volNo1[0]), str(volNo2[0]), str(processorName[0]), str(holderChineseName[0]), str(holderEnglishName[0]), str(holderJapaneseName[0]), str(holderAddress[0]), str(countryCode[0]), str(chineseCountryName[0]), str(agentChineseName[0]), str(agentAddress[0])),]
            cursor.executemany(sqlStuff, records)
            tmarkdb.commit()
            """

    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "exam-no":
            print (examNo = self.examno)
        elif self.CurrentData == "appl-no":
            print (applNo = self.applno)
        elif self.CurrentData == "tmark-name":
           print (tmarkName = self.tmarkname)
        elif self.CurrentData == "tmark-class-desc":
           print (tmarkClassDesc = self.tmarkClassDesc)
        elif self.CurrentData == "image-data-1":
           print (imageData1 = self.imagedata1)
        elif self.CurrentData == "image-data-2":
           print (imageData2 = self.imagedata2)
        elif self.CurrentData == "image-data-3":
           print (imageData3 = self.imagedata3)
        elif self.CurrentData == "image-data-4":
           print (imageData4 = self.imagedata4)
        elif self.CurrentData == "image-data-5":
           print (imageData5 = self.imagedata5)
        elif self.CurrentData == "image-data-6":
           print (imageData6 = self.imagedata6)
        elif self.CurrentData == "tmark-type":
           print (tmarkType = self.tmarktype)
        elif self.CurrentData == "tmark-type-desc":
           print (tmarkTypeDesc = self.tmarktypedesc)
        elif self.CurrentData == "tmark-color":
           print (tmarkColor = self.tmarkcolor)
        elif self.CurrentData == "tmark-color-desc":
           print (tmarkColorDesc = self.tmarkcolordesc)
        elif self.CurrentData == "tmark-draft-c":
           print (tmarkDraftC = self.tmarkdraftc)
        elif self.CurrentData == "tmark-draft-e":
           print (tmarkDraftE = self.tmarkdrafte)
        elif self.CurrentData == "tmark-draft-j":
           print (tmarkDraftJ = self.tmarkdraftj)
        elif self.CurrentData == "tmark-sign":
           print (tmarkSign = self.tmarksign)
        elif self.CurrentData == "word-description":
           print (wordDescription = self.worddescription)
        elif self.CurrentData == "goodsclass-code":
           print (goodsclassCode = self.goodsclasscode)
        elif self.CurrentData == "goods-name":
           print (goodsName = self.goodsname)
        elif self.CurrentData == "goods-group":
           print (goodsGroup = self.goodsgroup)
        elif self.CurrentData == "deadline":
           print (deadline = self.deadline)
        elif self.CurrentData == "vol-no1":
           print (volNo1 = self.volno1)
        elif self.CurrentData == "vol-no2":
           print (volNo2 = self.volno2)
        elif self.CurrentData == "processor-name":
           print (processorName = self.processorname)
        elif self.CurrentData == "chinese-name":
           print (holderChineseName = self.chinesename)
        elif self.CurrentData == "english-name":
           print (holderEnglishName = self.englishname)
        elif self.CurrentData == "japanese-name":
           print (holderJapaneseName = self.japanesename)
        elif self.CurrentData == "address":
           print (holderAddress = self.address)
        elif self.CurrentData == "country-code ":
           print (countryCode = self.countrycode )
        elif self.CurrentData == "chinese-country-name":
           print (chineseCountryName = self.chinesecountryname)
        elif self.CurrentData == "agent-chinese-name":
           print (agentChineseName = self.agentchinesename)
        elif self.CurrentData == "agent-address":
           print (agentAddress = self.agentaddress)
           

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "exam-no":
             self.examno = content
        elif self.CurrentData == "appl-no":
             self.applno = content
        elif self.CurrentData == "tmark-name":
            self.tmarkname = content            
        elif self.CurrentData == "tmark-class-desc":
            self.tmarkClassDesc = content
        elif self.CurrentData == "image-data-1":
            self.imagedata1 = content
        elif self.CurrentData == "image-data-2":
            self.imagedata2 = content
        elif self.CurrentData == "image-data-3":
            self.imagedata3 = content
        elif self.CurrentData == "image-data-4":
            self.imagedata4 = content
        elif self.CurrentData == "image-data-5":
            self.imagedata5 = content
        elif self.CurrentData == "image-data-6":
            self.imagedata6 = content            
        elif self.CurrentData == "tmark-type":
            self.tmarktype  = content
        elif self.CurrentData == "tmark-type-desc":
            self.tmarktypedesc = content
        elif self.CurrentData == "mark-color":
            self.tmarkcolor = content
        elif self.CurrentData == "tmark-color-desc":
            self.tmarkcolordesc = content
        elif self.CurrentData == "tmark-draft-c":
            self.tmarkdraftc = content
        elif self.CurrentData == "tmark-draft-e":
            self.tmarkdrafte = content
        elif self.CurrentData == "tmark-draft-j":
            self.tmarkdraftj = content            
        elif self.CurrentData == "tmark-sign":
            self.tmarksign = content
        elif self.CurrentData == "word-description":
            self.worddescription= content
        elif self.CurrentData == "goodsclass-code":
            self.goodsclasscode   = content
        elif self.CurrentData == "goods-name":
            self.goodsname = content
        elif self.CurrentData == "goods-group":
           self.goodsgroup = content
        elif self.CurrentData == "deadline":
           self.deadline = content
        elif self.CurrentData == "vol-no1":
           self.volno1 = content
        elif self.CurrentData == "vol-no2":
           self.volno2 = content
        elif self.CurrentData == "processor-name":
           self.processorname = content
        elif self.CurrentData == "chinese-name":
           self.chinesename = content
        elif self.CurrentData == "english-name":
           self.englishname = content
        elif self.CurrentData == "japanese-name":
           self.japanesename = content
        elif self.CurrentData == "address":
           self.address = content
        elif self.CurrentData == "country-code ":
           self.countrycode  = content
        elif self.CurrentData == "chinese-country-name":
           self.chinesecountryname = content
        elif self.CurrentData == "agent-chinese-name":
           self.agentchinesename = content
        elif self.CurrentData == "agent-address":
           self.agentaddress = content
           

url = 'https://tiponet.tipo.gov.tw/OpenDataApi/OpenData/API/TmarkRights?format=xml&top=5&skip=8896&orderby=appl-no&tk=ywgvRgZ1'

r = requests.get(url, verify=False)
soup = BeautifulSoup(r.text, 'html.parser')
f = open("./tmark.xml",'w',encoding="utf-8")
f.write(str(soup))

fopen=open("./tmark.xml",'r',encoding="utf-8")
lineNo = 0
changeNo=0
wopen=open("./tmark2.xml",'w',encoding="utf-8")
wopen.write("")
wopen.close()

w_str=""
for line in fopen:
    lineNo = lineNo +1
    if re.search('agent sequence',line) and changeNo == 0:
        changeNo = 1
        wopen=open("./tmark2.xml",'a',encoding="utf-8")
        wopen.write(line)
    elif re.search('tmarkcontent',line):
        changeNo = 0
        wopen=open("./tmark2.xml",'a',encoding="utf-8")
        wopen.write(line)
    elif re.search('chinese-name',line) and changeNo == 1:
        line=re.sub('chinese-name','agent-chinese-name',line)
        wopen=open("./tmark2.xml",'a',encoding="utf-8")
        wopen.write(line)
    elif re.search('address',line) and changeNo == 1:
        line=re.sub('address','agent-address',line)
        wopen=open("./tmark2.xml",'a',encoding="utf-8")
        wopen.write(line)
    else:
        wopen=open("./tmark2.xml",'a',encoding="utf-8")
        wopen.write(line)
fopen.close()
wopen.close()   

if ( __name__ == "__main__"):
   # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 重写 ContextHandler
    Handler = tmarkHandler()
    parser.setContentHandler( Handler )
    parser.parse("./tmark2.xml")
   
    print ("====================================================")