# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190824
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
driver.get('http://google.com')
q = driver.find_element_by_name('q')
q.send_keys(input)
q.send_keys(Keys.RETURN)
soup = BeautifulSoup(driver.page_source, 'lxml') 
for ele in soup.select('#rso h3 div'):
    print(ele.text)
driver.find_element_by_link_text('下一頁').click()
for p  in range(3):
    driver.find_element_by_link_text('下一頁').click()
    soup = BeautifulSoup(driver.page_source, 'lxml') 
    for ele in soup.select('#rso h3 div'):
        print(ele.text)
        time.sleep(1)
#driver.find_element_by_css_selector('#rso a:nth-child(1)').click()

#driver.get('http://dict.revised.moe.edu.tw/cbdic/search.htm')

#c = driver.find_element_by_link_text("本典")
#c.click()
#q.send_keys(Keys.RETURN)

#q = driver.find_element_by_name('#main input#qs0:nth-child(1)').send_keys('Keys.RETURN')