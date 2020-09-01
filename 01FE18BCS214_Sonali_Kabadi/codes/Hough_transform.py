# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:34:45 2020

@author: Soanli Kabadi
Program: Canny Image 
"""
import cv2
import numpy as np
import math 


                               
def hough(img,C_I):
    
    size_I = img.shape
    
    dia = int(round(math.sqrt(size_I[0] * size_I[0] + size_I[1] * size_I[1])))
    
    score = np.zeros((2 *dia, 180), dtype=np.uint8)
    
    for i in range(size_I[0]):
        for j in range(size_I[1]):
            if img[i,j] == 255:
                for ti in range(0,180):
                    rho =  int(round(i * np.cos(ti * math.pi / 180) + j * np.sin(ti * math.pi / 180)))
                    score[rho, ti] += 1
    s =score.shape
    for rho in range(s[0]):
        for ti in range(s[1]):
            if score[rho,ti] > 100:
                a = np.cos(np.deg2rad(ti))
                b = np.sin(np.deg2rad(ti))
                x0 = (a * rho) 
                y0 = (b * rho) 
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                img = cv2.line(C_I,(x1,y1),(x2,y2),(0,0,255),2)
    #score[ score< avg] =0
    cv2.imwrite('C:/Users/HP/Desktop/transform.png',img)
    
      
                   
                    
I= cv2.imread('C:/Users/HP/Desktop/chess.jpg',0)
C_I =cv2.imread('C:/Users/HP/Desktop/chess.jpg') 
patch_size = [3,3]
I1 = cv2.Canny(I,50,150)
hough(I1,C_I)






