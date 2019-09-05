# -*- coding: utf-8 -*-
############################
# Peicheng Lu 201908230
############################
# python _en_zh_div.py input
import sys
import re

cop = re.compile("[^\u4e00-\u9fa5^ ^A-Z^a-z^1-9^]") 
cop_en = re.compile("[^ ^A-Z^a-z^]")
cop_zh = re.compile("[^\u4e00-\u9fa5^ ^]") 
cop_dig = re.compile("[^0-9^ ^]") 
input = cop.sub('',sys.argv[1]) 
print ("input = " + input)

en_l = []
zh_l = []
dig_l = []
en_text = cop_en.sub(' ',input )
zh_text = cop_zh.sub(' ',input )
dig_text = cop_dig.sub(' ',input )
print (en_text.split())
print (zh_text.split())
print (dig_text.split())
en_l = en_text.split()
zh_l = zh_text.split()
dig_l = dig_text.split()
for i in en_l:
    print (i)
for i in zh_l:
    print (i)
for i in dig_l:
    print (i)




