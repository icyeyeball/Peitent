# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# 

import jieba
import logging
import sys
import gensim
from langconv import *


def main():
    model = gensim.models.Word2Vec.load('../word2vec_20190801.model')
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        with open("../jieba_dict/dict.txt_new.big", 'r', encoding='utf-8') as f2:
            for line in f:
                words = line.split()
                for word in words:
                    with open("../large_files/wiki_seg.txt", 'r', encoding='utf-8') as f3:
                        if word in f3.read()
                            pass
                        else:
                            continue
                    for i in range(0,10):
                        print("====================")
                        print (word)
                        word_ = model.most_similar(word)[i][0]
                        if word  == Converter('zh-hant').convert(word):
                            word_ = Converter('zh-hant').convert(word_)
                        else: 
                               word_ = Converter('zh-hans').convert(word_)
                        print (word_)

                
if __name__ == '__main__':
    main()
