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
jieba.set_dictionary('../jieba_dict/dict.txt_new.big')
# load stopwords set
stopword_set = set()
with open('../jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.strip('\n'))
model = gensim.models.Word2Vec.load('../word2vec_20190801.model')
        
input = sys.argv[1]
for i in range(0,len(input)):
    for j in range(0,len(input)-i):
        try:
            semi = model.wv.most_similar(input[j:j+i+1])
        except KeyError:
            print ("XXXXXXXXX input " + input[j:j+i+1])
            continue
        else:
            print ("OOOOOOO input " + input[j:j+i+1])
            