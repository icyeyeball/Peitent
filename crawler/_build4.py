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
deadlindIndex=0

class tmarkHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.examno = ""
        self.applno = ""
        self.examno2 = ""
        self.applno2 = ""
        self.applno3 = ""
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
        self.deadline2 = ""
        self.deadline3 = ""
        self.deadline4 = ""
        self.deadline5 = ""
        self.deadline6 = ""
        self.deadline7 = ""
        self.deadline8 = ""
        self.deadline9 = ""
        self.deadline10 = ""
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
        self.appldate = ""
        self.regdate = ""
        self.regnoticedate = ""
        self.examnoticedate = ""
        self.delreason = ""
        self.examstatus = ""
        self.extendedstatus = ""
        
        self.oppositionstatus = ""
        self.nullityactstatus = ""
        self.appldelstatus = ""
        self.autstatus = ""
        self.agaautstatus = ""
        self.amedmentstatus = ""
        self.transferstatus = ""
        self.issueoppstatus = ""
        self.issuedelstatus = ""
        self.quotastatus = ""
        self.unableusestatus = ""
    # Element start
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "tmarkcontent ":
            #print ("tmarkcontent")
            sequence = attributes["sequence"]
            #print ("sequence:", sequence)
            self.examno = ""
            self.applno = ""
            self.examno2 = ""
            self.applno2 = ""
            self.applno3 = ""
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
            self.deadline2 = ""
            self.deadline3 = ""
            self.deadline4 = ""
            self.deadline5 = ""
            self.deadline6 = ""
            self.deadline7 = ""
            self.deadline8 = ""
            self.deadline9 = ""
            self.deadline10 = ""
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
            self.appldate = ""
            self.regdate = ""
            self.regnoticedate = ""
            self.examnoticedate = ""
            self.delreason = ""
            self.examstatus = ""
            self.extendedstatus = ""
            
            self.oppositionstatus = ""
            self.nullityactstatus = ""
            self.appldelstatus = ""
            self.autstatus = ""
            self.agaautstatus = ""
            self.amedmentstatus = ""
            self.transferstatus = ""
            self.issueoppstatus = ""
            self.issuedelstatus = ""
            self.quotastatus = ""
            self.unableusestatus = ""

    # Element end
    def endElement(self, tag):
        global exNo
        global appNo
        if self.CurrentData == "exam-no":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write('end')
                f.write('\n')
                f.write('start')
                f.write('\n')
                f.write("examNo =" +  self.examno)
                f.write('\n')
                if len(self.examno2) == 8:
                    exNo = self.examno2
        elif self.CurrentData == "exam2-no":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("exam2No =" +  self.examno2)
                f.write('\n')
                if len(self.examno2) == 8:
                    exNo = self.examno2
                else:
                    exNo = '00000000'
        elif self.CurrentData == "appl-no":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("applNo =" +  self.applno)
                f.write('\n')
                if len(self.applno) == 9:
                    appNo = self.applno
        elif self.CurrentData == "appl2-no":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("appl2No =" +  self.applno2)
                f.write('\n')
                if len(self.applno2) == 9:
                    appNo = self.applno2
        elif self.CurrentData == "appl3-no":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("appl3No =" +  self.applno3)
                f.write('\n')
                if len(self.applno3) == 9:
                    appNo = self.applno3
                else:
                    appNo = '000000000'
        elif self.CurrentData == "tmark-name":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("tmarkName =" +  self.tmarkname)
                f.write('\n')
        elif self.CurrentData == "tmark-class-desc":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("tmarkClassDesc =" +  self.tmarkClassDesc)
                f.write('\n')
        elif self.CurrentData == "image-data-1":
            if self.imagedata1.startswith('http') == False:
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData1 =" +  "")
                    f.write('\n')
                    f.write("img_url1 =" +  "")
                    f.write('\n')
            else:
                img_url1 = self.imagedata1.replace(u'jpgformatName', u'jpg&formatName')
                img_url1 = img_url1.replace(u'jpegpath', u'jpg&path')
                path = './picBase/'+str(appNo)+'-1.png'
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData1 =" +  path)
                    f.write('\n')
                    f.write("img_url1 =" +  img_url1)
                    f.write('\n')
        elif self.CurrentData == "image-data-2":
            if self.imagedata2.startswith('http') == False:
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData2 =" +  "")
                    f.write('\n')
                    f.write("img_url2 =" +  "")
                    f.write('\n')
            else:
                img_url2 = self.imagedata2.replace(u'jpgformatName', u'jpg&formatName')
                img_url2 = img_url2.replace(u'jpegpath', u'jpg&path')
                path = './picBase/'+str(exNo)+'-2.png'
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData2 =" +  path)
                    f.write('\n')
                    f.write("img_url2 =" +  img_url2)
                    f.write('\n')
        elif self.CurrentData == "image-data-3":
            if self.imagedata3.startswith('http') == False:
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData3 =" +  "")
                    f.write('\n')
                    f.write("img_url3 =" +  "")
                    f.write('\n')
            else:
                img_url3 = self.imagedata3.replace(u'jpgformatName', u'jpg&formatName')
                img_url3 = img_url3.replace(u'jpegpath', u'jpg&path')
                path = './picBase/'+str(exNo)+'-3.png'
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData3 =" +  path)
                    f.write('\n')
                    f.write("img_url3 =" +  img_url3)
                    f.write('\n')
        elif self.CurrentData == "image-data-4":
            if self.imagedata4.startswith('http') == False:
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData4 =" +  "")
                    f.write('\n')
                    f.write("img_url4 =" +  "")
                    f.write('\n')
            else:
                img_url4 = self.imagedata4.replace(u'jpgformatName', u'jpg&formatName')
                img_url4 = img_url4.replace(u'jpegpath', u'jpg&path')
                path = './picBase/'+str(exNo)+'-4.png'
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData4 =" +  path)
                    f.write('\n')
                    f.write("img_url4 =" +  img_url4)
                    f.write('\n')
        elif self.CurrentData == "image-data-5":
            if self.imagedata5.startswith('http') == False:
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData5 =" +  "")
                    f.write('\n')
                    f.write("img_url5 =" +  "")
                    f.write('\n')
            else:
                img_url5 = self.imagedata5.replace(u'jpgformatName', u'jpg&formatName')
                img_url5 = img_url5.replace(u'jpegpath', u'jpg&path')
                path = './picBase/'+str(exNo)+'-5.png'
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData5 =" +  path)
                    f.write('\n')
                    f.write("img_url5 =" +  img_url5)
                    f.write('\n')
        elif self.CurrentData == "image-data-6":
            if self.imagedata6.startswith('http') == False:
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData6 =" +  "")
                    f.write('\n')
                    f.write("img_url6 =" +  "")
                    f.write('\n')
            else:
                img_url6 = self.imagedata6.replace(u'jpgformatName', u'jpg&formatName')
                img_url6 = img_url6.replace(u'jpegpath', u'jpg&path')
                path = './picBase/'+str(exNo)+'-6.png'
                with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                    f.write("imageData6 =" +  path)
                    f.write('\n')
                    f.write("img_url6 =" +  img_url6)
                    f.write('\n')
        elif self.CurrentData == "tmark-type":
            self.tmarktype.strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("tmarkType =" +  self.tmarktype)
                f.write('\n')
        elif self.CurrentData == "tmark-type-desc":
            self.tmarktypedesc.strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("ttmarkTypeDesc =" +  self.tmarktypedesc)
                f.write('\n')
        elif self.CurrentData == "tmark-color":
            self.tmarkcolor.strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("tmarkColor =" +  self.tmarkcolor)
                f.write('\n')
        elif self.CurrentData == "tmark-color-desc":
            self.tmarkcolordesc.strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("ttmarkColorDesc =" +  self.tmarkcolordesc)
                f.write('\n')
        elif self.CurrentData == "tmark-draft-c":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("tmarkDraftC =" +  self.tmarkdraftc)
                f.write('\n')
        elif self.CurrentData == "tmark-draft-e":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("tmarkDraftE =" +  self.tmarkdrafte)
                f.write('\n')
        elif self.CurrentData == "tmark-draft-j":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("tmarkDraftJ =" +  self.tmarkdraftj)
                f.write('\n')
        elif self.CurrentData == "tmark-sign":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("tmarkSign =" +  self.tmarksign)
                f.write('\n')
        elif self.CurrentData == "word-description":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("wordDescription =" +  self.worddescription)
                f.write('\n')
        elif self.CurrentData == "goodsclass-code":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("goodsclassCode =" +  self.goodsclasscode)
                f.write('\n')
        elif self.CurrentData == "goods-name":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("goodsName =" +  self.goodsname)
                f.write('\n')
        elif self.CurrentData == "goods-group":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("goodsGroup =" +  self.goodsgroup)
                f.write('\n')
        elif self.CurrentData == "deadline":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("deadline =" +  self.deadline)
                f.write('\n')
        elif self.CurrentData == "dead2line":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("dead2line =" +  self.deadline2)
                f.write('\n')
        elif self.CurrentData == "dead3line":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("dead3line =" +  self.deadline3)
                f.write('\n')
        elif self.CurrentData == "dead4line":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("dead4line =" +  self.deadline4)
                f.write('\n')
        elif self.CurrentData == "dead5line":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("dead5line =" +  self.deadline5)
                f.write('\n')
        elif self.CurrentData == "dead6line":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("dead6line =" +  self.deadline6)
                f.write('\n')
        elif self.CurrentData == "dead7line":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("dead7line =" +  self.deadline7)
                f.write('\n')
        elif self.CurrentData == "dead8line":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("dead8line =" +  self.deadline8)
                f.write('\n')
        elif self.CurrentData == "dead9line":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("dead9line =" +  self.deadline9)
                f.write('\n')
        elif self.CurrentData == "dead10line":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("dead10line =" +  self.deadline10)
                f.write('\n')
        elif self.CurrentData == "vol-no1":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("volNo1 =" +  self.volno1)
                f.write('\n')
        elif self.CurrentData == "vol-no2":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("volNo2 =" +  self.volno2)
                f.write('\n')
        elif self.CurrentData == "processor-name":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("processorName =" + self.processorname)
                f.write('\n')
        elif self.CurrentData == "chinese-name":
            self.chinesename.strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("holderChineseName =" + self.chinesename)
                f.write('\n')
        elif self.CurrentData == "english-name":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("holderEnglishName =" + self.englishname)
                f.write('\n')
        elif self.CurrentData == "japanese-name":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("holderJapaneseName =" + self.japanesename)
                f.write('\n')
        elif self.CurrentData == "address":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("holderAddress =" + self.address)
                f.write('\n')
        elif self.CurrentData == "country-code":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("countryCode =" + self.countrycode)
                f.write('\n')
        elif self.CurrentData == "chinese-country-name":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("chineseCountryName =" + self.chinesecountryname)
                f.write('\n')
        elif self.CurrentData == "agent-chinese-name":
            self.agentchinesename.strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("agentChineseName =" + self.agentchinesename)
                f.write('\n')
        elif self.CurrentData == "agent-address":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("agentAddress =" + self.agentaddress)
                f.write('\n')
        elif self.CurrentData == "appl-date":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("applDate =" + self.appldate)
                f.write('\n')
        elif self.CurrentData == "reg-date":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("regDate =" + self.regdate)
                f.write('\n')   
        elif self.CurrentData == "reg-notice-date":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("regNoticeDate =" + self.regnoticedate)
                f.write('\n')
        elif self.CurrentData == "exam-notice-date":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("_examNoticeDate =" + self.examnoticedate)
                f.write('\n')
        elif self.CurrentData == "del-reason":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("delReason =" + self.delreason)
                f.write('\n')
        elif self.CurrentData == "exam-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("examStatus =" + self.examstatus)
                f.write('\n')
        elif self.CurrentData == "extended-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("extendedStatus =" + self.extendedstatus)
                f.write('\n')
        elif self.CurrentData == "opposition-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("oppositionStatus =" + self.oppositionstatus)
                f.write('\n')
        elif self.CurrentData == "nullity-act-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("nullityActStatus =" + self.nullityactstatus)
                f.write('\n')
        elif self.CurrentData == "appl-del-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("applDelStatus =" + self.appldelstatus)
                f.write('\n')
        elif self.CurrentData == "aut-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("autStatus =" + self.autstatus)
                f.write('\n')
        elif self.CurrentData == "aga-aut-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("agaAutStatus =" + self.agaautstatus)
                f.write('\n')
        elif self.CurrentData == "amedment-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("amedmentStatus =" + self.amedmentstatus)
                f.write('\n')
        elif self.CurrentData == "transfer-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("transferStatus =" + self.transferstatus)
                f.write('\n')
        elif self.CurrentData == "issue-opp-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("issueOppStatus =" + self.issueoppstatus)
                f.write('\n')
        elif self.CurrentData == "issue-del-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("issueDelStatus =" + self.issuedelstatus)
                f.write('\n')
        elif self.CurrentData == "quota-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("quotaStatus =" + self.quotastatus)
                f.write('\n')
        elif self.CurrentData == "unable-use-status":
            with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
                f.write("unableUseStatus =" + self.unableusestatus)
                f.write('\n')

    # 內容事件處理
    def characters(self, content):
        if self.CurrentData == "exam-no":
             self.examno = content
        elif self.CurrentData == "exam2-no":
             self.examno2 = content
        elif self.CurrentData == "appl-no":
             self.applno = content
        elif self.CurrentData == "appl2-no":
             self.applno2 = content
        elif self.CurrentData == "appl3-no":
             self.applno3 = content
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
        elif self.CurrentData == "dead2line":
           self.deadline2 = content
        elif self.CurrentData == "dead3line":
           self.deadline3 = content
        elif self.CurrentData == "dead4line":
           self.deadline4 = content
        elif self.CurrentData == "dead5line":
           self.deadline5 = content
        elif self.CurrentData == "dead6line":
           self.deadline6 = content
        elif self.CurrentData == "dead7line":
           self.deadline7 = content
        elif self.CurrentData == "dead8line":
           self.deadline8 = content
        elif self.CurrentData == "dead9line":
           self.deadline9 = content
        elif self.CurrentData == "dead10line":
           self.deadline10 = content
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
        elif self.CurrentData == "country-code":
           self.countrycode  = content
        elif self.CurrentData == "chinese-country-name":
           self.chinesecountryname = content
        elif self.CurrentData == "agent-chinese-name":
           self.agentchinesename = content
        elif self.CurrentData == "agent-address":
           self.agentaddress = content
        elif self.CurrentData == "appl-date":
           self.appldate = content
        elif self.CurrentData == "reg-date":
           self.regdate = content
        elif self.CurrentData == "reg-notice-date":
           self.regnoticedate = content
        elif self.CurrentData == "exam-notice-date":
           self.examnoticedate = content
        elif self.CurrentData == "del-reason":
           self.delreason = content
        elif self.CurrentData == "exam-status":
           self.examstatus = content
        elif self.CurrentData == "extended-status":
           self.extendedstatus = content
        elif self.CurrentData == "opposition-status":
           self.oppositionstatus = content
        elif self.CurrentData == "nullity-act-status":
           self.nullityactstatus = content
        elif self.CurrentData == "appl-del-status":
           self.appldelstatus = content
        elif self.CurrentData == "aut-status":
           self.autstatus = content
        elif self.CurrentData == "aga-aut-status":
           self.agaautstatus = content
        elif self.CurrentData == "amedment-status":
           self.amedmentstatus = content
        elif self.CurrentData == "transfer-status":
           self.transferstatus = content
        elif self.CurrentData == "issue-opp-status":
           self.issueoppstatus = content
        elif self.CurrentData == "issue-del-status":
           self.issuedelstatus = content
        elif self.CurrentData == "quota-status":
           self.quotastatus = content
        elif self.CurrentData == "unable-use-status":
           self.unableusestatus = content
           
for index in range(224519, 2500000,400):
    url = 'https://tiponet.tipo.gov.tw/OpenDataApi/OpenData/API/TmarkRights?format=xml&top=400&skip='+str(index)+'&orderby=appl-no&tk=ywgvRgZ1'
    #url = 'https://tiponet.tipo.gov.tw/OpenDataApi/OpenData/API/TmarkRights?format=xml&top=100&skip=7485&orderby=appl-no&tk=ywgvRgZ1'
    
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    f = open("./tmark.xml",'w',encoding="utf-8")
    f.write(str(soup))

    wopen=open("./tmark2.xml",'w',encoding="utf-8")
    wopen.write("")
    wopen.close()

    wopen=open("./parsed.txt",'w',encoding="utf-8")
    wopen.write("")
    wopen.close()
    
    fopen=open("./tmark.xml",'r',encoding="utf-8")
    changeNo=0

    w_str=""
    for line in fopen:
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
        elif re.search('exam-no',line) and changeNo == 0:
            wopen=open("./tmark2.xml",'a',encoding="utf-8")
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('exam-no','exam2-no',line)
            wopen.write(line)
            wopen.write('\n')
        elif re.search('appl-no',line)  and changeNo == 0:
            wopen=open("./tmark2.xml",'a',encoding="utf-8")
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('appl-no','appl2-no',line)
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('appl2-no','appl3-no',line)
            wopen.write(line)
            wopen.write('\n')
        elif re.search('deadline',line):
            wopen=open("./tmark2.xml",'a',encoding="utf-8")
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('deadline','dead2line',line)
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('dead2line','dead3line',line)
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('dead3line','dead4line',line)
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('dead4line','dead5line',line)
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('dead5line','dead6line',line)
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('dead6line','dead7line',line)
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('dead7line','dead8line  ',line)
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('dead8line','dead9line',line)
            wopen.write(line)
            wopen.write('\n')
            line=re.sub('dead9line','dead10line',line)
            wopen.write(line)
        elif re.search('&amp;',line):
            line=re.sub('&amp;','',line)
            wopen=open("./tmark2.xml",'a',encoding="utf-8")
            wopen.write(line)
        else:
            wopen=open("./tmark2.xml",'a',encoding="utf-8")
            wopen.write(line)
    fopen.close()
    wopen.close()   

    if ( __name__ == "__main__"):
       # Create a XMLReader
        parser = xml.sax.make_parser()
        # turn off namepsaces
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        # rewrite ContextHandler
        Handler = tmarkHandler()
        parser.setContentHandler( Handler )
        parser.parse("./tmark2.xml")
        
        deadlindIndex=0
        eleNo = 0
        examNo_l = []
        applNo_l = []
        tmarkName_l = []
        tmarkClassDesc_l = []
        imageData1_l = []
        imageData2_l = []
        imageData3_l = []
        imageData4_l = []
        imageData5_l = []
        imageData6_l = []
        
        img_url1_l = []
        img_url2_l = []
        img_url3_l = []
        img_url4_l = []
        img_url5_l = []
        img_url6_l = []
        
        tmarkType_l = []
        tmarkTypeDesc_l = []
        tmarkColor_l = []
        tmarkColorDesc_l = []
        tmarkDraftC_l = []
        tmarkDraftE_l = []
        tmarkDraftJ_l = []
        tmarkSign_l = []
        wordDescription_l = []
        goodsclassCode_l = []
        goodsName_l = []
        goodsGroup_l = []
        deadline_l = []
        volNo1_l = []
        volNo2_l = []
        processorName_l = []
        holderChineseName_l = []
        holderEnglishName_l = []
        holderJapaneseName_l = []
        holderAddress_l = []
        countryCode_l = []
        chineseCountryName_l = []
        agentChineseName_l = []
        agentAddress_l = []
        applDate_l = []
        regDate_l = []
        regNoticeDate_l = []
        examNoticeDate_l = []
        delReason_l = []
        examStatus_l = []
        extendedStatus_l = []
        oppositionStatus_l = []
        nullityActStatus_l = []
        applDelStatus_l = []
        autStatus_l = []
        agaAutStatus_l = []
        amedmentStatus_l = []
        transferStatus_l = []
        issueOppStatus_l = []
        issueDelStatus_l = []
        quotaStatus_l = []
        unableUseStatus_l = []
        

        examindex=0
        applindex=0
        eleNo = 0
        deadlindIndex=0
        with open ("./parsed.txt",'a',encoding = 'utf-8') as f:
            f.write('end')
            f.write('\n')
        with open ("./parsed.txt",'r',encoding = 'utf-8') as f2:
            lines = f2.readlines()
            for line in lines:

                if line.startswith('start') == True:
                    deadlindIndex=0
                    eleNo = 1
                    goodsclassCodel = ""
                    goodsNamel = ""
                    goodsGroupl = ""
                    holderChineseNamel = ""
                    holderEnglishNamel = ""
                    holderJapaneseNamel = ""
                    holderAddressl = ""
                    agentChineseNamel = ""
                    agentAddressl = ""
                    tmarkTypel = ""
                    tmarkTypeDescl = ""
                    tmarkColorl = ""
                    tmarkColorDescl = ""
                    countryCodel  =""
                    chineseCountryNamel = ""
                    
                    
                elif line.startswith('examNo') == True and eleNo == 1:
                    if len(line.strip().replace(u'examNo =', u'')) == 8:
                        examNo_l.append(str(line.strip().replace(u'examNo =', u'')) + "")
                        examindex = 1
                    else:
                        examindex = 0
                elif line.startswith('exam2No') == True and eleNo == 1 and examindex ==0:
                    if len(line.strip().replace(u'exam2No =', u'')) == 8:
                        examNo_l.append(str(line.strip().replace(u'exam2No =', u'')) + "")
                    else:
                        examNo_l.append("00000000")

                    
                elif line.startswith('applNo') == True and eleNo == 1:
                    if len(line.strip().replace(u'applNo =', u'')) == 9:
                        applNo_l.append(str(line.strip().replace(u'applNo =', u'')) + "")
                        applindex = 1
                    else:
                        applindex = 0
                elif line.startswith('appl2No') == True and eleNo == 1 and applindex == 0:
                    if len(line.strip().replace(u'appl2No =', u'')) == 9:
                        applNo_l.append(str(line.strip().replace(u'appl2No =', u'')) + "")
                        applindex = 1
                    else:
                        applindex = 0
                elif line.startswith('appl3No') == True and eleNo == 1 and applindex ==0:
                    if len(line.strip().replace(u'appl3No =', u'')) == 9:
                        applNo_l.append(str(line.strip().replace(u'appl3No =', u'')) + "")
                    else:
                        applNo_l.append("000000000")

   
                    
                elif line.startswith('tmarkName') == True and eleNo == 1:
                    tmarkName_l.append(str(line.strip().replace(u'tmarkName =', u'')) + "")
                elif line.startswith('tmarkClassDesc') == True and eleNo == 1:
                    tmarkClassDesc_l.append(str(line.strip().replace(u'tmarkClassDesc =', u'')) + "")
                    
                elif line.startswith('imageData1') == True and eleNo == 1:
                    imageData1_l.append(str(line.strip().replace(u'imageData1 =', u'')) + "")
       
                elif line.startswith('img_url1') == True and eleNo == 1:
                    img_url1_l.append(str(line.strip().replace(u'img_url1 =', u'')) + "")
                        
                elif line.startswith('imageData2') == True and eleNo == 1:
                    imageData2_l.append(str(line.strip().replace(u'imageData2 =', u'')) + "")
                elif line.startswith('img_url2') == True and eleNo == 1:
                        img_url2_l.append(str(line.strip().replace(u'img_url2 =', u'')) + "")
                elif line.startswith('imageData3') == True and eleNo == 1:
                    imageData3_l.append(str(line.strip().replace(u'imageData3 =', u'')) + "")
                elif line.startswith('img_url3') == True and eleNo == 1:
                    img_url3_l.append(str(line.strip().replace(u'img_url3 =', u'')) + "")
                elif line.startswith('imageData4') == True and eleNo == 1:
                    imageData4_l.append(str(line.strip().replace(u'imageData4 =', u'')) + "")
                elif line.startswith('img_url4') == True and eleNo == 1:
                    img_url4_l.append(str(line.strip().replace(u'img_url4 =', u'')) + "")
                elif line.startswith('imageData5') == True and eleNo == 1:
                    imageData5_l.append(str(line.strip().replace(u'imageData5 =', u'')) + "")
                elif line.startswith('img_url5') == True and eleNo == 1:
                    img_url5_l.append(str(line.strip().replace(u'img_url5 =', u'')) + "")
                elif line.startswith('imageData6') == True and eleNo == 1:
                    imageData6_l.append(str(line.strip().replace(u'imageData6 =', u'')) + "")
                elif line.startswith('img_url6') == True and eleNo == 1:
                    img_url6_l.append(str(line.strip().replace(u'img_url6 =', u'')) + "")
                elif line.startswith('tmarkType') == True and eleNo == 1:
                    tmarkTypel = tmarkTypel + str(line.strip().replace(u'tmarkType =', u'')) + " "
                elif line.startswith('ttmarkTypeDesc') == True and eleNo == 1:
                    tmarkTypeDescl = tmarkTypeDescl + str(line.strip().replace(u'ttmarkTypeDesc =', u'')) + " "
                elif line.startswith('tmarkColor') == True and eleNo == 1:
                    tmarkColorl = tmarkColorl + str(line.strip().replace(u'tmarkColor =', u'')) + " "
                elif line.startswith('ttmarkColorDesc') == True and eleNo == 1:
                    tmarkColorDescl = tmarkColorDescl + str(line.strip().replace(u'ttmarkColorDesc =', u'')) + " "
                elif line.startswith('tmarkDraftC') == True and eleNo == 1:
                    tmarkDraftC_l.append(str(line.strip().replace(u'tmarkDraftC =', u'')) + "")
                elif line.startswith('tmarkDraftE') == True and eleNo == 1:
                    tmarkDraftE_l.append(str(line.strip().replace(u'tmarkDraftE =', u'')) + "")
                elif line.startswith('tmarkDraftJ') == True and eleNo == 1:
                    tmarkDraftJ_l.append(str(line.strip().replace(u'tmarkDraftJ =', u'')) + "")
                elif line.startswith('tmarkSign') == True and eleNo == 1:
                    tmarkSign_l.append(str(line.strip().replace(u'tmarkSign =', u'')) + "")
                elif line.startswith('wordDescription') == True and eleNo == 1:
                    wordDescription_l.append(str(line.strip().replace(u'wordDescription =', u'')) + "")
                elif line.startswith('goodsclassCode') == True and eleNo == 1:
                    goodsclassCodel = goodsclassCodel + str(line.strip().replace(u'goodsclassCode =', u'')) + " "
                elif line.startswith('goodsName') == True and eleNo == 1:
                    goodsNamel = goodsNamel + str(line.strip().replace(u'goodsName =', u'')) + " "
                elif line.startswith('goodsGroup') == True and eleNo == 1:
                    goodsGroupl = goodsGroupl + str(line.strip().replace(u'goodsGroup =', u'')) + " "
                elif line.startswith('deadline') == True and eleNo == 1 and len(line.strip().replace(u'deadline =', u'')) == 10:
                    deadline_l.append(str(line.strip().replace(u'deadline =', u'')) + "")
                    deadlindIndex = 1
                elif line.startswith('dead2line') == True and eleNo == 1 and deadlindIndex==0 and len(line.strip().replace(u'dead2line =', u'')) == 10:
                    deadline_l.append(str(line.strip().replace(u'dead2line =', u'')) + "")
                    with open ("./deadline.txt",'a',encoding = 'utf-8') as f:
                        f.write("======2======")
                        f.write('\n')
                    deadlindIndex = 1
                elif line.startswith('dead3line') == True and eleNo == 1 and deadlindIndex==0 and len(line.strip().replace(u'dead3line =', u'')) == 10:
                    deadline_l.append(str(line.strip().replace(u'dead3line =', u'')) + "")
                    with open ("./deadline.txt",'a',encoding = 'utf-8') as f:
                        f.write("======3======")
                        f.write('\n')
                    deadlindIndex = 1
                elif line.startswith('dead4line') == True and eleNo == 1 and deadlindIndex==0 and len(line.strip().replace(u'dead4line =', u'')) == 10:
                    deadline_l.append(str(line.strip().replace(u'dead4line =', u'')) + "")
                    with open ("./deadline.txt",'a',encoding = 'utf-8') as f:
                        f.write("======4======")
                        f.write('\n')
                    deadlindIndex = 1
                elif line.startswith('dead5line') == True and eleNo == 1 and deadlindIndex==0 and len(line.strip().replace(u'dead5line =', u'')) == 10:
                    deadline_l.append(str(line.strip().replace(u'dead5line =', u'')) + "")
                    with open ("./deadline.txt",'a',encoding = 'utf-8') as f:
                        f.write("======5======")
                        f.write('\n')
                    deadlindIndex = 1
                elif line.startswith('dead6line') == True and eleNo == 1 and deadlindIndex==0 and len(line.strip().replace(u'dead6line =', u'')) == 10:
                    deadline_l.append(str(line.strip().replace(u'dead6line =', u'')) + "")
                    with open ("./deadline.txt",'a',encoding = 'utf-8') as f:
                        f.write("======6======")
                        f.write('\n')
                    deadlindIndex = 1
                elif line.startswith('dead7line') == True and eleNo == 1 and deadlindIndex==0 and len(line.strip().replace(u'dead7line =', u'')) == 10:
                    deadline_l.append(str(line.strip().replace(u'dead7line =', u'')) + "")
                    with open ("./deadline.txt",'a',encoding = 'utf-8') as f:
                        f.write("======7======")
                        f.write('\n')
                    deadlindIndex = 1
                elif line.startswith('dead8line') == True and eleNo == 1 and deadlindIndex==0 and len(line.strip().replace(u'dead8line =', u'')) == 10:
                    deadline_l.append(str(line.strip().replace(u'dead8line =', u'')) + "")
                    with open ("./deadline.txt",'a',encoding = 'utf-8') as f:
                        f.write("======8======")
                        f.write('\n')
                    deadlindIndex = 1
                elif line.startswith('dead9line') == True and eleNo == 1 and deadlindIndex==0 and len(line.strip().replace(u'dead9line =', u'')) == 10:
                    deadline_l.append(str(line.strip().replace(u'dead9line =', u'')) + "")
                    with open ("./deadline.txt",'a',encoding = 'utf-8') as f:
                        f.write("======9======")
                        f.write('\n')
                    deadlindIndex = 1
                elif line.startswith('dead10line') == True and eleNo == 1 and deadlindIndex==0:
                    if len(str(line.strip().replace(u'dead10line =', u'')) + "") == 10:
                        deadline_l.append(str(line.strip().replace(u'dead10line =', u'')) + "")
                        with open ("./deadline.txt",'a',encoding = 'utf-8') as f:
                            f.write('\n')
                    else:
                        deadline_l.append("1900/01/01")
                elif line.startswith('volNo1') == True and eleNo == 1:
                    volNo1_l.append(str(line.strip().replace(u'volNo1 =', u'')) + "")
                elif line.startswith('volNo2') == True and eleNo == 1:
                    volNo2_l.append(str(line.strip().replace(u'volNo2 =', u'')) + "")
                elif line.startswith('processorName') == True and eleNo == 1:
                    processorName_l.append(str(line.strip().replace(u'processorName =', u'')) + "")
                elif line.startswith('imageData2l') == True and eleNo == 1:
                    processorName_l.append(str(line.strip().replace(u'processorName =', u'')) + "")
                elif line.startswith('holderChineseName') == True and eleNo == 1:
                    holderChineseNamel = holderChineseNamel + str(line.strip().replace(u'holderChineseName =', u'')) + " "
                elif line.startswith('holderEnglishName') == True and eleNo == 1:
                    holderEnglishNamel = holderEnglishNamel + str(line.strip().replace(u'holderEnglishName =', u'')) + " "
                elif line.startswith('holderJapaneseName') == True and eleNo == 1:
                    holderJapaneseNamel = holderJapaneseNamel + str(line.strip().replace(u'holderJapaneseName =', u'')) + " "
                elif line.startswith('holderAddress') == True and eleNo == 1:
                    holderAddressl = holderAddressl + str(line.strip().replace(u'holderAddress =', u'')) + " "
                elif line.startswith('countryCode') == True and eleNo == 1:
                    countryCodel = countryCodel + str(line.strip().replace(u'countryCode =', u'')) + " "
                elif line.startswith('chineseCountryName') == True and eleNo == 1:
                    chineseCountryNamel = chineseCountryNamel + str(line.strip().replace(u'chineseCountryName =', u'')) + " "
                elif line.startswith('agentChineseName') == True and eleNo == 1:
                    agentChineseNamel = agentChineseNamel + str(line.strip().replace(u'agentChineseName =', u'')) + " "
                elif line.startswith('agentAddress') == True and eleNo == 1:
                    agentAddressl = agentAddressl + str(line.strip().replace(u'agentAddress =', u'')) + " "
                elif line.startswith('applDate') == True and eleNo == 1:
                    if len(line.strip().replace(u'applDate =', u'')) == 10:
                        applDate_l.append(str(line.strip().replace(u'applDate =', u'')) + "")
                    else:
                        applDate_l.append("1900/01/01")
                elif line.startswith('regDate') == True and eleNo == 1:
                    if len(line.strip().replace(u'regDate =', u'')) == 10:
                        regDate_l.append(str(line.strip().replace(u'regDate =', u'')) + "")
                    else:
                        regDate_l.append("1900/01/01")
                elif line.startswith('regNoticeDate') == True and eleNo == 1:
                    if len(line.strip().replace(u'regNoticeDate =', u'')) == 10:
                        regNoticeDate_l.append(str(line.strip().replace(u'regNoticeDate =', u'')) + "")
                    else:
                        regNoticeDate_l.append("1900/01/01")
                elif line.startswith('_examNoticeDate') == True and eleNo == 1:
                    if len(line.strip().replace(u'_examNoticeDate =', u'')) == 10:
                        examNoticeDate_l.append(str(line.strip().replace(u'_examNoticeDate =', u'')) + "")
                    else:
                        examNoticeDate_l.append("1900/01/01")
                elif line.startswith('delReason') == True and eleNo == 1:
                    delReason_l.append(str(line.strip().replace(u'delReason =', u'')) + "")
                elif line.startswith('examStatus') == True and eleNo == 1:
                    examStatus_l.append(str(line.strip().replace(u'examStatus =', u'')) + "")
                elif line.startswith('extendedStatus') == True and eleNo == 1:
                    extendedStatus_l.append(str(line.strip().replace(u'extendedStatus =', u'')) + "")
                elif line.startswith('oppositionStatus') == True and eleNo == 1:
                    oppositionStatus_l.append(str(line.strip().replace(u'oppositionStatus =', u'')) + "")
                elif line.startswith('nullityActStatus') == True and eleNo == 1:
                    nullityActStatus_l.append(str(line.strip().replace(u'nullityActStatus =', u'')) + "")
                elif line.startswith('applDelStatus') == True and eleNo == 1:
                    applDelStatus_l.append(str(line.strip().replace(u'applDelStatus =', u'')) + "")
                elif line.startswith('autStatus') == True and eleNo == 1:
                    autStatus_l.append(str(line.strip().replace(u'autStatus =', u'')) + "")
                elif line.startswith('agaAutStatus') == True and eleNo == 1:
                    agaAutStatus_l.append(str(line.strip().replace(u'agaAutStatus =', u'')) + "")
                elif line.startswith('amedmentStatus') == True and eleNo == 1:
                    amedmentStatus_l.append(str(line.strip().replace(u'amedmentStatus =', u'')) + "")
                elif line.startswith('transferStatus') == True and eleNo == 1:
                    transferStatus_l.append(str(line.strip().replace(u'transferStatus =', u'')) + "")
                elif line.startswith('issueOppStatus') == True and eleNo == 1:
                    issueOppStatus_l.append(str(line.strip().replace(u'issueOppStatus =', u'')) + "")
                elif line.startswith('issueDelStatus') == True and eleNo == 1:
                    issueDelStatus_l.append(str(line.strip().replace(u'issueDelStatus =', u'')) + "")
                elif line.startswith('quotaStatus') == True and eleNo == 1:
                    quotaStatus_l.append(str(line.strip().replace(u'quotaStatus =', u'')) + "")
                elif line.startswith('unableUseStatus') == True and eleNo == 1:
                    unableUseStatus_l.append(str(line.strip().replace(u'unableUseStatus =', u'')) + "")
                elif line.startswith('end') == True and eleNo == 1:
                    eleNo == 0
                    tmarkType_l.append(tmarkTypel)
                    tmarkTypeDesc_l.append(tmarkTypeDescl)
                    tmarkColor_l.append(tmarkColorl)
                    tmarkColorDesc_l.append(tmarkColorDescl)
                    goodsclassCode_l.append(goodsclassCodel)
                    goodsName_l.append(goodsNamel)
                    goodsGroup_l.append(goodsGroupl)
                    holderChineseName_l.append(holderChineseNamel)
                    holderEnglishName_l.append(holderEnglishNamel)
                    holderJapaneseName_l.append(holderJapaneseNamel)
                    holderAddress_l.append(holderAddressl)
                    chineseCountryName_l.append(chineseCountryNamel)
                    countryCode_l.append(countryCodel)
                    agentChineseName_l.append(agentChineseNamel)
                    agentAddress_l.append(agentAddressl)
        """
        print (str(indexNo1))
        print (str(examNo_l))
        print (str(applNo_l))
        print (str(tmarkName_l))
        print (str(tmarkClassDesc_l))
        print (str(imageData1_l))
        print (str(imageData2_l))
        print (str(imageData3_l))
        print (str(imageData4_l))
        print (str(imageData5_l))
        print (str(imageData6_l))
        print("===========" + "tmarkType_l")
        print (str(tmarkType_l))
        print("===========" + "tmarkTypeDesc_l")
        print (str(tmarkTypeDesc_l))
        print("===========" + "tmarkColor_l")
        print (str(tmarkColor_l))
        print("===========" + "tmarkColorDesc_l")
        print (str(tmarkColorDesc_l))
        print("===========" + "tmarkDraftC_l")
        print (str(tmarkDraftC_l))
        print (str(tmarkDraftE_l))
        print (str(tmarkDraftJ_l))
        print (str(tmarkSign_l))
        print("===========" + "wordDescription_l")
        print (str(wordDescription_l))
        print("===========" + "goodsclassCode_l")
        print (str(goodsclassCode_l))
        print("===========" + "goodsName_l")
        print (str(goodsName_l))
        print("===========" + "goodsGroup_l")
        print (str(goodsGroup_l))
        print (deadline_l)
        print (str(volNo1_l))
        print (str(volNo2_l))
        print (str(processorName_l))
        print (str(holderChineseName_l))
        print (str(holderEnglishName_l))
        print (str(holderJapaneseName_l))
        print (str(holderAddress_l))
        print (str(holderChineseName_l))
        print (str(holderEnglishName_l))
        print (str(holderJapaneseName_l))
        print (str(holderAddress_l))
        print("++++++++++++++++++" + "countrycode")
        print (str(countryCode_l))
        print (str(chineseCountryName_l))
        print (str(agentChineseName_l))
        print (str(agentAddress_l))
        
        print(str(len(indexNo1))+str(len(examNo_l))+str(len(applNo_l))+str(len(tmarkName_l))+str(len(tmarkClassDesc_l)))
        print(str(len(imageData1_l))+str(len(imageData2_l))+str(len(imageData3_l))+str(len(imageData4_l))+str(len(imageData5_l))+str(len(imageData6_l)))
        print(str(len(tmarkType_l))+str(len(tmarkTypeDesc_l))+str(len(tmarkColor_l))+str(len(tmarkColorDesc_l)))
        print(str(len(goodsclassCode_l))+str(len(goodsName_l))+str(len(goodsGroup_l))+str(len(deadline_l)))
        print(str(len(volNo1_l))+str(len(volNo2_l))+str(len(processorName_l)))
        print(str(len(holderChineseName_l))+str(len(holderEnglishName_l))+str(len(holderJapaneseName_l))+str(len(holderAddress_l)))
        print(str(len(countryCode_l))+str(len(chineseCountryName_l)))
        print(str(len(agentChineseName_l))+str(len(agentAddress_l)))
        """
        if len(examNo_l)>0:
            indexNo1 = [index]
            for z in range(1,len(examNo_l)):
                indexNo1.append(index + z)
        else:
            print("No element")
            break
            break
            break
        if not (len(examNo_l) == len(indexNo1) and len(applNo_l) == len(indexNo1) and len(tmarkName_l)  == len(indexNo1) and len(tmarkClassDesc_l) == len(indexNo1) and len(imageData1_l) == len(indexNo1) and len(imageData2_l) == len(indexNo1) and len(imageData3_l) == len(indexNo1) and len(imageData4_l) == len(indexNo1) and len(imageData5_l) == len(indexNo1) and len(imageData6_l) == len(indexNo1) and len(tmarkType_l) == len(indexNo1) and len(tmarkTypeDesc_l) == len(indexNo1) and  len(tmarkColor_l) == len(indexNo1) and len(tmarkColorDesc_l) == len(indexNo1) and len(tmarkDraftC_l) == len(indexNo1) and len(tmarkDraftE_l) == len(indexNo1) and len(tmarkDraftJ_l) == len(indexNo1) and len(tmarkSign_l) == len(indexNo1) and len(wordDescription_l) == len(indexNo1) and len(goodsclassCode_l) == len(indexNo1) and len(goodsName_l) == len(indexNo1) and len(goodsGroup_l) == len(indexNo1) and len(deadline_l) == len(indexNo1) and len(volNo1_l) == len(indexNo1) and len(volNo2_l) == len(indexNo1) and len(processorName_l) == len(indexNo1) and len(holderChineseName_l) == len(indexNo1) and len(holderEnglishName_l) == len(indexNo1) and len(holderJapaneseName_l) == len(indexNo1) and len(holderAddress_l) == len(indexNo1) and len(countryCode_l) == len(indexNo1) and len(chineseCountryName_l) == len(indexNo1) and len(agentChineseName_l) == len(indexNo1) and len(agentAddress_l) == len(indexNo1) and len(applDate_l) == len(indexNo1) and len(regDate_l) == len(indexNo1) and len(regNoticeDate_l) == len(indexNo1) and len(examNoticeDate_l) == len(indexNo1) and len(delReason_l) == len(indexNo1) and len(examStatus_l) == len(indexNo1) and len(extendedStatus_l) == len(indexNo1) and len(oppositionStatus_l)  == len(indexNo1) and len(nullityActStatus_l) == len(indexNo1) and len(applDelStatus_l) == len(indexNo1) and len(autStatus_l) == len(indexNo1) and len(agaAutStatus_l) == len(indexNo1) and len(amedmentStatus_l) == len(indexNo1) and len(transferStatus_l) == len(indexNo1) and len(issueOppStatus_l) == len(indexNo1) and len(issueDelStatus_l) == len(indexNo1) and len(quotaStatus_l) == len(indexNo1) and len(img_url1_l) == len(indexNo1)):
            print(str(len(indexNo1))+"-"+str(len(examNo_l))+"-"+str(len(applNo_l))+"-"+str(len(tmarkName_l))+"-"+str(len(tmarkClassDesc_l))+"-"+str(len(imageData1_l))+"-"+str(len(imageData2_l))+"-"+str(len(imageData3_l))+"-"+str(len(imageData4_l))+"-"+str(len(imageData5_l))+"-"+str(len(imageData6_l))+"-"+str(len(tmarkType_l))+"-"+str(len(tmarkTypeDesc_l))+"-"+str(len(tmarkColor_l))+"-"+str(len(tmarkColorDesc_l))+"-"+str(len(tmarkDraftC_l))+"-"+str(len(tmarkDraftE_l))+"-"+str(len(tmarkDraftJ_l))+"-"+str(len(tmarkSign_l))+"-"+str(len(wordDescription_l))+"-"+str(len(goodsclassCode_l))+"-"+str(len(goodsName_l))+"-"+str(len(goodsGroup_l))+"-"+str(len(deadline_l))+"-"+str(len(volNo1_l))+"-"+str(len(volNo2_l))+"-"+str(len(processorName_l))+"-"+str(len(holderChineseName_l))+"-"+str(len(holderEnglishName_l))+"-"+str(len(holderJapaneseName_l))+"-"+str(len(holderAddress_l))+"-"+str(len(countryCode_l))+"-"+str(len(chineseCountryName_l))+"-"+str(len(agentChineseName_l))+"-"+str(len(agentAddress_l))+"-"+str(len(applDate_l))+"-"+str(len(regDate_l))+"-"+str(len(regNoticeDate_l))+"-"+str(len(examNoticeDate_l))+"-"+str(len(delReason_l))+"-"+str(len(examStatus_l))+"-"+str(len(extendedStatus_l))+"-"+str(len(oppositionStatus_l))+"-"+str(len(nullityActStatus_l))+"-"+str(len(applDelStatus_l))+"-"+str(len(autStatus_l))+"-"+str(len(agaAutStatus_l))+"-"+str(len(amedmentStatus_l))+"-"+str(len(transferStatus_l))+"-"+str(len(issueOppStatus_l))+"-"+str(len(issueDelStatus_l))+"-"+str(len(quotaStatus_l))+"-"+str(len(img_url1_l)))
            print("Length not matched")                                                                                     
            break 
            break    
            break
        for k in range(len(examNo_l)):
            if len(imageData1_l[k]) < 25  or len(examNo_l[k]) !=8 or len(applNo_l[k]) !=9:
                continue
                
            now = datetime.datetime.today()
            deadline = deadline_l[k]
            if len(deadline) == 0 or deadline == [None]:
                continue
            print("===================")
            print(str(indexNo1[k]) + '-' + str(examNo_l[k]))
            print(deadline)
            deadline = deadline.replace('/', '-')
           
            #try:
                #deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d')
            #except:
                #print(deadline)
                #continue
            #else:
           
            deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d')
            delta = datetime.timedelta(days=183)
            halfYearLater = deadline + delta
            if halfYearLater < now :
                print(deadline)
                continue
            else:
                print(len(indexNo1))
                print("==="+str(deadline)+"===")
                
            #if len(imageData1_l[k]) < 24 or len(img_url1_l[k]) < 134:
                #continue
                sqlStuff = "INSERT INTO tmarkTable4 (indexNo, examNo, applNo, tmarkName, tmarkClassDesc, imageData1, imageData2, imageData3, imageData4, imageData5, imageData6, tmarkType, tmarkTypeDesc, tmarkColor, tmarkColorDesc, tmarkDraftC, tmarkDraftE, tmarkDraftJ, tmarkSign, wordDescription, goodsclassCode, goodsName, goodsGroup, deadline,volNo1, volNo2, processorName, holderChineseName, holderEnglishName, holderJapaneseName, holderAddress, countryCode, chineseCountryName, agentChineseName, agentAddress, applDate, regDate, regNoticeDate, examNoticeDate, delReason, examStatus, extendedStatus,oppositionStatus, nullityActStatus, applDelStatus, autStatus, agaAutStatus, amedmentStatus, transferStatus, issueOppStatus, issueDelStatus, quotaStatus, unableUseStatus, url1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                records = [(str(indexNo1[k]), str(examNo_l[k]), str(applNo_l[k]), str(tmarkName_l[k]), str(tmarkClassDesc_l[k]), imageData1_l[k], imageData2_l[k], imageData3_l[k], imageData4_l[k], imageData5_l[k], imageData6_l[k], str(tmarkType_l[k]), str(tmarkTypeDesc_l[k]), str(tmarkColor_l[k]), str(tmarkColorDesc_l[k]), str(tmarkDraftC_l[k]), str(tmarkDraftE_l[k]), str(tmarkDraftJ_l[k]), str(tmarkSign_l[k]), str(wordDescription_l[k]), str(goodsclassCode_l[k]), str(goodsName_l[k]), str(goodsGroup_l[k]), deadline_l[k], str(volNo1_l[k]), str(volNo2_l[k]), str(processorName_l[k]), str(holderChineseName_l[k]), str(holderEnglishName_l[k]), str(holderJapaneseName_l[k]), str(holderAddress_l[k]), str(countryCode_l[k]), str(chineseCountryName_l[k]), str(agentChineseName_l[k]), str(agentAddress_l[k]),str(applDate_l[k]),str(regDate_l[k]),str(regNoticeDate_l[k]),str(examNoticeDate_l[k]),str(delReason_l[k]),str(examStatus_l[k]),str(extendedStatus_l[k]), str(oppositionStatus_l[k]), str(nullityActStatus_l[k]),str(applDelStatus_l[k]),str(autStatus_l[k]),str(agaAutStatus_l[k]),str(amedmentStatus_l[k]),str(transferStatus_l[k]),str(issueOppStatus_l[k]),str(issueDelStatus_l[k]),str(quotaStatus_l[k]),str(unableUseStatus_l[k]),str(img_url1_l[k])),]
                cursor.executemany(sqlStuff, records)
                tmarkdb.commit()
                #print("len(imageData1_l[k]) = "+ str(len(imageData1_l[k])))
                #print("len(img_url1_l[k]) = "+ str(len(img_url1_l[k])))
                if len(img_url1_l[k]) > 0:
                    r = requests.get(img_url1_l[k])
                    with open('./picBase/'+str(applNo_l[k])+'-1.png', 'wb') as f:
                        f.write(r.content)
                if len(img_url2_l[k]) > 0:
                    r = requests.get(img_url2_l[k])
                    with open('./picBase/'+str(applNo_l[k])+'-2.png', 'wb') as f:
                        f.write(r.content)
                if len(img_url3_l[k]) > 0:
                    r = requests.get(img_url3_l[k])
                    with open('./picBase/'+str(applNo_l[k])+'-3.png', 'wb') as f:
                        f.write(r.content)
                if len(img_url4_l[k]) > 0:
                    r = requests.get(img_url4_l[k]) 
                    with open('./picBase/'+str(applNo_l[k])+'-4.png', 'wb') as f:
                        f.write(r.content)
                if len(img_url5_l[k]) > 0:
                    r = requests.get(img_url5_l[k])
                    with open('./picBase/'+str(applNo_l[k])+'-5.png', 'wb') as f:
                        f.write(r.content)
                if len(img_url6_l[k]) > 0:
                    r = requests.get(img_url6_l[k])
                    with open('./picBase/'+str(applNo_l[k])+'-6.png', 'wb') as f:
                        f.write(r.content)
    time.sleep(2)