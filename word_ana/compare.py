# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# Usage: python demo.py words
import sys
import re
#demo.py must be utf-8

import gensim
model = gensim.models.Word2Vec.load('../word2vec_20190801.model')
cop = re.compile("[^\u4e00-\u9fa5^A-Z^a-z^ ^]")
with open('./class/45.txt','r', encoding='utf-8') as f:
    for line in f:
        line = line = cop.sub('', line)
        print (line)
        for word in line.split():
#print (model.most_similar(sys.argv[1]))
            print (word)
            print (model.similarity(sys.argv[1], word))
            print ("==============")



