# -*- coding: utf-8 -*-
############################
# Peicheng Lu 201908230
############################
# python fuzzy.py txt
import gensim
import sys
import re
import jieba
from langconv import *

i = 0
class_l=["a"]
for i in range(0,len(class_l)):
    print(class_l[i])
    