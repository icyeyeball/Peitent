# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
#
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import math
import sys
import imutils

import requests #引入函式庫
from bs4 import BeautifulSoup
import re
url = 'https://www.dcard.tw/f'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
dcard_title = soup.find_all('h3', re.compile('Title__Text-v196i6-0 gmfDU'))
print('Dcard 熱門前十文章標題：')
for index, item in enumerate(dcard_title[:10]):
    print("{0:2d}. {1}".format(index + 1, item.text.strip()))