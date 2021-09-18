# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190829
############################
# 

import jieba
import sys
import re

def main():

    # jieba custom setting.
    jieba.set_dictionary('../jieba_dict/dict.txt_new.big')
     
    # load stopwords set
    stopword_set = set()
    with open('../jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))
    print ("====================Running " + sys.argv[1] +" to "+ sys.argv[2])
    output = open(sys.argv[2], 'w', encoding='utf-8')
    cop = re.compile("[^\u4e00-\u9fa5^ ^A-Z^a-z^]")
    class_l=[]
    with open(sys.argv[1], 'r', encoding='utf-8') as content :
        for texts_num, line in enumerate(content):
            line = line.strip('\n')
            line = cop.sub('', line)
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopword_set:
                    for i in range(0,len(class_l)):
                        continue
                    else:
                        output.write(word + ' ')
    output.write('\n')
    output.close()

if __name__ == '__main__':
    main()