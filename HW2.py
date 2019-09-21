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
import numpy as np

# Load images, Create the nparray of greyscale
iris = Image.open("iris.bmp").convert('L')

autumn = Image.open("PrincessAutumn.jpg").convert('L')
autumn.save("GreyAutumn.jpg")
autumn = autumn.filter(ImageFilter.GaussianBlur)
autumn.save("GaussianAutumn.jpg")
img = np.asarray(autumn, dtype='uint8')

# sobel
sobelx_weights = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]])

sobely_weights = np.array([
        [-1,-1,-1],
        [ 0, 0, 0],
        [ 1, 1, 1]])

x_out = ndimage.convolve(img, sobelx_weights)
y_out = ndimage.convolve(img, sobely_weights)
out = (x_out + y_out)
sobel_autumn = Image.fromarray(out, 'L')
sobel_autumn.save("SobelAutumn.jpg")

# laplacian
#laplacian_autumn = Image.new("L", autumn.size)
laplacian_weights = np.array([
        [-1,-1, -1],
        [-1, 8, -1],
        [-1,-1, -1]])
out = ndimage.convolve(img, laplacian_weights)
laplacian_autumn = Image.fromarray(out, 'L')
laplacian_autumn.save("LaplacianAutumn.jpg")

# median
#median_autumn = Image.new("L", autumn.size)
median_weights = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]])/9
out = ndimage.convolve(img, median_weights)
median_autumn = Image.fromarray(out, "L")
median_autumn.save("MedianAutumn.jpg")