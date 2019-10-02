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
pic = Image.open("YourFace.jpg")
img = np.read(pic)



pic_LAB = img.convert("LAB")

