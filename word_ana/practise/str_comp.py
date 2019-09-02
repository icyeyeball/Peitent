# -*- coding: utf-8 -*-
############################
# Peicheng Lu 201908230
############################
# 
import gensim
import sys
import re
import jieba
from langconv import *

class_l=["a","b","c"]
class_l.append("d")
word = "b"
for i in range(0,len(class_l)):
    if word == class_l[i]:
        print(word)