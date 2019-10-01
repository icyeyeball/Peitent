# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
import requests
import time
from lxml import etree
from io import BytesIO
import requests.packages.urllib3
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pymysql
import time


for index in range(0,100):
    url = 'https://tiponet.tipo.gov.tw/OpenDataApi/OpenData/API/TmarkRights?format=xml&top=1+&skip='+str(index)+'&orderby=appl-no&tk=ywgvRgZ1'
    #url = 'https://tiponet.tipo.gov.tw/OpenDataApi/OpenData/API/TmarkRights?format=xml&top=1+&skip=12&orderby=appl-no&tk=ywgvRgZ1'
    r = requests.get(url, verify=False) 
    xml_bytes = r.content
    f = BytesIO(xml_bytes)
    tree = etree.parse(f)
    isOK = [t.text for t in tree.xpath("/API/status")]
    
    if isOK == ['ok']:
        examNo = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/exam-no")]
        print(examNo)
        applNo = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/appl-no")]
        print(applNo)
        #商標種類
        tmarkName = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-name")]
        print(tmarkName)
        #商標種類描述: 1,2,3,T：商標, 4,5,6,S：商標(原服務標章), 7,C：證明標章, 8,M：團體標章, G：團體商標
        tmarkClassDesc = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-class-desc")]
        print(tmarkClassDesc)
        imageData1 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-1")]
        print(imageData1)
        imageData2 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-2")]
        print(imageData2)
        imageData3 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-3")]
        print(imageData3)
        imageData4 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-4")]
        print(imageData4)
        imageData5 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-5")]
        print(imageData5)
        imageData6 = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-image-url/image-data-6")]
        print(imageData6)
        #商標樣態描述 1：聲音  2：立體 3：平面 4：顏色 5：全像圖  6：動態 9：其他
        tmarkType = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-type")]
        print(tmarkType)
        tmarkTypeDesc = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-type-desc")]
        print(tmarkTypeDesc )
        tmarkColor = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-color")]
        print(tmarkColor)
        #圖樣顏色描述 1：墨色 2：彩色 3：紅色 4：藍色 5：咖啡色 6：其他
        tmarkColorDesc = [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-color-desc")]
        print(tmarkColorDesc)
        #圖樣中文
        tmarkDraftC= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-draft-c")]
        print(tmarkDraftC)
        #圖樣英文
        tmarkDraftE= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-draft-e")]
        print(tmarkDraftE)
        #圖樣日文
        tmarkDraftJ= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-draft-j")]
        print(tmarkDraftJ)
        #圖樣記號
        tmarkSign= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/tmark-sign")]
        print(tmarkSign)
        #說明文字內容
        wordDescription= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/word-description")]
        print(wordDescription)
        goodsclassCode= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/goodsclasses/goodsclass/goodsclass-code")]
        print(goodsclassCode)
        goodsName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/goodsclasses/goodsclass/goods-name")]
        print(goodsName)
        goodsGroup= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/goodsclasses/goodsclass/goods-group")]
        print(goodsGroup)
        deadline= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/deadline")]
        print(deadline)
        volNo1= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/vol-no1")]
        print(volNo1)
        volNo2= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/vol-no2")]
        print(volNo2)
        processorName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/processor-name")]
        print(processorName)
        holderChineseName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/chinese-name")]
        for i in range(0, len(holderChineseName)):
            holderChineseName[i] = holderChineseName[i] .strip().replace(u'\u3000', u' ').replace(u'\xa0', u'  ').replace(u'\ufeff', u'  ')
        print(holderChineseName)
        holderEnglishName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/english-name")]
        print(holderEnglishName)
        holderJapaneseName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/japanese-name")]
        print(holderJapaneseName)
        holderAddress= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/address")]
        print(holderAddress)
        countryCode= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/country-code")]
        print(countryCode)
        chineseCountryName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/holders/holder/chinese-country-name")]
        print(chineseCountryName)
        agentChineseName= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/agents/agent/chinese-name")]
        print(agentChineseName)
        agentAddress= [t.text for t in tree.xpath("/API/tmarkrights/tmarkcontent/parties/agents/agent/address")]
        print(agentAddress)
        
        time.sleep(2)
    else:
        break
    index=1    


#tmarkclass = [t.text for t in tree.xpath("/API/tmarkrights/tmark-class")]
#print("====="+str(type(xml_bytes)))

print ("====================================================")