# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190824
############################
# python googles.py input

import requests
import sys
from bs4 import BeautifulSoup
import re

# Google 搜尋 URL
google_url = 'https://www.google.com.tw/search?num=30&q='
wiki_rul = 'https://zh.wikipedia.org/wiki/'

# 查詢參數

my_params = sys.argv[1]
k1 = google_url + my_params
k2 = wiki_rul + my_params
cop = re.compile("[^\u4e00-\u9fa5^^]")

# 下載 Google 搜尋結果
r = requests.get(k1, params = my_params)

# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 原始碼
    soup = BeautifulSoup(r.text, 'html.parser')
    #print (soup.prettify())
    sp = str(soup)
    #print (sp)
    #print (sp[sp.find('http://')-23:sp.find('http://')-18])
    items = soup.findAll("div", {"class": sp[sp.find('http://')-23:sp.find('http://')-18]})
    #items = soup.findAll("div", {"class": sp[sp.find('https://')-23:sp.find('https://')-18]})
i = 1   
with open('google.txt', 'w', encoding = 'utf-8') as f2:
    for item in items:
        # title
        #news_title = item.find("h3", {"class": "r"}).find("a").text
        #print (news_title)
        # url
        href = str(item)
        if href.find('wiki') >= 0:
            url = k2
            #print (url)
        elif href.find('gov.tw') >= 0:
            url = ''
        else:
            url = href[href.find('http'):href.find('&amp')]
            #print (url)
        if url == '':
            continue
        else:
            res = requests.get(url)
            if res.status_code == requests.codes.ok:
                soup2 = BeautifulSoup(res.text, 'html.parser') 
                stories = str(soup2.find_all('p', class_=""))
                stories = cop.sub('', stories)
                print (stories)
                f2.write(stories)
                f2.write('\n')
                #f2.write("--------------------------i = " + str(i))
                #f2.write('\n')
                #f2.write("url = " + str(url))
                #f2.write('\n')
        #f2.write("=================================================")
        f2.write('\n')
        i += 1
