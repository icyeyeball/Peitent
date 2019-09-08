# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190908
############################
# python _googles.py input

import sys
import xlrd
import re
import jieba
import gensim

book = xlrd.open_workbook('dict.xls')
sheet1 = book.sheets()[0]

cop = re.compile("[^\u4e00-\u9fa5^]")
    # jieba custom setting.
jieba.set_dictionary('../jieba_dict/dict.txt_new.big')

    # load stopwords set
stopword_set = set()
with open('../jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.strip('\n'))
        
model = gensim.models.Word2Vec.load('../word2vec_20190801.model')

input1 = sys.argv[1]
input2 = sys.argv[2]

word_l = []
meaning = []

cop = re.compile("[^\u4e00-\u9fa5^]")

word_l = col_values = sheet1.col_values(2)
meaning = col_values = sheet1.col_values(10)

with open('./inputs/1.txt', 'w', encoding='utf-8') as in1:
    for i in range(0,len(word_l)):
        if input1 == word_l[i]:
            line = meaning[i]
            line = cop.sub('', line)
            #in1.write(meaning[i])
            words = jieba.cut(line)
            for word in words:
                if word not in stopword_set:
                    in1.write(word + ' ')
            in1.write('\n')
print ("input1 finished")

with open('./inputs/2.txt', 'w', encoding='utf-8') as in2:
    for i in range(0,len(word_l)):
        if input2 == word_l[i]:
            line = meaning[i]
            line = cop.sub('', line)
            words = jieba.cut(line)
            for word in words:
                if word not in stopword_set:
                    in2.write(word + ' ')
            in2.write('\n')
print ("input2 finished")
index1 = 0
index2 = 0
weight_l = []
word_l1 = []
word_l2 = []
with open('./inputs/1.txt', 'r', encoding='utf-8') as f1:
    print ("Read f1")
    for texts_num1, line1 in enumerate(f1):
        words1 = jieba.cut(line1)
        for word1 in words1:
            try:
                semi = model.wv.most_similar(word1)
            except KeyError:
                continue
            else:
                index1 = index1 +1
                word_l1.append(word1)
                if index1>=20:
                    break
for i in word_l1:
    print (i)
    
with open('./inputs/2.txt', 'r', encoding='utf-8') as f2:
    print ("Read f2")
    for texts_num2, line2 in enumerate(f2):
        words2 = jieba.cut(line2)
        for word2 in words2:
            try:
                semi = model.wv.most_similar(word2)
            except KeyError:
                continue
            else:
                index2 = index2 +1
                word_l2.append(word2)
                if index2>=20:
                    break
for i in word_l2:
    print (i)
    
for i in word_l1:
    for j in word_l2:
        print(i +"  " +j)
        try:
            tmp = model.similarity(i, j)
        except KeyError:
            continue
        else:
            tmp = model.similarity(i, j)
            print (i +"  " +j + "  "+ str(tmp))
            weight_l.append(tmp)
            for a in range(0,len(weight_l)-1): 
                for b in range(0,len(weight_l)-1-a): 
                    if weight_l[b] < weight_l[b+1]: 
                        tmp = weight_l[b]
                        weight_l[b] = weight_l[b+1]
                        weight_l[b+1] = tmp
            if len(weight_l) > 20:
                del weight_l[20]

total = 0.0
for a in range(0,len(weight_l)):
    print (weight_l[a])
    total += weight_l[a]
total = total / len(weight_l)
print ("  total = " + str(total))                   





