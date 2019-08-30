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
    jieba.set_dictionary('../jieba_dict/dict.txt.big')
    # load stopwords set
    stopword_set = set()
    with open('../jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))
    model = gensim.models.Word2Vec.load('../word2vec_20190801.model')
    
    print ("=================Running " + sys.argv[1] + " to "+ sys.argv[2])
    input = sys.argv[1]
    output = sys.argv[2]
    with open(output, 'a', encoding='utf-8') as f :
        with open(input, 'r', encoding='utf-8') as f2 :
            for texts_num, line in enumerate(f2):
                line = line.strip('\n')
                line = cop.sub('', line)
                words = jieba.cut_for_search(line)                
                for word in words:
                    if word not in stopword_set:   
                        try:
                            semi = model.most_similar(word)
                        except KeyError:
                            continue
                        else:
                            for i in range(0,10):
                                word_ = model.most_similar(word)[i][0]
                                print (word_)
                                if word  == Converter('zh-hant').convert(word):
                                    word_ = Converter('zh-hant').convert(word_)
                                    f.write(word_ + ' ')                                    
                                else: 
                                    word_ = Converter('zh-hans').convert(word_)
                                    f.write(word_ + ' ')



if __name__ == "__main__":
    main()
