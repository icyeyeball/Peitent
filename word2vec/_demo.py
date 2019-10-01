# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# Usage: python demo.py words
import sys
sys.path.append(r'../PythonProject/langconv.py')
#demo.py must be utf-8

import gensim
model = gensim.models.Word2Vec.load('../word2vec_20190801.model')

print (model.wv.most_similar(sys.argv[1], topn=5))




