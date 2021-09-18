# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# Usage: python demo.py words
import sys
import jieba
import gensim
import json
import re

input = sys.argv[1]
jieba.add_word('駁回')
jieba.add_word('會過')
jieba.add_word('不會過')
seg_list = jieba.lcut(input, cut_all=False)

#print(seg_list)

list_key = [["商標","申請","註冊","流程","時間","多久","多長"],\
            ["個人","申請","公司","商標","名義","獨自"],\
            ["商標","彩色","黑白","墨色","顏色","色彩"],\
            ["商標","不會過","會過","核准","駁回","通過"],\
            ["商標","費用","申請","註冊","多少錢","價錢","價格"],\
            ["商標","申請","服務","方案","內容","註冊"],\
            ["申請","商標","近似","相同","使用","先"],\
            ["申請","自己","商標","核駁","駁回","代理人"],\
            ["商標","選擇","類別","商品","服務","分類"],\
            ["委任","合約","簽約","條款","服務","條約"],\
            ["侵權","商標","別人","同業","仿冒","相同","抄襲","相似"],\
            ["延展","商標","期限","到期","過期","延長"],\
            ["廢止","商標","別人","類似","相似","停用","使用"],\
            ["識別","商標","相似","類似","相同"],\
            ["混淆","誤認","相似","相同","商標","一樣","類似"],\
            ["地址","哪裏","縣市","事務所","公司","聯絡","連絡"],\
            ["聯繫","聯絡","電話","何時","手機","信箱","LINE","Line","line"],\
            ["線上","商標","申請","使用","操作","自助"],\
            ["使用","操作","商標","查詢","檢索","系統","平台"]]
            
list_num = [[40,40,40,80,80,80,80],\
            [80,40,80,40,40,80],\
            [40,60,60,60,60,60,60],\
            [40,60,80,60,80],\
            [40,80,40,40,80,80,80],\
            [40,40,80,80,60,40],\
            [40,40,40,40,40,80],\
            [40,40,40,80,80,40],\
            [40,60,80,60,60,80],\
            [80,80,40,40,40,80],\
            [80,40,40,60,60,60,60,60],\
            [80,40,60,60,60,60],\
            [80,40,40,60,60,80,80],\
            [40,40,40,40,40],\
            [80,80,60,60,40,60,80],\
            [80,60,80,60,40,60,60],\
            [80,80,80,40,80,80,80,80,80],\
            [80,40,40,60,60,60],\
            [60,60,40,60,60,60,60]]
            
result = []
for i in range(0,len(list_key)):
    z = 0
    weight = 0.0
    for j in range(0,len(list_key[i])):
        for k in range(0,len(seg_list)):
            if seg_list[k]==list_key[i][j]:
                z = z + 1
                weight = weight + list_num[i][j]
    if z > 1:
        weight = weight*1.2
        subresult = {"q":i+1,"weight":weight}
        result.append(subresult)
    else:
        subresult = {"q":i+1,"weight":weight}
        result.append(subresult)
        
#print(result)
for i in range(0,len(result)-1):
    for j in range(0,len(result)-1-i): 
        if result[j]["weight"] < result[j+1]["weight"]:
            tmp = result[j]
            result[j]= result[j+1]
            result[j+1] = tmp
data = []
#print(len(result))
for i in range(0,len(list_key)):
    if i < len(result):
        data.append(result[i])
    else:
        break
app_json = json.dumps(data)
print(app_json)

    
    
