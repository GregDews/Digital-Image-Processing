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

# Load images, Create the pixel map
iris = Image.open("iris.bmp").convert('L')
#iris_pixels = im.load()
autumn = Image.open("PrincessAutumn.jpg").convert('L')
autumn.save("GreyAutumn.jpg")
sobel_autumn = Image.new("L", autumn.size)
laplacian_autumn = Image.new("L", autumn.size)
median_autumn = Image.new("L", autumn.size)

# Create kernels
sobelx = ImageFilter.Kernel((3,3),
(-1, 0, 1,
 -2, 0, 2,
 -1, 0, 1))
laplacian = ImageFilter.Kernel((3,3),
(-1,-1, -1,
 -1, 8, -1,
 -1,-1, -1))
median = ImageFilter.Kernel((3,3),
( 1, 1, 1,
  1, 1, 1,
  1, 1, 1))

# Apply filters
sobel_autumn = autumn.filter(filter= sobelx)
laplacian_autumn = autumn.filter(filter= laplacian)
median_autumn = autumn.filter(filter= median)

# Save Pictures
sobel_autumn.save("SobelAutumn.jpg")
laplacian_autumn.save("LaplacianAutumn.jpg")
median_autumn.save("MedianAutumn.jpg")