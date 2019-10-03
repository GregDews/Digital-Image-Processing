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
import numpy as np
import cv2

# load the images
img = np.read("face_dark.bmp")

# convert to luv 
luv = cv2.cvtColor(np.array(img).astype('float32')/255, cv2.COLOR_RGB2Luv)

L = luv[0]

range = cv2.max(cv2.max(L))
L = L / range
L2 = cv2.imadjust(L,[],[],0.6)
L2 = L2 * range
L= L * range

luv[0] = L
cv2.imshow(L)
cv2.waitkey(0)

cv2.imshow(luv)
cv2.waitkey(0)
