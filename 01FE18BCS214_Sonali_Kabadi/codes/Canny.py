
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 11:34:45 2020

@author: Soanli Kabadi
Program: Canny Image 
"""
import cv2
import numpy as np
                       
                               
def guassian(I,patch_size):
    size_I = I.shape
    patch = [[1,2,1],[2,4,2],[1,2,1]]
    op_matrix = np.zeros([size_I[0]-2,size_I[1]-2])
    
    for i in range(0,size_I[0]-2):
        for j in range(0,size_I[1]-2):
            op=np.zeros(patch_size)
            for k in range(patch_size[0]):
                for l in range(patch_size[1]):
                    op[k,l]=I[i+k,j+l]
            temp = np.sum(op*patch)
            temp = temp/16
            op_matrix[i,j] = temp
    return op_matrix

def sobelv(I,patch_size):
    size_I = I.shape
    patch =[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    op_matrix = np.zeros([size_I[0]-2,size_I[1]-2])
    
    for i in range(0,size_I[0]-patch_size[0]-1):
        for j in range(0,size_I[1]-patch_size[1]-1):
            op=np.zeros(patch_size)
            for k in range(patch_size[0]):
                for l in range(patch_size[1]):
                    op[k,l]=I[i+k,j+l]
            temp = np.sum(patch*op)
            temp = temp/8
            op_matrix[i,j] = temp
    return op_matrix       

def sobelh(I,patch_size):
    size_I = I.shape
    patch = [[-1,-2,-1],[0,0,0],[1,2,1]]
    op_matrix = np.zeros([size_I[0]-2,size_I[1]-2])
    
    for i in range(0,size_I[0]-2):
        for j in range(0,size_I[1]-2):
            op=np.zeros(patch_size)
            for k in range(patch_size[0]):
                for l in range(patch_size[1]):
                    op[k,l]=I[i+k,j+l]
            temp = np.sum(patch*op)
            temp = temp/8
            op_matrix[i,j] = temp
    return op_matrix

def lap(I,patch_size):
    size_I = I.shape
    patch = [[0,1,0],[1,-4,1],[0,1,0]]
    op_matrix = np.zeros([size_I[0]-2,size_I[1]-2])
    
    for i in range(0,size_I[0]-patch_size[0]-1):
        for j in range(0,size_I[1]-patch_size[0]-1):
            op=np.zeros(patch_size)
            for k in range(0,patch_size[0]):
                for l in range(0,patch_size[1]):
                    op[k,l]=I[i+k,j+l]
            temp = np.sum(op*patch)
            #temp = temp/9
            op_matrix[i,j] = temp
    return op_matrix
    
def hyteresis(I):
    size_I = I.shape
    img = np.copy(I)
    highThreshold = np.max(img) * 0.32
    lowThreshold = np.max(img)  * 0.15
    x1 = 1
    x2=0
    while(x2!= x1):            #while loop runs until x1 and x2 are eual to sum of image
        x2 = x1
        for i in range(0,size_I[0]):
            for j in range(0,size_I[1]):
                if(img[i,j] > highThreshold):#if pixel value is greater than high threshold we keep it
                    img[i,j] = 255
                elif(img[i,j] < lowThreshold):#if pixel value is greater than high threshold we discard it
                    img[i,j] = 0
                #if the pixel is between two thresholds,neighbouring pixel value is checked.
                else:
                    if((img[i-1,j-1] > highThreshold) or (img[i-1,j] > highThreshold) or(img[i-1,j+1] > highThreshold) or(img[i,j-1] > highThreshold) or(img[i,j+1] > highThreshold) or(img[i+1,j-1] > highThreshold) or(img[i+1,j] > highThreshold) or(img[i+1,j+1] > highThreshold)):
                        img[i,j] = 255
                    else:
                        img[i,j]= 0
                x1 = np.sum(img )
    return img
I= cv2.imread('C:/Users/HP/Desktop/lena.jfif',0)

patch_size = [3,3]
I1 = guassian(I,patch_size)
#cv2.imwrite('C:/Users/HP/Desktop/Guassian_image.png',I1)

I4 = sobelv(I1,patch_size)
#cv2.imwrite('C:/Users/HP/Desktop/Sobel_x-axis.png',I4)

I5 = sobelh(I1,patch_size)
#cv2.imwrite('C:/Users/HP/Desktop/Sobel_y-axis.png',I5)

I2 = lap(I1,patch_size)
#cv2.imwrite('C:/Users/HP/Desktop/l.png',I2)
I6 = np.hypot(I4,I5)
I3 = hyteresis(I6)
cv2.imwrite('C:/Users/HP/Desktop/Canny123.png',I3)