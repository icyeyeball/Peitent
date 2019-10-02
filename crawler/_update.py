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

tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()

for index in range(0,500):
    #url = 'https://tiponet.tipo.gov.tw/OpenDataApi/OpenData/API/TmarkRights?format=xml&top=10+&skip=0&orderby=appl-no&tk=ywgvRgZ1'
    url = 'https://tiponet.tipo.gov.tw/OpenDataApi/OpenData/API/TmarkRights?format=xml&top=1+&skip='+str(index)+'&orderby=appl-no&tk=ywgvRgZ1'
    r = requests.get(url, verify=False) 
    xml_bytes = r.content
    f = BytesIO(xml_bytes)
    tree = etree.parse(f)
    isOK = [t.text for t in tree.xpath("/API/status")]
    
    if isOK == ['ok']:
        print("===============")
        deadline= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/deadline")]
        print(deadline)
        if len(deadline) == 0 or deadline == [None]:
            continue
        deadline = deadline[0].replace('/', '-')
        deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d')
        #print("deadline =      "+str(deadline))
        delta = datetime.timedelta(days=183)
        halfYearLater = deadline + delta
        #print("halfYearLater = "+str(halfYearLater))
        now = datetime.datetime.today()
        #print("now =           "+str(now))
        if halfYearLater < now :
            continue
      
        examNo = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/exam-no")]
        print(examNo)
        applNo = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/appl-no")]
        #print(applNo)
        #商標種類
        tmarkName = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-name")]
        for i in range(0, len(tmarkName)):
            if tmarkName !=[] and tmarkName != [None]:
                tmarkName[i] = tmarkName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        print(tmarkName)
        #商標種類描述: 1,2,3,T：商標, 4,5,6,S：商標(原服務標章), 7,C：證明標章, 8,M：團體標章, G：團體商標
        tmarkClassDesc = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-class-desc")]
        for i in range(0, len(tmarkClassDesc)):
            if tmarkClassDesc !=[] and tmarkClassDesc != [None]:
                tmarkClassDesc[i] = tmarkClassDesc[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkClassDesc)
        imageData1 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-1")]
        path1 = ['./picBase/'+str(examNo[0])+'-1.png']
        if imageData1 != [None]:
            r = requests.get(imageData1[0])
            with open(path1[0], 'wb') as f:
                f.write(r.content)
        else:
            path1 = [None]
        #print(imageData1)
        imageData2 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-2")]
        path2 = ['./picBase/'+str(examNo[0])+'-2.png']
        if imageData2 != [None]:
            r = requests.get(imageData2[0])
            with open(path2[0], 'wb') as f:
                f.write(r.content)
        else:
            path2 = [None]
        #print(imageData2)
        imageData3 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-3")]
        path3 = ['./picBase/'+str(examNo[0])+'-3.png']
        if imageData3 != [None]:
            r = requests.get(imageData3[0])
            with open(path3[0], 'wb') as f:
                f.write(r.content)
        else:
            path3 = [None]
        #print(imageData3)
        imageData4 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-4")]
        path4 = ['./picBase/'+str(examNo[0])+'-4.png']
        if imageData4 != [None]:
            r = requests.get(imageData4[0])
            with open(path4[0], 'wb') as f:
                f.write(r.content)
        else:
            path4 = [None]
        #print(imageData4)
        imageData5 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-5")]
        path5 = ['./picBase/'+str(examNo[0])+'-5.png']
        if imageData5 != [None]:
            r = requests.get(imageData5[0])
            with open(path5[0], 'wb') as f:
                f.write(r.content)
        else:
            path5 = [None]
        #print(imageData5)
        imageData6 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-6")]
        path6 = ['./picBase/'+str(examNo[0])+'-6.png']
        if imageData6 != [None]:
            r = requests.get(imageData6[0])
            with open(path6[0], 'wb') as f:
                f.write(r.content)
        else:
            path6 = [None]
        #print(imageData6)
        #商標樣態描述 1：聲音  2：立體 3：平面 4：顏色 5：全像圖  6：動態 9：其他
        tmarkType = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-type")]
        #print(tmarkType)
        tmarkTypeDesc = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-type-desc")]
        for i in range(0, len(tmarkTypeDesc)):
            if tmarkTypeDesc !=[] and tmarkTypeDesc != [None]:
                tmarkTypeDesc[i] = tmarkTypeDesc[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        print(tmarkTypeDesc )
        tmarkColor = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-color")]
        #print(tmarkColor)
        #圖樣顏色描述 1：墨色 2：彩色 3：紅色 4：藍色 5：咖啡色 6：其他
        tmarkColorDesc = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-color-desc")]
        for i in range(0, len(tmarkColorDesc)):
            if tmarkColorDesc !=[] and tmarkColorDesc != [None]:
                tmarkColorDesc[i] = tmarkColorDesc[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkColorDesc)
        #圖樣中文
        tmarkDraftC= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-draft-c")]
        for i in range(0, len(tmarkDraftC)):
            if tmarkDraftC !=[] and tmarkDraftC != [None]:
                tmarkDraftC[i] = tmarkDraftC[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        print(tmarkDraftC)
        #圖樣英文
        tmarkDraftE= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-draft-e")]
        for i in range(0, len(tmarkDraftE)):
            if tmarkDraftE !=[] and tmarkDraftE != [None]:
                tmarkDraftE[i] = tmarkDraftE[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkDraftE)
        #圖樣日文
        tmarkDraftJ= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-draft-j")]
        for i in range(0, len(tmarkDraftJ)):
            if tmarkDraftJ !=[] and tmarkDraftJ != [None]:
                tmarkDraftJ[i] = tmarkDraftJ[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkDraftJ)
        #圖樣記號
        tmarkSign= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-sign")]
        #print(tmarkSign)
        #說明文字內容
        wordDescription= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/word-description")]
        for i in range(0, len(wordDescription)):
            if wordDescription !=[] and wordDescription != [None]:
                wordDescription[i] = wordDescription[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(wordDescription)
        goodsclassCode= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/goodsclasses/goodsclass/goodsclass-code")]
        print(goodsclassCode)
        goodsName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/goodsclasses/goodsclass/goods-name")]
        for i in range(0, len(goodsName)):
            if goodsName !=[] and goodsName != [None]:
                goodsName[i] = goodsName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        print(goodsName)
        goodsGroup= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/goodsclasses/goodsclass/goods-group")]
        print(goodsGroup)
        volNo1= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/vol-no1")]
        print(volNo1)
        volNo2= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/vol-no2")]
        print(volNo2)
        processorName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/processor-name")]
        for i in range(0, len(processorName)):
            if processorName !=[] and processorName != [None]:
                processorName[i] = processorName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass 
        #print(processorName)
        holderChineseName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/chinese-name")]
        for i in range(0, len(holderChineseName)):
            if holderChineseName !=[] and holderChineseName != [None]:
                holderChineseName[i] = holderChineseName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass 
        print(holderChineseName)
        holderEnglishName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/english-name")]
        for i in range(0, len(holderEnglishName)):
            if holderEnglishName !=[] and holderEnglishName != [None]:
                holderEnglishName[i] = holderEnglishName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass   
        #print(holderEnglishName)
        holderJapaneseName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/japanese-name")]
        for i in range(0, len(holderJapaneseName)):
            if holderJapaneseName !=[] and holderJapaneseName != [None]:
                holderJapaneseName[i] = holderJapaneseName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass   
        #print(holderJapaneseName)
        holderAddress= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/address")]
        for i in range(0, len(holderAddress)):
            if holderAddress !=[] and holderAddress != [None]:
                holderAddress[i] = holderAddress[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass   
        #print(holderAddress)
        countryCode= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/country-code")]
        #print(countryCode)
        chineseCountryName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/chinese-country-name")]
        for i in range(0, len(chineseCountryName)):
            if chineseCountryName !=[] and chineseCountryName != [None]:
                chineseCountryName[i] = chineseCountryName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass   
        #print(chineseCountryName)
        agentChineseName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/agents/agent/chinese-name")]
        for i in range(0, len(agentChineseName)):
            if agentChineseName !=[] and agentChineseName != [None]:
                agentChineseName[i] = agentChineseName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        if len(agentChineseName) == 0:
            agentChineseName = [None]
        #print(agentChineseName)
        agentAddress= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/agents/agent/address")]
        for i in range(0, len(agentAddress)):
            if agentAddress !=[] and agentAddress != [None]:
                agentAddress[i] = agentAddress[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass   
        if len(agentAddress) == 0:
            agentAddress = [None]
        #print(agentAddress)
         
        sqlStuff = "INSERT INTO tmarkTable (examNo, applNo, tmarkName, tmarkClassDesc, imageData1, imageData2, imageData3, imageData4, imageData5, imageData6, tmarkType, tmarkTypeDesc, tmarkColor, tmarkColorDesc, tmarkDraftC, tmarkDraftE, tmarkDraftJ, tmarkSign, wordDescription, goodsclassCode, goodsName, goodsGroup, deadline,volNo1, volNo2, processorName, holderChineseName, holderEnglishName, holderJapaneseName, holderAddress, countryCode, chineseCountryName, agentChineseName, agentAddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        records = [(str(examNo[0]), str(applNo[0]), str(tmarkName[0]), str(tmarkClassDesc[0]), path1[0], path2[0], path3[0], path4[0], path5[0], path6[0], str(tmarkType[0]), str(tmarkTypeDesc[0]), str(tmarkColor[0]), str(tmarkColorDesc[0]), str(tmarkDraftC[0]), str(tmarkDraftE[0]), str(tmarkDraftJ[0]), str(tmarkSign[0]), str(wordDescription[0]), str(goodsclassCode[0]), str(goodsName[0]), str(goodsGroup[0]), deadline, str(volNo1[0]), str(volNo2[0]), str(processorName[0]), str(holderChineseName[0]), str(holderEnglishName[0]), str(holderJapaneseName[0]), str(holderAddress[0]), str(countryCode[0]), str(chineseCountryName[0]), str(agentChineseName[0]), str(agentAddress[0])),]
        #records = [(str(examNo[0]), str(applNo[0]), str(tmarkName[0]), str(tmarkClassDesc[0]), img1, img2, img3, img4, img5, img6, str(tmarkType[0]), str(tmarkTypeDesc[0]), str(tmarkColor[0]), str(tmarkColorDesc[0]), str(tmarkDraftC[0]), str(tmarkDraftE[0]), str(tmarkDraftJ[0]), str(tmarkSign[0]), str(wordDescription[0]), str(goodsclassCode[0]), str(goodsName[0]), str(goodsGroup[0]), deadline ,str(volNo1[0]), str(volNo2[0]), str(processorName[0]), str(holderChineseName[0]), str(holderEnglishName[0]), str(holderJapaneseName[0]), str(holderAddress[0]), str(countryCode[0]), str(chineseCountryName[0]), str(agentChineseName[0]), str(agentAddress[0])),]
        cursor.executemany(sqlStuff, records)
        tmarkdb.commit()
                
        time.sleep(2)
    else:
        break
    index=1    


#tmarkclass = [t.text for t in tree.xpath("/API/tmarkrights/tmark-class")]
#print("====="+str(type(xml_bytes)))

print ("====================================================")