# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# Usage: python demo.py words
import sys
#demo.py must be utf-8

import gensim
model = gensim.models.Word2Vec.load('../word2vec_en_20190801.model')

#print (model.most_similar(sys.argv[1]))
print (model.similarity(sys.argv[1], sys.argv[2]))



