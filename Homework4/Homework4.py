"""
Greg Dews
CS390S
Homework 4

1. Generate 256x256 gray image with only 2 intensities
    0.4 and 0.7 of intensity
    80 pixel radius circle

2. Generate three types of noise
        Gaussian mean=0 variance=0.1

    add noise
    histogram these images
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

im = np.image

