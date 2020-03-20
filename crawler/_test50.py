# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import sys
from _singleEng import *

word1_l = ["app","app","app","app","app","app","app","app","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc","abc"]
word2_l = ["age","pp","ap","apl","appl","apple","applle","oapde","abc","x","a","b","c","ab","bc","ba","cb","ax","xb","cx","xc","xy","xyz","xab","xbc","xac","axc","abx","cba","xba","xcb","abb","cab","abcx","xabc","cbax","xcba","abxy","xaby","xyab","bcxy","xbcy","xybc","aabc","aabx","abbc","abcc","xbbc","aaa","wxyz"]

for i in range(0,50):
    print(wordsEng(word1_l[i],word2_l[i]))
