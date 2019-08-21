# -*- coding: utf-8 -*-

import gensim
model = gensim.models.Word2Vec.load('word2vec_20190801.model')

print (model.most_similar('牛肉'))
#print (model.similarity('女人', '男人'))



