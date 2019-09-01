# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
#
import requests
from bs4 import BeautifulSoup
import os
import time
from fake_useragent import UserAgent
import random

#print(UserAgent().chrome)
#print(UserAgent().ie)
#print(UserAgent().firefox)
#print(UserAgent().opera)
#print(UserAgent().safari)

url = 'https://twtmsearch.tipo.gov.tw/SS0/SS0202.jsp?tab_showView=showView_Image&l6=zh_TW&isReadBulletinen_US=&isReadBulletinzh_TW=true'
#url = 'https://www.google.com.tw/search?num=20&lr=lang_zh-TW&q=cat'

ua = UserAgent()
#headers = {'User-Agent': ua.random}
headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "",# cookie
        "Host": "sbgg.saic.gov.cn:9080",
        "Origin": "http://sbgg.saic.gov.cn:9080",
        "Referer": "http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
print (headers)

response = requests.get(url,headers=headers, timeout=15) #使用header避免訪問受到限制
soup = BeautifulSoup(response.content, 'html.parser')
print (soup.prettify())
print ("====================================================")
#news_title = item.find("h3", {"class": "r"}).find("a").text
name_l = soup.find_all('div',  class_='item_btn')
for name in name_l:
    print (name)


"""
items = soup.find_all('img')


folder_path ='./picture/1/'

if (os.path.exists(folder_path) == False): #判斷資料夾是否存在
    os.makedirs(folder_path) #Create folder



for index , item in enumerate (items):
    if (item and index < 5):

        html = requests.get(item.get('src')) # use 'get' to get photo link path , requests = send request
        img_name = folder_path + str(index + 1) + '.jpg'

        with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入
            file.write(html.content)
            file.flush()
        file.close() #close file

        print('第 %d 張' % (index + 1))
        
        time.sleep(1)

print('Done')
"""