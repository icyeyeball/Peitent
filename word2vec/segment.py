# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# 

import jieba
import logging
import re

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    cop = re.compile("[^\u4e00-\u9fa5^ ^A-Z^a-z^]")
    # jieba custom setting.
    jieba.set_dictionary('../jieba_dict/dict.txt_new.big')

    # load stopwords set
    stopword_set = set()
    with open('../jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))

    output = open('../large_files/wiki_seg.txt', 'w', encoding='utf-8')
    with open('../large_files/wiki_texts.txt', 'r', encoding='utf-8') as content :
        for texts_num, line in enumerate(content):
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopword_set:
                    output.write(word + ' ')
            output.write('\n')

            if (texts_num + 1) % 10000 == 0:
                logging.info("已完成前 %d 行的斷詞" % (texts_num + 1))
    output.close()

if __name__ == '__main__':
    main()
