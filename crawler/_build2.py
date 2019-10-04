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

now = datetime.datetime.today()
headers = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
'Cookie':'gr_user_id=1f9ea7ea-462a-4a6f-9d55-156631fc6d45; bid=vPYpmmD30-k; ll="118282"; ue="codin; __utmz=30149280.1499577720.27.14.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/doulist/240962/; __utmv=30149280.3049; _vwo_uuid_v2=F04099A9dd; viewed="27607246_26356432"; ap=1; ps=y; push_noty_num=0; push_doumail_num=0; dbcl2="30496987:gZxPfTZW4y0"; ck=13ey; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1515153574%2C%22https%3A%2F%2Fbook.douban.com%2Fmine%22%5D; __utma=30149280.833870293.1473539740.1514800523.1515153574.50; __utmc=30149280; _pk_id.100001.8cb4=255d8377ad92c57e.1473520329.20.1515153606.1514628010.'
} #替換成自己的cookie

for index in range(0,3000000, 100):
#for index in range(0,3000000):
    #url = 'https://tiponet.tipo.gov.tw/OpenDataApi/OpenData/API/TmarkRights?format=xml&top=10+&skip=0&orderby=appl-no&tk=ywgvRgZ1'
    url = 'https://tiponet.tipo.gov.tw/OpenDataApi/OpenData/API/TmarkRights?format=xml&top=100&skip='+str(index)+'&orderby=appl-no&tk=ywgvRgZ1'
    print ("url = " + url)
    r = requests.get(url, verify=False) 
    xml_bytes = r.content
    f = BytesIO(xml_bytes)
    tree = etree.parse(f,)
    isOK = [t.text for t in tree.xpath("/API/status")]
    
    #time.sleep(0.1)
    print("index = " + str(index))
    
    if isOK == ['ok']:
        #print("===============")
        deadlineOK = []
        deadline= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/deadline")]
        #print(deadline)
        for i in range(0,len(deadline)):
            if deadline[i] == 0 or deadline[i] == [None]:
                dieadlineOK.append(0)
            else:
                deadlineOK.append(1)

        deadline[i] = deadline[i].replace('/', '-')
        deadline[i] = datetime.datetime.strptime(deadline[i], '%Y-%m-%d')
        #print("deadline =      "+str(deadline))
        delta = datetime.timedelta(days=183)
        halfYearLater = deadline[i] + delta
        #print("halfYearLater = "+str(halfYearLater))
        #print("now =           "+str(now))
        for i in range(0,len(deadline)):
            if deadlineOK[i] == 1:
                if halfYearLater < now :
                    deadlineOK[i] = 0
                else:
                    deadlineOK[i] = 1
         
        examNo = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/exam-no")]
        print(examNo)
        applNo = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/appl-no")]
        #print(applNo)
        #商標種類
        tmarkName = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-name")]
        for i in range(0, len(tmarkName)):
            if tmarkName !=[] and None not in tmarkName:
                tmarkName[i] = tmarkName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        print(tmarkName)
        #商標種類描述: 1,2,3,T：商標, 4,5,6,S：商標(原服務標章), 7,C：證明標章, 8,M：團體標章, G：團體商標
        tmarkClassDesc = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-class-desc")]
        for i in range(0, len(tmarkClassDesc)):
            if tmarkClassDesc !=[] and None not in tmarkClassDesc:
                tmarkClassDesc[i] = tmarkClassDesc[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkClassDesc)
        imageData1 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-1")]
        path1 = ['./picBase2/'+str(examNo[0])+'-1.png']
        if imageData1 != [None]:
            r = requests.get(imageData1[0])
            with open(path1[0], 'wb') as f:
                f.write(r.content)
        else:
            path1 = [None]
        #print(imageData1)
        imageData2 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-2")]
        path2 = ['./picBase2/'+str(examNo[0])+'-2.png']
        if imageData2 != [None]:
            r = requests.get(imageData2[0])
            with open(path2[0], 'wb') as f:
                f.write(r.content)
        else:
            path2 = [None]
        #print(imageData2)
        imageData3 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-3")]
        path3 = ['./picBase2/'+str(examNo[0])+'-3.png']
        if imageData3 != [None]:
            r = requests.get(imageData3[0])
            with open(path3[0], 'wb') as f:
                f.write(r.content)
        else:
            path3 = [None]
        #print(imageData3)
        imageData4 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-4")]
        path4 = ['./picBase2/'+str(examNo[0])+'-4.png']
        if imageData4 != [None]:
            r = requests.get(imageData4[0])
            with open(path4[0], 'wb') as f:
                f.write(r.content)
        else:
            path4 = [None]
        #print(imageData4)
        imageData5 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-5")]
        path5 = ['./picBase2/'+str(examNo[0])+'-5.png']
        if imageData5 != [None]:
            r = requests.get(imageData5[0])
            with open(path5[0], 'wb') as f:
                f.write(r.content)
        else:
            path5 = [None]
        #print(imageData5)
        imageData6 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-6")]
        path6 = ['./picBase2/'+str(examNo[0])+'-6.png']
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
            if tmarkTypeDesc !=[] and None not in tmarkTypeDesc:
                tmarkTypeDesc[i] = tmarkTypeDesc[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkTypeDesc )
        tmarkColor = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-color")]
        #print(tmarkColor)
        #圖樣顏色描述 1：墨色 2：彩色 3：紅色 4：藍色 5：咖啡色 6：其他
        tmarkColorDesc = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-color-desc")]
        for i in range(0, len(tmarkColorDesc)):
            if tmarkColorDesc !=[] and None not in tmarkColorDesc:
                tmarkColorDesc[i] = tmarkColorDesc[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkColorDesc)
        #圖樣中文
        tmarkDraftC= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-draft-c")]
        for i in range(0, len(tmarkDraftC)):
            if tmarkDraftC !=[] and None not in tmarkDraftC:
                tmarkDraftC[i] = tmarkDraftC[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkDraftC)
        #圖樣英文
        tmarkDraftE= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-draft-e")]
        for i in range(0, len(tmarkDraftE)):
            if tmarkDraftE !=[] and None not in tmarkDraftE:
                tmarkDraftE[i] = tmarkDraftE[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkDraftE)
        #圖樣日文
        tmarkDraftJ= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-draft-j")]
        for i in range(0, len(tmarkDraftJ)):
            if tmarkDraftJ !=[] and None not in tmarkDraftJ:
                tmarkDraftJ[i] = tmarkDraftJ[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(tmarkDraftJ)
        #圖樣記號
        tmarkSign= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-sign")]
        #print(tmarkSign)
        #說明文字內容
        wordDescription= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/word-description")]
        for i in range(0, len(wordDescription)):
            if wordDescription !=[] and None not in wordDescription:
                wordDescription[i] = wordDescription[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(wordDescription)
        goodsclassCode= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/goodsclasses/goodsclass/goodsclass-code")]
        #print(goodsclassCode)
        goodsName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/goodsclasses/goodsclass/goods-name")]
        for i in range(0, len(goodsName)):
            if goodsName !=[] and None not in goodsName:
                goodsName[i] = goodsName[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        #print(goodsName)
        goodsGroup= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/goodsclasses/goodsclass/goods-group")]
        #print(goodsGroup)
        volNo1= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/vol-no1")]
        #print(volNo1)
        volNo2= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/vol-no2")]
        #print(volNo2)
        processorName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/processor-name")]
        for i in range(0, len(processorName)):
            if processorName !=[] and None not in processorName:
                processorName[i] = processorName[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass 
        #print(processorName)
        holderChineseName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/chinese-name")]
        for i in range(0, len(holderChineseName)):
            if holderChineseName !=[] and None not in holderChineseName:
                holderChineseName[i] = holderChineseName[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass 
        #print(holderChineseName)
        holderEnglishName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/english-name")]
        
        for i in range(0, len(holderEnglishName)):
            if holderEnglishName !=[] and None not in holderEnglishName:
                holderEnglishName[i] = holderEnglishName[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass   
        #print(holderEnglishName)
        holderJapaneseName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/japanese-name")]
        for i in range(0, len(holderJapaneseName)):
            if holderJapaneseName !=[]  and None not in holderJapaneseName:
                holderJapaneseName[i] = holderJapaneseName[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass   
        #print(holderJapaneseName)
        holderAddress= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/address")]
        for i in range(0, len(holderAddress)):
            if holderAddress !=[] and None not in holderAddress:
                holderAddress[i] = holderAddress[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass   
        #print(holderAddress)
        countryCode= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/country-code")]
        #print(countryCode)
        chineseCountryName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/chinese-country-name")]
        for i in range(0, len(chineseCountryName)):
            if chineseCountryName !=[] and None not in chineseCountryName:
                chineseCountryName[i] = chineseCountryName[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass   
        #print(chineseCountryName)
        agentChineseName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/agents/agent/chinese-name")]
        for i in range(0, len(agentChineseName)):
            if agentChineseName !=[] and None not in agentChineseName:
                agentChineseName[i] = agentChineseName[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        if len(agentChineseName) == 0:
            agentChineseName = [None]
        #print(agentChineseName)
        agentAddress= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/agents/agent/address")]
        for i in range(0, len(agentAddress)):
            if agentAddress !=[] and None not in agentAddress:
                agentAddress[i] = agentAddress[i].strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
            else:
                pass
        if len(agentAddress) == 0:
            agentAddress = [None]
        #print(agentAddress)

        if len(goodsclassCode) == 100 and len(goodsName) == 100 and len(goodsGroup) == 100 and (holderChineseName)  == 100 and len(holderEnglishName) ==100 and len(holderJapaneseName) == 100 and len(agentChineseName) ==100 and len(agentAddress) == 100:
            for i in range(0,100):
                if deadlineOK[i] == 1:
                    print (deadline[i])
                    sqlStuff = "INSERT INTO tmarkTable (examNo, applNo, tmarkName, tmarkClassDesc, imageData1, imageData2, imageData3, imageData4, imageData5, imageData6, tmarkType, tmarkTypeDesc, tmarkColor, tmarkColorDesc, tmarkDraftC, tmarkDraftE, tmarkDraftJ, tmarkSign, wordDescription, goodsclassCode, goodsName, goodsGroup, deadline,volNo1, volNo2, processorName, holderChineseName, holderEnglishName, holderJapaneseName, holderAddress, countryCode, chineseCountryName, agentChineseName, agentAddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    records = [(str(examNo[i]), str(applNo[i]), str(tmarkName[i]), str(tmarkClassDesc[i]), path1[i], path2[i], path3[i], path4[i], path5[i], path6[i], str(tmarkType[i]), str(tmarkTypeDesc[i]), str(tmarkColor[i]), str(tmarkColorDesc[i]), str(tmarkDraftC[i]), str(tmarkDraftE[i]), str(tmarkDraftJ[i]), str(tmarkSign[i]), str(wordDescription[i]), str(goodsclassCode[i]), str(goodsName[i]), str(goodsGroup[i]), deadline[i], str(volNo1[i]), str(volNo2[i]), str(processorName[i]), str(holderChineseName[i]), str(holderEnglishName[i]), str(holderJapaneseName[i]), str(holderAddress[i]), str(countryCode[i]), str(chineseCountryName[i]), str(agentChineseName[i]), str(agentAddress[i])),]
                    #records = [(str(examNo[0]), str(applNo[0]), str(tmarkName[0]), str(tmarkClassDesc[0]), img1, img2, img3, img4, img5, img6, str(tmarkType[0]), str(tmarkTypeDesc[0]), str(tmarkColor[0]), str(tmarkColorDesc[0]), str(tmarkDraftC[0]), str(tmarkDraftE[0]), str(tmarkDraftJ[0]), str(tmarkSign[0]), str(wordDescription[0]), str(goodsclassCode[0]), str(goodsName[0]), str(goodsGroup[0]), deadline ,str(volNo1[0]), str(volNo2[0]), str(processorName[0]), str(holderChineseName[0]), str(holderEnglishName[0]), str(holderJapaneseName[0]), str(holderAddress[0]), str(countryCode[0]), str(chineseCountryName[0]), str(agentChineseName[0]), str(agentAddress[0])),]
                    cursor.executemany(sqlStuff, records)
                    tmarkdb.commit()
                else:
                    print (deadline[i])
                    continue
        else:
            for i in range(0,100):
                if deadlineOK[i] == 1:
                    print (deadline[i])
                    sqlStuff = "INSERT INTO tmarkTable (examNo, applNo, tmarkName, tmarkClassDesc, imageData1, imageData2, imageData3, imageData4, imageData5, imageData6, tmarkType, tmarkTypeDesc, tmarkColor, tmarkColorDesc, tmarkDraftC, tmarkDraftE, tmarkDraftJ, tmarkSign, wordDescription, goodsclassCode, goodsName, goodsGroup, deadline,volNo1, volNo2, processorName, holderChineseName, holderEnglishName, holderJapaneseName, holderAddress, countryCode, chineseCountryName, agentChineseName, agentAddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    records = [(str(examNo[i]), str(applNo[i]), str(tmarkName[i]), str(tmarkClassDesc[i]), path1[i], path2[i], path3[i], path4[i], path5[i], path6[i], str(tmarkType[i]), str(tmarkTypeDesc[i]), str(tmarkColor[i]), str(tmarkColorDesc[i]), str(tmarkDraftC[i]), str(tmarkDraftE[i]), str(tmarkDraftJ[i]), str(tmarkSign[i]), str(wordDescription[i]), '', '', '', deadline[i], str(volNo1[i]), str(volNo2[i]), str(processorName[i]), '', '', '', '', str(countryCode[0]), str(chineseCountryName[0]), '', ''),]
                    #records = [(str(examNo[0]), str(applNo[0]), str(tmarkName[0]), str(tmarkClassDesc[0]), img1, img2, img3, img4, img5, img6, str(tmarkType[0]), str(tmarkTypeDesc[0]), str(tmarkColor[0]), str(tmarkColorDesc[0]), str(tmarkDraftC[0]), str(tmarkDraftE[0]), str(tmarkDraftJ[0]), str(tmarkSign[0]), str(wordDescription[0]), str(goodsclassCode[0]), str(goodsName[0]), str(goodsGroup[0]), deadline ,str(volNo1[0]), str(volNo2[0]), str(processorName[0]), str(holderChineseName[0]), str(holderEnglishName[0]), str(holderJapaneseName[0]), str(holderAddress[0]), str(countryCode[0]), str(chineseCountryName[0]), str(agentChineseName[0]), str(agentAddress[0])),]
                    cursor.executemany(sqlStuff, records)
                    tmarkdb.commit()
                else:
                    print (deadline[i])
                    continue
               
    else:
        break
        
#tmarkclass = [t.text for t in tree.xpath("/API/tmarkrights/tmark-class")]
#print("====="+str(type(xml_bytes)))

print ("====================================================")