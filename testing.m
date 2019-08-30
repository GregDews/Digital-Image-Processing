clc
clear all
close all


path='./standard_test_images/'; % this is your working path
impath=[path,'NyanCat.PNG']; % path of the image
im=imread(impath);
figure,imshow(im); % you could also try image() imagesc() other image display functions 

im_resized=imresize(im,[128,128]);
figure,imshow(im_resized);

[r,c,ch]=size(im);
img=zeros(r,c);
img=rgb2gray(im); % change color image to grayscale image 

figure,imshow(img);

%out_impath=[path,'output/','lena_gray_256.tif'];% path of the output im
%imwrite(img,out_impath);
%i=i;