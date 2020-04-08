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
    weight_l = [[60,40,0,0,0,0,0,0,0,0,0,0],[45,30,25,0,0,0,0,0,0,0,0,0,0],[33,28,22,17,0,0,0,0,0,0,0,0],[28,24,20,16,12,0,0,0,0,0,0,0],[27,23,19,15,8,6,2,0,0,0,0,0],[25,21,17,13,7,5,2,1,1,1,1,1],[23,19,15,11,9,7,4,2,1,1,1,1],[21,17,13,9,8,7,5,3,2,2,1,1],[19,16,13,9,8,7,5,4,3,2,2,1],[19,16,13,9,8,7,5,4,3,2,2,1],[19,16,13,9,8,7,5,4,3,2,2,1],[19,16,13,9,8,7,5,4,3,2,2,1],[19,16,13,9,8,7,5,4,3,2,2,1],[19,16,13,9,8,7,5,4,3,2,2,1],[19,16,13,9,8,7,5,4,3,2,2,1],[19,16,13,9,8,7,5,4,3,2,2,1],[19,16,13,9,8,7,5,4,3,2,2,1]]
    #seperate word to lists
    word1_l = []
    word2_l = []
    if len(word1)>len(word2):
        wordMax = word1
        wordmin = word2
    else:
        wordMax = word2
        wordmin = word1
    wordmin_min = math.ceil(len(wordmin)*0.66)
    wordmin_max = math.ceil(len(wordmin)*1.00)
    if wordmin_min < 1:
        wordmin_min = 1
    
    #decide how many characters
    for i in range(0,len(word1)):
    #decide the first position
        word1_l.append(word1[i:i+1])
    for i in range(0,len(word2)):
        word2_l.append(word2[i:i+1])
    
    n_char = 0
    same = False
    for i in word1_l:
        for j in word2_l:
            #print(word1_l)
            #print(word2_l)
            if word1_l[-1].strip() == "" or word1_l[-1].strip() == "":
                break
                break
            if i == j and i.strip() != '' :
                #print("i = " + i)
                #print("j = " + j)
                npos1_t = word1_l.index(i)
                npos2_t = word2_l.index(j)
                #print("npos1_t=" + str(npos1_t))
                #print("npos2_t=" + str(npos2_t))

                if same == False:
                    npos1 = word1_l.index(i)
                    npos2 = word2_l.index(j)
                same = True
                n_char = n_char + 1
                for x in range(0,npos1_t+1):
                    word1_l[x] = ""
                for y in range(0,npos2_t+1):
                    word2_l[y] = ""
                i = ""
                j = ""
    #print("n_char = "+str(n_char))
    #if n_char>=wordmin_min and n_char<=wordmin_max:
    if n_char>=1 and n_char<=wordmin_max:
        #to find out the word
        #print(word1 + ":" + word2)
        if len(word1) > len(word2):
            long = len(word1)
        else:
            long = len(word2)
            # Compare the total the same words
        if npos1>npos2:
            pos = npos1
        else:
            pos = npos2
        ends = pos+n_char
        if ends >10:
            ends = 10
        a = 0
        for i in range(pos,ends):
            a = a + weight_l[long-1][i]
            #print("pa="+str(a))
        #print("long="+str(long))    
        a = a * n_char*2./(long+abs(npos1-npos2))
        #a = a * n_char*2./long
        return a
    else:
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
                        a = a + weight_l[long-1][i]
                    a = a * leng_subword*1.8/long
            if not flag:
                break
        return a


if __name__=="__main__":
    wordsEng(sys.argv[1],sys.argv[2],sys.argv[3])
