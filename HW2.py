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
import PIL
from PIL import Image

# Load images, Create the pixel map
iris = Image.open("iris.bmp").convert('LA')
#iris_pixels = im.load()
autumn = Image.open("PrincessAutumn.jpg").convert('LA')
sobel_autumn = Image.new('L', autumn.size)
laplacian_autumn = Image.new('L', autumn.size)
median_autumn = Image.new('L', autumn.size)

# Create kernels
sobelx = PIL.ImageFilter.Kernel((3,3),
(-1,0,1,-2,0,2,-1,0,1)
,1,0)
sobely = PIL.ImageFilter.Kernel((3,3),
(1,0,-1,2,0,-2,1,0,-1)
,1,0)
laplacian = PIL.ImageFilter.Kernel((3,3),
(0,-1,0,-1,4,-1,0,-1,0)
,1,0)
median = PIL.ImageFilter.Kernel((3,3),
(1,1,1,1,1,1,1,1,1)
,1,0)

# Apply filters
horizontal = autumn.filter(sobelx)
#vertical = autumn.filter(sobely)
#sobel_autumn = horizontal + vertical
laplacian_autumn = autumn.filter(laplacian)
median_autumn = autumn.filter(median)

# Save Pictures
sobel_autumn.save("SobelAutumn.png")
laplacian_autumn.save("LaplacianAutumn.png")
median_autumn.save("MedianAutumn.png")

# Show pictures
sobel_autumn.show
laplacian_autumn.show
median_autumn.show