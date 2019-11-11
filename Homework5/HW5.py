"""
Greg Dews
CS390S
11/4/2019

Requirements:
    load image with simple subject
    create two images with "distortion"
    compare image quality by means of:
        MSE
        PSNR
        SSIM
        Own-Metric
    trial and error possible for self made metric.
"""
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
from skimage.measure import compare_psnr as psnr
from skimage.measure import compare_ssim as ssim

# from PIL import Image

def distortion_mask(im, x, right, y, down):
    length, width = im.shape()
    disimage = im.copy()
    mask = np.ones((length, width))
    for i in range(x,right):
        for j in range(y,down):
                mask[i][j] = 0
    return disimage + mask

def mse(im1, im2):
    a = np.mean( (im1 - im2) ** 2 )
    return a

def psnr(im1, im2):
    mse_im = mse(im1,im2)
    if mse_im == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / (mse_im)**0.5)

def wpsnr(im1, im2):
    mse_im = np.mean( (im1 - im2) ** 2 )
    if mse_im == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / (mse_im)**0.5)

im = cv2.imread("thepic.*")
distorted_A = distortion_mask(im, 100, 100, 100, 100)
distorted_B = distortion_mask(im, 250, 100, 250, 100)

# Show images
plt.figure()
plt.subplot(2, 2,1)
plt.imshow(im)
plt.title("Original Image")
plt.subplot(2, 2,2)
plt.imshow(distorted_A)
plt.title("Distorted Image A")
plt.subplot(2, 2,3)
plt.imshow(distorted_B)
plt.title("Distorted Image B")

mse_test = mse(im, im)
mse_A = mse(im, distorted_A)
mse_B = mse(im, distorted_B)
print("MSE of Original: " + mse_test)
print("MSE of A: " + mse_A)
print("MSE of B: " + mse_B)

psnr_test = psnr(im, im)
psnr_A = psnr(im, distorted_A)
psnr_B = psnr(im, distorted_B)
print("PSNR of Original: " + psnr_test)
print("PSNR of A: " + psnr_A)
print("PSNR of B: " + psnr_B)

weighted_psnr_A = wpsnr(im, distorted_A)
weighted_psnr_B = wpsnr(im, distorted_B)
print("Salienity Weighted PSNR of A: " + weighted_psnr_A)
print("Salienity Weighted PSNR of B: " + weighted_psnr_B)