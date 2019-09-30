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

# median filter
def median_filter(arr):
    #Pad image with copy of bordering pixels
    padded = cv2.copyMakeBorder(
        arr, 1, 1, 1, 1, cv2.BORDER_REFLECT, None)

    width = len(padded) - 1
    length = len(padded[0]) - 1
    pix = [0]*9
    for i in range(1,width):
        for j in range(1,length):
            pix[0] = padded[i-1][j-1]
            pix[1] = padded[i][j-1]
            pix[2] = padded[i+1][j-1]
            pix[3] = padded[i-1][j]
            pix[4] = padded[i][j]
            pix[5] = padded[i+1][j]
            pix[6] = padded[i-1][j+1]
            pix[7] = padded[i][j+1]
            pix[8] = padded[i+1][j+1]
            arr[i-1][j-1] = sorted(pix)[4]
    return arr

(Image.fromarray(median_filter(img), 'L')).save("median_autumn.jpg")

# iris processing
iris = cv2.imread("iris.bmp", 0)
median_iris = median_filter(iris)
out_not_x = cv2.filter2D(median_iris,-1, sobelx_weights * (-1))
out_x = cv2.filter2D(median_iris,-1, sobelx_weights)
out_not_y = cv2.filter2D(median_iris,-1, sobely_weights * (-1))
out_y = cv2.filter2D(median_iris,-1, sobely_weights)
filtered = out_y + out_not_y + out_x + out_not_x
wasted_var, threshed = cv2.threshold(filtered, 145, 255, cv2.THRESH_BINARY)

brow_mask = np.zeros(iris.shape, np.uint8)
width, height = brow_mask.shape
for i in range(width):
    for j in range(height):
        dist = np.sqrt((i-width/2)**2+(j-height/2)**2)
        if dist < 60:
            brow_mask[i][j] = 1
processed = threshed * brow_mask

processed_iris = Image.fromarray(processed, 'L')
processed_iris.save("ProcessedIris.jpg")
