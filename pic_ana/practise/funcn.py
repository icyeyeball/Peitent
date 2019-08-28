# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
#
import sys
import cv2
import numpy as np
import imutils

def ROOTSIFT(grayIMG, kpsData):

    #extractor = cv2.xfeatures2d.SIFT_create()
    extractor = cv2.xfeatures2d.SURF_create()
    
    (kps, descs) = extractor.compute(grayIMG, kpsData)
    
    return (kps, descs)

def PIC_ANA(input1, input2):
    #detector = cv2.xfeatures2d.SURF_create() # Fast version of SIFT
    detector = cv2.xfeatures2d.SIFT_create()

    matcher = cv2.DescriptorMatcher_create("BruteForce")

    path1 = input1
    path2 = input2
    
    outpath = path1.replace('Input','Output',1)
    outpath = outpath[0:-4] + "_comp.jpg"

    imageA = cv2.imread(path1)
 
    imageB = cv2.imread(path2)

    imageA = imutils.resize(imageA, width = 600)

    imageB = imutils.resize(imageB, width = 600)
    
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
 
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    
    #grayA = cv2.Canny(grayA, 30, 150)
    #grayA = cv2.Canny(grayA, 30, 150)
    
    #grayB = cv2.Canny(grayB, 30, 150)
    
    grayA = cv2.GaussianBlur(grayA, (5, 5), 0)

    grayB = cv2.GaussianBlur(grayB, (5, 5), 0)  

    kpsA = detector.detect(grayA)

    kpsB = detector.detect(grayB)

    (kpsA, featuresA) = ROOTSIFT(grayA, kpsA)

    (kpsB, featuresB) = ROOTSIFT(grayB, kpsB)
    

    rawMatches = matcher.knnMatch(featuresA, featuresB, 2)

    matches = []

    i = 0.0
    m0 = 0.0
    m1 = 0.0
    for m in rawMatches:

        #print ("#1:{} , #2:{}".format(m[0].distance, m[1].distance))

        if len(m) == 2 and m[0].distance < m[1].distance * 0.7:
            matches.append((m[0].trainIdx, m[0].queryIdx))

        m0 += m[0].distance
        m1 += m[1].distance
        i += 1.0
    (hA, wA) = imageA.shape[:2]
  
    (hB, wB) = imageB.shape[:2]
    
    vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
    
    vis[0:hA, 0:wA] = imageA

    vis[0:hB, wA:] = imageB
  
    for (trainIdx, queryIdx) in matches:
 
        ptA = (int(kpsA[queryIdx].pt[0]), int(kpsA[queryIdx].pt[1]))

        ptB = (int(kpsB[trainIdx].pt[0] + wA), int(kpsB[trainIdx].pt[1]))
    
        cv2.line(vis, ptA, ptB, (np.random.randint(0, high=255),np.random.randint(0, high=255),np.random.randint(0, high=255)), 1)
    if i == 0.0:
        return (100.0, vis, i)
    else:    
        return ((m0+(m1*0.7))/i/2., vis, i)
    #cv2.imshow('My Image', vis)
    #cv2.waitKey(0)
    #cv2.imwrite(outpath, vis)
    #cv2.destroyAllWindows()