"""
Greg Dews
CS390S Digital Image Processing

Homework 1
1. Load an image (self made)
2. Convery to grey-scale image
3. Apply filters: Sobel, Laplacian, Median
4. Create your own filter not listed
5. Using iris.bmp, detect edge of pupil
    pupil should be ~35-45 pixels
    use thresholding and mask out noise in background
"""
from PIL import Image

# Load image, Create the pixel map
im = Image.open("iris.bmp").convert('LA')
iris_pixels = im.load()

# Basic info
length = im.size[1]
width = im.size[0]

# What's next
