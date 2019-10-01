# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190907
############################
# python _googles.py input

import requests
import sys
from bs4 import BeautifulSoup
import re
import time
from langconv import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Google 搜尋 URL
#google_url = 'https://www.google.com.tw/search?num=20&lr=lang_zh-TW&q='
input = sys.argv[1]
driver = webdriver.Chrome(r"C:\Users\lehsiao\cmder\peitent\chromedriver.exe")
driver.get('http://dict.revised.moe.edu.tw/cbdic/search.htm')
qs0 = driver.find_element_by_name('qs0')
qs0.send_keys(input)
qs0.send_keys(Keys.RETURN)
soup = BeautifulSoup(driver.page_source, 'lxml') 
#print (soup)
pinyin=[]
ele_l = []
for ele in soup.select('#main td'):
    ele_l.append(ele.text)
for i in range(2, len(ele_l),3):
    if(len(ele_l[i])==2):
        pinyin.append(ele_l[i+1])
    else:
        break
for i in pinyin:
    print(i)
