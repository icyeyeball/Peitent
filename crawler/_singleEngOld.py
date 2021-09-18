# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190908
############################
# python _googles.py input

import sys
import pygame
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import math
import imutils

def wordsEng(word1, word2):
    a = 0
    weight_l = [[60,40,0,0,0,0,0,0,0,0,0,0],[45,30,25,0,0,0,0,0,0,0,0,0,0],[33,28,22,17,0,0,0,0,0,0,0,0],[28,24,20,16,12,0,0,0,0,0,0,0],[27,23,19,15,8,6,2,0,0,0,0,0],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1],[25,21,17,13,7,5,2,1,1,1,1,1]]
    #seperate word to lists
    word1_l = []
    word2_l = []
    #decide how many characters
    for i in range(len(word1),1,-1):
    #decide the first position
        for j in range(0,len(word1)-i+1):
            word1_l.append(word1[j:j+i])
    for i in range(len(word2),1,-1):
        for j in range(0,len(word2)-i+1):
            word2_l.append(word2[j:j+i])
    #to find out the word
    same = False
    flag = True
    if len(word1) > len(word2):
        long = len(word1)
    else:
        long = len(word2)
    
    for i in word1_l:
        for j in word2_l:
            if i == j:
                subword = i
                flag = False
                same = True
                npos1 = word1_l[0].find(subword)
                npos2 = word2_l[0].find(subword)
                leng_subword = len(subword)
                # Compare the total the same words
                if npos1>npos2:
                    pos = npos1
                else:
                    pos = npos2
                ends = pos+leng_subword
                if ends >10:
                    ends = 10
                a = 0
                for i in range(pos,ends):
                    a = a + weight_l[long][i]
                a = a * leng_subword/long*1.8
        if not flag:
            break

    return a


if __name__=="__main__":
    wordsEng(sys.argv[1],sys.argv[2],sys.argv[3])
