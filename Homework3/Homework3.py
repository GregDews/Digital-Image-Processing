"""
Greg Dews
CS-390S
Homework3
due: 10/06/98

To-Do: (suggested)
    Load images(color)

    convert to Yuv format
    hist(luminous component) and 1d filter for valley using 10 local neighbors{for(11:246)}
    threshold at calculated valley and pull out background
"""

import numpy as np
import cv2

# load the images
img = np.imread("yourface.jpg")

# will need to 