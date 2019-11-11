"""
Greg Dews
CS-390S
Homework3
due: 10/06/98

To-Do: (suggested)
    Load images(color)

    convert to Yuv format
    hist(luminous component) and 1d filter for valley using 10 local neighbors{for(11:246)}
    threshold at calculated valley and mask out background

"""
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import cv2


def detect_face(image):
    width, height, depth = image.shape[0:3]
    result = np.zeros((width, height, depth))
    RED = image[:,:,2]
    GREEN = image[:,:,1]
    BLUE = image[:,:,0]
    for j in range(width):
        for k in range(height):
            red = int(RED[j][k])
            grn = int(GREEN[j][k])
            blu = int(BLUE[j][k])
            rgb = [red, grn, blu]
            rvg = (abs(red - grn) > 15) and (red > grn)
            if (red > 95) and (grn > 40) and (blu > 20) and (max(rgb) - min(rgb) > 15) and rvg and (red > blu):
                result[j][k][0:3] = image[j][k][0:3]
            else:
                result[j][k][0:3] = 0
    result = np.uint8(result)
    luv_img = cv2.cvtColor(result, cv2.COLOR_BGR2Luv)
    hgram = np.zeros(256)
    for m in range(width):
        for n in range(height):
            hgram[luv_img[m][n][0]] += 1
    hsversion = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    thold = otsu_thresh(hgram)
    for m in range(width):
        for n in range(height):
            if hsversion[m][n][1] > thold: 
                result[m][n][0:3] = image[m][n][0:3]
            else:
                result[m][n][0:3] = 0
    result = np.uint8(result)
    return result


def otsu_thresh(hist):
    total_px = sum(hist)
    wcv = {}
    for t in range(256):
        w_b = sum(hist[0:t])/total_px
        w_f = sum(hist[t:256])/total_px
        mu_b = 0
        mu_f = 0
        var_b = 0
        var_f = 0

        for m in range(t):
            mu_b += (m * hist[m])
        mu_b /= max(sum(hist[0:t]), 1)
        for v in range(t):
            var_b += (v-mu_b)**2 * hist[v]
        var_b /= max(sum(hist[0:t]), 1)

        for m in range(t, 256):
            mu_f += (m * hist[m])
        mu_f /= max(sum(hist[t:256]), 1)
        for v in range(t, 256):
            var_f += (v-mu_f)**2 * hist[v]
        var_f /= max(sum(hist[t:256]), 1)

        wcv[t] = (w_b * var_b) + (w_f * var_f)
        index_min = 255
    for x in range(256):
        if wcv[x] < wcv[index_min]:
            index_min = x
    return index_min

im = cv2.imread("me1.bmp")
mydetect1 = detect_face(im)
cv2.imwrite("me1_filtered.png", cv2.cvtColor(mydetect1, cv2.COLOR_BGR2GRAY))

im2 = cv2.imread("me2.bmp")
mydetect2 = detect_face(im2)
cv2.imwrite("me2_filtered.png", cv2.cvtColor(mydetect2, cv2.COLOR_BGR2GRAY))

im3 = cv2.imread("me3.bmp")
mydetect3 = detect_face(im3)
cv2.imwrite("me3_filtered.png", cv2.cvtColor(mydetect3, cv2.COLOR_BGR2GRAY))

im4 = cv2.imread("me4.bmp")
mydetect4 = detect_face(im4)
cv2.imwrite("me4_filtered.png", cv2.cvtColor(mydetect4, cv2.COLOR_BGR2GRAY))

im5 = cv2.imread("me5.bmp")
mydetect5 = detect_face(im5)
cv2.imwrite("me5_filtered.png", cv2.cvtColor(mydetect5, cv2.COLOR_BGR2GRAY))

