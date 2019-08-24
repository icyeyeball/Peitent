# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190824
############################
# python googles.py input

import requests
from bs4 import BeautifulSoup
str = "python3"
r = requests.get('https://www.google.com/search?q=寒流')
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
a_tags = soup.find_all("span > h3.r",class_="g", )
print(a_tags)
#for t in a_tags:
#    print(t.text)