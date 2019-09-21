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

# Load images, Create the pixel map
iris = Image.open("iris.bmp").convert('L')
#iris_pixels = im.load()
autumn = Image.open("PrincessAutumn.jpg").convert('L')
autumn.save("GreyAutumn.jpg")

img = ndimage.imread("GreyAutumn.jpg")

# sobel
sobel_weights = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]])

out = ndimage.convolve(img, sobel_weights)
sobel_autumn = Image.fromarray(out, "L")
sobel_autumn.save("SobelAutumn.jpg")
"""
# laplacian
#laplacian_autumn = Image.new("L", autumn.size)
laplacian = ImageFilter.Kernel((3,3),
(-1,-1, -1,
 -1, 8, -1,
 -1,-1, -1),0,0)
laplacian_autumn = autumn.filter(filter= laplacian)
laplacian_autumn = ImageOps.equalize(laplacian_autumn)
laplacian_autumn.save("LaplacianAutumn.jpg")
tester = laplacian_autumn.filter(ImageFilter.MedianFilter)
tester.save("laplacian_test.jpg")

# median
#median_autumn = Image.new("L", autumn.size)
median = ImageFilter.Kernel((3,3),
( 1, 1, 1,
  1, 1, 1,
  1, 1, 1),9,0)
median_autumn = autumn.filter(filter= median)
median_autumn.save("MedianAutumn.jpg")
"""