# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191119
############################
#
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
import imutils
import sys
import mysql.connector
import re
import shutil
from _dict_meaning import wordmeaning
from _dict_pic import *
from _dict_pinyin_offline import pinyin
import json
import time

#connect to database
tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
cursor=tmarkdb.cursor()
#cop = re.compile("[^.^/^A-Z^a-z^0-9^-]")
#cop = re.compile("[^\u4e00-\u9fa5^A-Z^a-z^ ^]")
cop = re.compile("[^\u4e00-\u9fa5^]")
copNo = re.compile("[^0-9^]")
#print(judge1)
#print(judge2)
# for instance: (1)"LIKE '45%'"  (2)"LIKE '%、45%'" (3)"LIKE '3519%'" (4)"LIKE '%、3519%'"
print("文+圖")
for i in range(1,46):
    if i < 10:
        i1 = str(0) + str(i)
    else:
        i1 = i
    for j in range(1,50):
        if j < 10:
            j1 = str(0) + str(j)
        else:
            j1 = j
        cmd_users = "SELECT tmarkName FROM tmarkTable WHERE goodsGroup LIKE '" + str(i1) + str(j1) + "%'"
        #print(cmd_users)
        cursor.execute(cmd_users)
        tmark_list11 = cursor.fetchall()
        cmd_users = "SELECT tmarkName FROM tmarkTable WHERE goodsGroup LIKE '%、" + str(i1) + str(j1) + "%'"
        cursor.execute(cmd_users)
        tmark_list12 = cursor.fetchall()
        cmd_users = "SELECT tmarkName FROM tmarkTable2 WHERE goodsGroup LIKE '" + str(i1) + str(j1) + "%'"
        cursor.execute(cmd_users)
        tmark_list21 = cursor.fetchall()
        cmd_users = "SELECT tmarkName FROM tmarkTable2 WHERE goodsGroup LIKE '%、" + str(i1) + str(j1) + "%'"
        cursor.execute(cmd_users)
        tmark_list22 = cursor.fetchall()
        cmd_users = "SELECT tmarkName FROM tmarkTable3 WHERE goodsGroup LIKE '" + str(i1) + str(j1) + "%'"
        cursor.execute(cmd_users)
        tmark_list31 = cursor.fetchall()
        cmd_users = "SELECT tmarkName FROM tmarkTable3 WHERE goodsGroup LIKE '%、" + str(i1) + str(j1) + "%'"
        cursor.execute(cmd_users)
        tmark_list32 = cursor.fetchall()
        cmd_users = "SELECT tmarkName FROM tmarkTable4 WHERE goodsGroup LIKE '" + str(i1) + str(j1) + "%'"
        cursor.execute(cmd_users)
        tmark_list41 = cursor.fetchall()
        cmd_users = "SELECT tmarkName FROM tmarkTable4 WHERE goodsGroup LIKE '%、" + str(i1) + str(j1) + "%'"
        cursor.execute(cmd_users)
        tmark_list42 = cursor.fetchall()
        #combine these two lists
        tmark_list11.extend(tmark_list12)
        tmark_list11.extend(tmark_list21)
        tmark_list11.extend(tmark_list22)
        tmark_list11.extend(tmark_list31)
        tmark_list11.extend(tmark_list32)
        tmark_list11.extend(tmark_list41)
        tmark_list11.extend(tmark_list42)
        tmark_list11 = list(set(tmark_list11))
        #if len(tmark_list11) !=0:
            #print(str(i1) + str(j1) + " 總筆數 : " + str(len(tmark_list11)))
        word1 = []
        for tmark in tmark_list11:
            word = cop.sub('', str(tmark[0]))
            if word.find("及圖") > 0:
                word1.append(1)
            elif word.find("及") > 0 and word.find("標章") > 0:
                word1.append(1)
            elif word.find("及") > 0 and word.find("標章圖") > 0:
                word1.append(1)

                 
        if len(tmark_list11) != 0:
            #print(str(i1) + str(j1) + " : " + str(len(word1)))
            print(str(len(word1)))
            
