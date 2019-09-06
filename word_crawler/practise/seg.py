# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190826
############################
# 

import jieba
import logging

def seg():

    # jieba custom setting.
    jieba.set_dictionary('./jieba_dict/dict.txt.big')

    # load stopwords set
    stopword_set = set()
    with open('./jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))

    output = open('./google_seg.txt', 'w', encoding='utf-8')
    with open('./google.txt', 'r', encoding='utf-8') as content :
        for texts_num, line in enumerate(content):
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopword_set:
                    output.write(word + ' ')
            output.write('\n')
    output.close()

if __name__ == '__main__':
    main()
