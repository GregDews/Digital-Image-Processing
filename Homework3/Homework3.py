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


def imadjust(src, dst, tol, channel, vIn = (0,255), vOut = (0,255)):
    rows, cols = src.shape
    cv2.calcHist(src, [channel], None, [256], [0,255])
    # Stretching
    for r in range(rows):
        for c in range(cols):
            vs = max(src(r, c) - vIn[0], 0)
            vd = min(int(vs + 0.5) + vOut[0], vOut[1])
            dst[r, c, channel] = vd


# load the images
img = cv2.imread("face_dark.bmp")

# convert to luv 
luv = cv2.cvtColor(np.array(img).astype('float32')/255, cv2.COLOR_RGB2Luv)

L = luv[0]

range = np.amax(np.amax(L))
L = L / range
L2 = L
imadjust(L,L2,0.6,0)
L2 = L2 * range
L= L * range

luv[0] = L
cv2.imshow(L)
cv2.waitkey(0)

cv2.imshow(luv)
cv2.waitkey(0)

