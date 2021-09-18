# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# 

import jieba
import jieba.analyse

final = ""
filename = './s2.txt'

with open(filename,'r',encoding = 'utf-8') as f:
    for line in f.readlines():
        word = jieba.cut(line)
        for i in word:
            final = final + i +" "

with open('./o2.txt', 'w', encoding = 'utf-8') as f2:
    f2.write(final)
    
f.close 
f2.close



