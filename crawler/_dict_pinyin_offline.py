# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190908
############################
# python _googles.py input

import sys
import xlrd
import re

def pinyin(word):
    book = xlrd.open_workbook('dict.xls')
    sheet1 = book.sheets()[0]


    word_l = []
    pinyin_t=[]
    pinyin_l=[]

    cop = re.compile("[^ㄅ-ㄩ^˙^ˊ^ˇ^ˋ^]")

    word_l = col_values = sheet1.col_values(2)
    pinyin_t=col_values = sheet1.col_values(6)

    for i in range(0,len(word_l)):
        if word == word_l[i]:
            pinyin_l.append(pinyin_t[i])
       
    temp_l = ["","","","","","",""]
    for i in range(0, len(pinyin_l)):
        if "(一)" == pinyin_l[i][0:3]:
            temp_l[0] =pinyin_l[i][3:]
        elif "(二)" == pinyin_l[i][0:3]:
            temp_l[1] =pinyin_l[i][3:]
        elif "(三)" == pinyin_l[i][0:3]:
            temp_l[2] =pinyin_l[i][3:]
        elif "(四)" == pinyin_l[i][0:3]:
            temp_l[3] =pinyin_l[i][3:]
        elif "(五)" == pinyin_l[i][0:3]:
            temp_l[4] =pinyin_l[i][3:]
        elif "(六)" == pinyin_l[i][0:3]:
            temp_l[5] =pinyin_l[i][3:]
        else :
            temp_l[6] =pinyin_l[i][0:]

    pinyin_l = []
    for i in range(0,len(temp_l)):
        if temp_l[i] == "" :
            continue   
        else:
            pinyin_l.append(cop.sub('',temp_l[i]))

    for i in range(0,len(pinyin_l)):
        print(pinyin_l)
        return pinyin_l

if __name__=="__main__":
    pinyin(sys.argv[1],sys.argv[2])







