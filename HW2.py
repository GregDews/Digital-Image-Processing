"""
Greg Dews
CS390S Digital Image Processing

Homework 1
1. Load an image
2. Create a grey-scale image
3. Edit individual pixels using a for-loop to add a round frame
4. Save image for report
"""
from PIL import Image
import math

# Load image, Create the pixel map
im = Image.open("iris.bmp")
iris_pixels = im.load()

# Basic info
length = img.size[1]
width = img.size[0]

# What's next
