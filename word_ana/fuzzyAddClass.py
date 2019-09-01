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
    
    print ("=================Running " + sys.argv[1] + " to "+ sys.argv[2])
    input = sys.argv[1]
    output = sys.argv[2]
    class_l = [""]
    with open(output, 'w', encoding='utf-8') as f :
        with open(input, 'r', encoding='utf-8') as f2 :
            for texts_num, line in enumerate(f2):
                line = line.strip('\n')
                line = cop.sub('', line)
                words = jieba.cut_for_search(line)                
                for word in words:
                    if word not in stopword_set:   
                        print ("**********************"+word)
                        try:
                            semi = model.wv.most_similar(word)
                        except KeyError:
                            continue
                        else:
                            print ("3333333333333333"+word)
                            print (str(len(class_l)))
                            for k in range(0,5):
                                print ("444444444444444444"+Converter('zh-hant').convert(word))
                                if Converter('zh-hant').convert(word) == class_l[k]:
                                        continue
                                else:
                                    word = Converter('zh-hant').convert(word) 
                                    print ("+++++++++++"+word+"+++++++++")
                                    print ("====="+word+"=====")
                                    class_l.append(word)
                                    print ("5555555555555555555555555555555"+class_l[len(class_l)-1])
                                    f.write(word + ' ')
                                    word = Converter('zh-hans').convert(word)
                                    f.write(word + ' ')
                                    
                                    for i in range(0,3):
                                        word_ = model.wv.most_similar(word,topn=3)[i][0]
                                        print ("66666666666666666666666666"+word_)
                                        for j in range(0,len(class_l)-1):                                
                                            if Converter('zh-hant').convert(word_) == class_l[j]:
                                                break
                                            else:
                                                class_l.append(word)
                                                f.write(word_ + ' ')    
                                                print (word_)                                
                                                word_ = Converter('zh-hans').convert(word_)
                                                f.write(word_ + ' ')
                                                print (word_)

if __name__ == "__main__":
    main()