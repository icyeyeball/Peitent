# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import sys
from _singleEng import *

word1_l = []
word2_l = []

f = open(r'./A.txt', encoding='utf-8')
for line in f:
    word1_l.append(line.strip("\n"))

f = open(r'./B.txt', encoding='utf-8')
for line in f:
    word2_l.append(line.strip("\n"))
    

print(len(word1_l))
print(len(word2_l))
print(word1_l)
print(word2_l)
for i in range(0,len(word1_l)):
    print(wordsEng(word1_l[i],word2_l[i]))
    

