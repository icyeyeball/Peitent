# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL
import random
q=0
while(q<50):
    q+=1
    a=[]
    while len(a)<4:
        a.append(int(random.random()*10))
        for i in range(len(a)):
            for j in range(len(a)):
                if i != j:
                    if a[i] ==a[j]:
                        while a[i] in a[0:i]:
                            a[i] = int(random.random()*10)
    print(a)