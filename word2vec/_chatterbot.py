# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# Usage: python demo.py words
import sys
#demo.py must be utf-8

import gensim
model = gensim.models.Word2Vec.load('../word2vec_20190801.model')
input = sys.argv[1]
seg_list = jieba.cut(input, cut_all=False)

print(" ".join(seg_list))

list_key = ["商標、申請、註冊、流程、流程、時間、時間、多久、多久","個人、個人、申請、公司、公司、商標、名義","商標、彩色、黑白、墨色","商標、過、核准、核准、駁回、通過、通過"]

print(list_key[0])