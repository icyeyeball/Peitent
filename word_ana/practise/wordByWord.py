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

def main():
    cop = re.compile("[^\u4e00-\u9fa5^ ^A-Z^a-z^]")
    # jieba custom setting.
    jieba.set_dictionary('../jieba_dict/dict.txt_new.big')
    # load stopwords set
    stopword_set = set()
    with open('../jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))
    model = gensim.models.Word2Vec.load('../word2vec_20190801.model')
    
    class_l = []
    with open('1.txt', 'r', encoding='utf-8') as f2 :
        for texts_num, line in enumerate(f2):
            line = line.strip('\n')
            line = cop.sub('', line)
            words = jieba.cut_for_search(line)
            for word in words:
                if word not in stopword_set:   
                    try:
                        semi = model.wv.most_similar(word)
                    except KeyError:
                        continue
                    else:
                        class_l.append(word)
                        print (word)
        print(class_l[5])
                         

if __name__ == "__main__":
    main()