# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190824
############################
# python googles.py input

import requests
from bs4 import BeautifulSoup

search_list = []
keyword = "柯文哲"
res = requests.get("https://www.google.com.tw/search?num=5&q="+keyword+"&oq="+keyword+"&dcr=0&tbm=nws&source=lnt&tbs=qdr:d")

# 關鍵字多加一個雙引號是精準搜尋
# num: 一次最多要request的筆數, 可減少切換頁面的動作
# tbs: 資料時間, hour(qdr:h), day(qdr:d), week(qdr:w), month(qdr:m), year(qdr:w)

if res.status_code == 200:
    content = res.content
    soup = BeautifulSoup(content, "html.parser")
    print (soup.prettify())
    items = soup.findAll("div", {"class": "g"})
    
    for item in items:
        # title
        news_title = item.find("h3", {"class": "r"}).find("a").text
        print (news_title)
        # url
        href = item.find("h3", {"class": "r"}).find("a").get("href")
        href = str(href)
        url = href[href.find('http'):href.find('&sa')]
        print (url)        
