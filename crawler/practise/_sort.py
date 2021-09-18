# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
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


tmark_list1 = [("0","0.1"), ("1","1.1"), ("2","2")]
tmark_list2 = [ ("0","0.1"), ("3","3"),("5","5.5")]
tmark_list1.extend(tmark_list2)
tmark_list1 = list(set(tmark_list1))
print (tmark_list1)
    
    
    