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
    weight_l = [[60,40,0,0,0,0,0,0,0,0,0,0],[45,30,25,0,0,0,0,0,0,0,0,0,0],[40,28,22,10,0,0,0,0,0,0,0,0],[37,30,24,5,4,0,0,0,0,0,0,0],[35,29,23,13,10,3,0,0,0,0,0,0],[33,26,20,10,6,4,1,0,0,0,0,0],[30,24,18,9,7,5,4,3,0,0,0,0],[30,24,18,9,7,5,4,2,1,0,0,0],[30,24,18,9,7,5,4,1,1,1,0,0],[30,24,18,9,7,5,3,1,1,1,1,0],[30,24,18,9,6,5,3,1,1,1,1,1],[30,24,18,9,6,5,3,1,1,1,1,1],[30,24,18,9,6,5,3,1,1,1,1,1],[30,24,18,9,6,5,3,1,1,1,1,1],[30,24,18,9,6,5,3,1,1,1,1,1],[30,24,18,9,6,5,3,1,1,1,1,1],[30,24,18,9,6,5,3,1,1,1,1,1]]
    #seperate word to lists
    if len(word1) == 0 or len(word2) == 0:
        return -1.0
    if len(word1)>len(word2):
        wordMax = word1
        wordmin = word2
    else:
        wordMax = word2
        wordmin = word1
    wordmin_min = math.ceil(len(wordmin)*0.66)
    wordmin_max = math.ceil(len(wordmin)*1.50)
    if wordmin_min < 1:
        wordmin_min = 1
    if len(wordMax)<wordmin_min or len(wordMax)>wordmin_max:
        return -1.0

    
    #decide how many characters
    word1_l = []
    word2_l = []
    for i in range(0,len(word1)):
    #decide the first position
        word1_l.append(word1[i:i+1])
    for i in range(0,len(word2)):
        word2_l.append(word2[i:i+1])
    depends = []
    depends2 = []
    dependst = []
    depends2t = []
    dependsii = []
    if len(word1_l)<=len(word2_l):
        depends = word1_l.copy()
        depends2 = word2_l.copy()
        dependst = word1_l.copy()
        depends2t = word2_l.copy()
    else:
        depends = word2_l.copy()
        depends2 = word1_l.copy()
        dependst = word2_l.copy()
        depends2t = word1_l.copy()
    #print(depends)
    #print(depends2)
        
    p1_l = []
    p2_l = []
    p1_lt = []
    p2_lt = []
    p1_total = 0
    p2_total = 0
    p1_totalt = 0
    p2_totalt = 0
    total_max = 0
    total_min = 0
    dependsii = depends.copy()
    n_char = 0
    same = False
    p1 = 0
    p2 = 0
    for ii in range(0,len(dependsii)):
        depends = dependst.copy()
        depends2 = depends2t.copy()
        n_char_t = 0
        p1_lt = []
        p2_lt = []
        for i in range(ii,len(depends)):
            for j in range(0,len(depends2)):
                if depends[-1].strip() == "" or depends2[-1].strip() == "":
                    break
                    break
                if depends[i] == depends2[j] and depends[i].strip() != "" :
                    same = True
                    n_char_t = n_char_t + 1
                    p1_lt.append(i)
                    p2_lt.append(j)
                    for x in range(0,i+1):
                        depends[x] = ""
                    for y in range(0,j+1):
                        depends2[y] = ""
                    #print(depends)
                    #print(depends2)
        if same == True and p1_l == [] and p2_l == []:
            p1_l = p1_lt.copy()
            p2_l = p2_lt.copy()
            #print("p1_l & p2_l")
            #print(p1_l)
            #print(p2_l)
            #print(p1_l)
            #print(p2_l)
            p1_total = 0
            p2_total = 0
            for p in p1_l:
                p1_total = p1_total + p
            p1_total = (p1_total/n_char_t) - 0.5*(n_char-1)
            for p in p2_l:
                p2_total = p2_total + p
            p2_total = (p2_total/n_char_t) - 0.5*(n_char-1)
            n_char = n_char_t
        #elif same == True and n_char_t > 0:
        elif n_char_t > 0:
            p1_total = 0
            p2_total = 0
            p1_totalt = 0
            p2_totalt = 0
            for p in p1_l:
                p1_total = p1_total + p
            p1_total = (p1_total/n_char) - 0.5*(n_char-1)
            for p in p2_l:
                p2_total = p2_total + p
            p2_total = (p2_total/n_char) - 0.5*(n_char-1)
            
            for p in p1_lt:    
                p1_totalt = p1_totalt + p
            p1_totalt = (p1_totalt/n_char_t) - 0.5*(n_char_t-1)
            for p in p2_lt:    
                p2_totalt = p2_totalt + p
            p2_totalt = (p2_totalt/n_char_t) - 0.5*(n_char_t-1)
            
            if (p1_totalt+p2_totalt)<(p1_total+p2_total):
                p1_l = p1_lt.copy()
                p2_l = p2_lt.copy()
                p1_total = p1_totalt
                p2_total = p2_totalt
                n_char = n_char_t
                #print("p1_l & p2_l")
                #print(p1_l)
                #print(p2_l)
            else:
                pass
    if len(dependst)<4 or len(depends2t)<4:
        if len(p1_l) == 0:
            return -1.0
                    #print("p1_l & p2_l")
                    #print(p1_l)
                    #print(p2_l)
            #else:
                #return 0.0
        p_max_avg = 0
        p_min_avg = 0
        p_l_max = []
        p_l_min = []
        if p1_total>p2_total:
            p_max_avg = p1_total
            p_min_avg = p2_total
            p_l_max = p1_l.copy()
            p_l_min = p2_l.copy()
        else:
            p_max_avg = p2_total
            p_min_avg = p1_total
            p_l_max = p2_l.copy()
            p_l_min = p1_l.copy()
        #print("p_l_max & p_l_min")
        #print(p1_l)
        #print(p2_l)
        c_noise = 0
        for i in range(0,n_char):
            if i + 1 < n_char:
                c_noise = c_noise + ((p_l_max[i+1]-p_l_max[i])-(p_l_min[i+1]-p_l_min[i]))
            else:
                break
        c_noise = abs(c_noise)
        d_noise = math.pow(0.9,c_noise)
        m_i = 0
        h_i = 0
        q_i = 0
        y_total = 0
        for i in range(0,len(p_l_min)):
            m_i = p_min_avg + i + 1
            #print("p_min_avg = " + str(p_min_avg))
            #print("m_i = " + str(m_i))
            if len(dependst) <= 5:
                if m_i < 2 or (m_i >= 4 and m_i < 5):
                    h_i = 0.05
                    f_i = 0.927 - (0.184 * m_i)
                    g_i = 0.522 - (0.241*m_i) + (0.031*math.pow(m_i,2))
                    q_i = h_i + f_i - g_i*math.log(len(dependst))
                    y_total = y_total + q_i
                elif m_i >=2 and m_i < 4:
                    h_i = -0.05
                    f_i = 0.927 - (0.184 * m_i)
                    g_i = 0.522 - (0.241*m_i) + (0.031*math.pow(m_i,2))
                    q_i = h_i + f_i - g_i*math.log(len(dependst))
                    y_total = y_total + q_i
                elif m_i == 5:
                    q_i = 0.11
                    y_total = y_total + q_i
                else:
                    pass
            elif len(dependst) > 5:    
                if m_i < 5:
                    h_i = 0.0
                    f_i = 0.927 - (0.184 * m_i)
                    g_i = 0.522 - (0.241*m_i) + (0.031*math.pow(m_i,2))
                    q_i = h_i + f_i - g_i*math.log(6)
                    y_total = y_total + q_i
                elif m_i >= 5:
                    q_i = 0.22/(len(dependst)-4)
                    y_total = y_total + q_i
                else:
                    pass
        if len(dependsii)+abs(p1_l[0]-p2_l[0]) > 0:
            r = n_char/(len(wordMax)+abs(p1_l[0]-p2_l[0]))
            #print("r = " + str(n_char) + "/(" + str(len(depends2t)) + "+" + str(abs(p1_l[0]-p2_l[0])) + ")" + " = " + str(r))
        else:
            r = 0.01
        #print("r = " + str(r))
        #print("a = " + str(y_total) + "*" + str(d_noise) + "*" + str(r) + "*" + str(1.25))
        a = y_total * d_noise * r * 1.25
        return a*100
    else:
 
        """
        same = False
        for i in p1_l:
            for j in p2_l:
                #print(word1_l)
                #print(word2_l)
                if p1_l[-1].strip() == "" or p2_l[-1].strip() == "":
                    break
                    break
                if i == j and i.strip() != "":
                    #print("i = " + i)
                    #print("j = " + j)
                    npos1_t = p1_l.index(i)
                    npos2_t = p2_l.index(j)
                    #print("npos1_t=" + str(npos1_t))
                    #print("npos2_t=" + str(npos2_t))
                    
                    if same == False:
                        npos1 = p1_l.index(i)
                        npos2 = p2_l.index(j)
                    same = True
                    n_char = n_char + 1
                    for x in range(0,npos1_t+1):
                        word1_l[x] = ""
                    for y in range(0,npos2_t+1):
                        word2_l[y] = ""
                    i = ""
                    j = ""
        """
                    
        #to find out the word
        #print(word1 + ":" + word2)
        if len(p1_l) == 0:
            return 0.0
        #print("word1 : word2 = " + word1+ ":" + word2)

        if len(word1) > len(word2):
            long = len(word1)
            #print("p1_l:")
            #print(p1_l)
        else:
            long = len(word2)

        #print("others = " + str(others))
            # Compare the total the same words
        if p1_l[0] > p2_l[0]:
            pos = p1_l[0]
            pos_l = p1_l.copy()
        else:
            pos = p2_l[0]
            pos_l = p2_l.copy()
        others = 0
        for i in range(0,len(p1_l)):
            if (i+1) < len(p1_l):
                others = others + (p1_l[i+1]-p1_l[i]-1)
        for i in range(0,len(p2_l)):
            if (i+1) < len(p2_l):
                others = others + (p2_l[i+1]-p2_l[i]-1)
        others = others/2.0
        a = 0
        #print("others = " + str(others))
        #print("n_char = " + str(n_char))
        ends = pos+n_char
        for i in range(pos,ends):
            if i <12:
                a = a + weight_l[long-2][i]
        #print("long="+str(long))

        a = a * n_char*1.3/(long+others)
        #print("n_char = " + str(n_char))
        #print("long = " + str(long))
        #a = a * n_char*2./long
        return a


if __name__=="__main__":
    wordsEng(sys.argv[1],sys.argv[2],sys.argv[3])
