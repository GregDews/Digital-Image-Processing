"""
Greg Dews
CS390S
Homework 4
1. Generate 256x256 gray image with only 2 intensities
    0.4 and 0.7 of intensity
    80 pixel radius circle
2. Generate three types of noise and add to image
        Gaussian mean=0 variance=0.1
        Uniform
        Salt and pepper ratio=0.5 amount=0.02
3. Histogram these images
4. Filter to recover images
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image

# Make some noise!
circle = np.ones((256,256), np.uint8) * 178 # 0.7*255 = 178
width, height = circle.shape
for i in range(width):
    for j in range(height):
        dist = np.sqrt((i-width/2)**2+(j-height/2)**2)
        if dist < 80:
            circle[i][j] = 102 # 0.4*255 = 102
Image.fromarray(circle).save("Circle.TIFF")

# noise settings
gauss_mean = 0
gauss_var = 0.01
ratio = 0.5
amount = 0.02

# Gaussian distribution noise
sigma = gauss_var**0.5
gauss = np.random.normal(gauss_mean, sigma, (width, height))
gauss = gauss.reshape(width, height)
gaussNoise = circle + (gauss * 255)
img_gauss = Image.fromarray(gaussNoise)
img_gauss.save("GaussCircle.TIFF")

# Uniform Noise
uni_noise = np.random.uniform(-0.05, 0.05, (width, height))
uniform = (uni_noise * 255) + circle
img_uniform = Image.fromarray(uniform)
img_uniform.save("UniformCircle.TIFF")

# Salt
s_n_p = np.copy(circle)
salt = np.ceil(amount * circle.size * ratio)
coords = [np.random.randint(0, i - 1, int(salt))
         for i in circle.shape]
s_n_p[coords] = 255

# Pepper
pepper = np.ceil(amount* circle.size * (1. - ratio))
coords = [np.random.randint(0, i - 1, int(pepper))
         for i in circle.shape]
s_n_p[coords] = 0

img_snp = Image.fromarray(s_n_p)
img_snp.save("SnPCircle.TIFF")

# Show the noise!
fig1 = plt.figure()
a = fig1.add_subplot(1, 4, 1)
imgplot = plt.imshow(circle, 'gray')
a.set_title('Original')

a = fig1.add_subplot(1, 4, 2)
imgplot = plt.imshow(gaussNoise, 'gray')
a.set_title('Gaussian Noise')

a = fig1.add_subplot(1, 4, 3)
imgplot = plt.imshow(uniform, 'gray')
a.set_title('Uniform Noise')

a = fig1.add_subplot(1, 4, 4)
imgplot = plt.imshow(s_n_p, 'gray')
a.set_title("Salt n Pepper")
plt.show()

fig2 = plt.figure()
a = fig2.add_subplot(1, 4, 1)
imgplot = plt.hist(circle.ravel())
a.set_title('Original')
a = fig2.add_subplot(1, 4, 2)
imgplot = plt.hist(gaussNoise.ravel(), bins=256)
a.set_title('Gaussian Noise')
a = fig2.add_subplot(1, 4, 3)
imgplot = plt.hist(uniform.ravel(), bins=256)
a.set_title('Uniform Noise')
a = fig2.add_subplot(1, 4, 4)
imgplot = plt.hist(s_n_p.ravel(), bins=256)
a.set_title("Salt n Pepper")
plt.show()

"""
need to add filters and fixes
"""