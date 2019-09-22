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
from PIL import Image, ImageFilter
from scipy import ndimage
from math import sqrt
import numpy as np
import cv2

# Load autumn, Create the nparray of greyscale
autumn = Image.open("PrincessAutumn.jpg").convert('L')
autumn.save("GreyAutumn.jpg")
img = np.asarray(autumn, dtype='uint8')

# average
average_weights = np.array([
    [ 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1]])/25
out = ndimage.convolve(img, average_weights)
average_autumn = Image.fromarray(out, "L")
average_autumn.save("averageAutumn.jpg")

# sobel 
sobelx_weights = np.array([
    [ 2, 2, 2, 2, 2],
    [ 1, 1, 1, 1, 1],
    [ 0, 0, 0, 0, 0],
    [-1,-1,-1,-1,-1],
    [-2,-2,-2,-2,-2]])

sobely_weights = np.array([
    [ 2, 1, 0,-1,-2],
    [ 2, 1, 0,-1,-2],
    [ 2, 1, 0,-1,-2],
    [ 2, 1, 0,-1,-2],
    [ 2, 1, 0,-1,-2]])

out = ndimage.convolve(img, sobelx_weights)
sobel_autumn = Image.fromarray(out, 'L')
sobel_autumn.save("SobelAutumn.jpg")

# laplacian
laplacian_weights = np.array([
    [ 0, 0,-1, 0, 0],
    [ 0,-1,-2,-1, 0],
    [-1,-2,16,-2,-1],
    [ 0,-1,-2,-1, 0],
    [ 0, 0,-1, 0, 0]])
out = ndimage.convolve(img, average_weights)
out = ndimage.convolve(out, laplacian_weights)
laplacian_autumn = Image.fromarray(out, 'L')
laplacian_autumn.save("LaplacianAutumn.jpg")

# iris processing
iris = Image.open("iris.bmp").convert('L')
img = np.asarray(iris, dtype='uint8')
out_x = ndimage.convolve(img, sobelx_weights)
out_y = ndimage.convolve(img, sobely_weights)
out = out_x + out_y
sobel_iris = Image.fromarray(out, 'L')
sobel_iris.save("SobelIris.jpg")
