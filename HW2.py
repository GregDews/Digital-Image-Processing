"""
Greg Dews
CS390S Digital Image Processing

Homework 1
1. Load an image (self made)
2. Convert to grey-scale image
3. Apply filters: Sobel, Laplacian, Median
4. Create your own filter not listed
5. Using iris.bmp, detect edge of pupil
    pupil should be ~35-45 pixels
    use thresholding and mask out noise in background
"""
from PIL import Image
import numpy as np
import cv2

# Load autumn, Create the nparray of greyscale
autumn = Image.open("PrincessAutumn.jpg").convert('L')
autumn.save("GreyAutumn.jpg")
img = cv2.imread("GreyAutumn.jpg",0)

# average
average_weights = np.array([
    [ 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1]])/25
out = cv2.filter2D(img, -1, average_weights)
average_autumn = Image.fromarray(out)
average_autumn.save("averageAutumn.jpg")

# sobel 
sobelx_weights = np.array([
    [ 1, 1, 1],
    [ 0, 0, 0],
    [-1,-1,-1]])

sobely_weights = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]])

out_x = cv2.filter2D(img,-1, sobelx_weights)
out_y = cv2.filter2D(img,-1, sobely_weights)
out = out_x + out_y
sobel_autumn = Image.fromarray(out)
sobel_autumn.save("SobelAutumn.jpg")

# laplacian
laplacian_weights = np.array([
    [-1,-1,-1,],
    [-1, 8,-1,],
    [-1,-1,-1,]])

out = cv2.filter2D(img, -1, laplacian_weights)
laplacian_autumn = Image.fromarray(out)
laplacian_autumn.save("LaplacianAutumn.jpg")

# iris processing
iris = cv2.imread( "iris.bmp", 0)
out_not_x = cv2.filter2D(iris,-1, sobelx_weights * (-1))
out_x = cv2.filter2D(iris,-1, sobelx_weights)
out_not_y = cv2.filter2D(iris,-1, sobely_weights * (-1))
out_y = cv2.filter2D(iris,-1, sobely_weights)
filtered = out_x + out_not_x + out_y + out_not_y
processed = cv2.filter2D(filtered, -1, average_weights)
processed_iris = Image.fromarray(processed, 'L')
processed_iris.save("ProcessedIris.jpg")
