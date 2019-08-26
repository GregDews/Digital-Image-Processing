"""
Greg Dews
CS390S Digital Image Processing

Homework 1
"""
import numpy as np
import cv2

img = cv2.imread("NyanCat.PNG")
length = img.shape[0]
width = img.shape[1]

for i in range(length)
    for j in range(width)
        if (math.sqrt((i**2)+(j**2)) <= 80)
            img.item(i,j,0) = 255
            img.item(i,j,1) = 255
            img.item(i,j,2) = 255

img.show()
