"""
Greg Dews
CS390S Digital Image Processing

Homework 1
"""
from PIL import Image
import math

im = Image.open("NyanCat.PNG")
nyanpixels = im.load() # create the pixel map
img = Image.new( 'L', (im.size[1],im.size[0]), "white")
imgpixels = img.load()
length = img.size[1]
width = img.size[0]

for i in range(width):    # for every col:
    for j in range(length):    # For every row
        if (math.sqrt( ( (i-(width/2))**2) + ( (j-(length/2))**2)) <= 80):
            imgpixels[i,j] = nyanpixels[i,j][0]
        else:
            imgpixels[i,j] = (0)

img.save("NyanInFrame.BMP")
img.show()
