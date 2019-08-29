# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# python s2zh.py inputfile outputfile

from langconv import *
import jieba
import logging

def Simplified2Traditional(sentence):
    
    sentence = Converter('zh-hant').convert(sentence)
    return sentence

final = ""
filename = sys.argv[1]
outname = sys.argv[2]
traditional_sentence = ""
simplified_sentence = ""
words_num=0

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info(sys.argv)
with open(filename,'r',encoding = 'utf-8') as f:
    for line in f.readlines():
        word = jieba.cut(line)
        for i in word:
            final = final + Simplified2Traditional(i) +" "
            words_num += 1
            if words_num % 10000 == 0:
                logging.info("已處理 %d 個文字" % words_num)

with open(outname, 'w', encoding = 'utf-8') as f2:
    f2.write(final)
    
f.close 
f2.close
