"""
Greg Dews
CS390S
Project 1

testing---
        input - Me = Bi
        P'Bi = wt_B (single vector with eigenvector quantities)
        compare wt_B to each column of wt_A , if matching, it is that person
    
    adding efficiency to training
        shortcutting 2500 x 2500 array problem
        find eigenvector of A'A = P2 (40x40)
            rather than A*A' (2500x2500)
            A'*A * P2 = lamdaP2
            A A' A P2 = lamda A P2
            AA' Q = lamda Q 
            AA' P = lamda P
            ... therefore A P2 = P, or A (A'A)
    CMC curve - hint code in slides/codes posted
        rank 1 to 10

    Python coding notes
    numpy.transpose(matrix) to transpose
    reshape is numpy method
    Check faceRecoganition4faces.pdf for example of report?
    will discuss more by next time. Recommend download sample code and try
    """

import numpy as np
import cv2
import glob
from matplotlib import pyplot as plt
from os import listdir
from PIL import Image
from scipy import linalg


# Training - original author Feng Jiang
"""
call train with directory of images as param
Will default to images/enrolling/*.bmp
"""


def train():
    # Read in all Training images
    # Build multi-D collections for Training Data

    
    # load all images in a directory
    loaded_images = list()
    X_filenames = list()
    person_dict = dict()
    num = 0
    for filename in listdir('Project1/images/enrolling'):
        # load image
        if ".bmp" in filename:
            img_data = cv2.imread('Project1/images/enrolling/' + filename, 0)
            person = filename[0:-8]
            if person not in person_dict:
                person_dict[person] = []
            person_dict[person].append(num)
            num += 1
            # store loaded image
            loaded_images.append(img_data)
            #print('> loaded %s %s' % (filename, img_data.shape))
    
    #print(person_dict)
    all_images = [image[np.newaxis, ...] for image in loaded_images]

    try:
        X_arr = np.concatenate(all_images)
    except ValueError:
        raise ValueError('Image dimensions must agree.')

    image_width = X_arr.shape[2]
    image_height = X_arr.shape[1]
    dims = (image_height, image_width)

    vect_length = image_height*image_width
    M = X_arr.shape[0]  # number of training images
    Mp = 43  # number of  person

    X_flat = convert_to_vects(X_arr)  # Convert images to vectors

    m = len(person_dict.keys())

    print('     Constructing dictionary of {} persons on {} training images...'.format(m, M))

    # 2. build avg vector for each person !!!!
    #  create parallel list to hold img names
    print('     Creating average vector of images from each face...')
    avg_vects = np.empty((Mp, vect_length), dtype=X_arr[0].dtype)
    avg_vects_names = []
    row = 0
    for key, value in person_dict.items():
        avg_vects_names.append(key)

        temp_vects = np.empty((len(value), vect_length), dtype=X_arr[0].dtype)
        for i in range(temp_vects.shape[0]):
            # print('{} : {}'.format(key,self.X_flat[value[i]]))
            temp_vects[i] = X_flat[value[i]]
        # avg vectors for given image
        avg_vects[row] = temp_vects.mean(axis=0)
        row += 1
    print('     Done...')

    # 3. Calc mean vector of all persons in training set
    print('     Calculating mean of all vectors...')
    mean_vect = avg_vects.mean(axis=0)
    print('     Done...')

    print('     Subtracting mean from all average images...')
    X_flat_centered = np.empty(avg_vects.shape, dtype=X_arr[0].dtype)
    for i in range(Mp):
        X_flat_centered[i] = center_vect(avg_vects[i], mean_vect)
    X_flat_centered = X_flat_centered
    print('     Done...')

    print('     Computing eigenvalues and eigenvectors...')
    cov_mat = np.cov(X_flat_centered)
    # .eigh returns only real eigenvals
    eigenvals, eigenvects = linalg.eigh(cov_mat.astype('float32'))

    # reverse to put most contrib at beginning
    ordered_eigenvals = eigenvals[::-1]
    ordered_eigenvects = np.fliplr(eigenvects)
    wt_A = np.dot(
        ordered_eigenvects.T[:m].T, X_flat_centered)
    #np.save('wt_A.npy', wt_A)
    np.save('mean_vect.npy', mean_vect)

    # Eigen Faces
    row = wt_A.shape[0]
    plt.figure()
    for i in range(row):
        plt.subplot(6, 8, i + 1)
        plt.imshow(wt_A[i].reshape((image_height, image_width)), cmap=plt.cm.gray)
        plt.title(avg_vects_names[i])
        plt.xticks(())
        plt.yticks(())
        imgplot = plt.imshow(wt_A[i].reshape(
            image_width, image_height), 'gray')
    plt.show()


def convert_to_vect(mat_):

    mat = mat_.copy()
    vect = np.ravel(mat)
    return vect


def convert_to_vects(arr_):
    '''
    flattens all images in a numpy array into vectors
    Input:
            arr_: numpy array 
    '''
    print('     Converting 2D images to vectors...')

    arr = arr_.copy()
    vect_length = arr.shape[1]*arr.shape[2]
    M = arr.shape[0]         # number of training images

    if M == 1:  # vectorize single image
        return np.ravel(arr)
    else:
        arr_flat = np.empty((M, vect_length), dtype=arr[0].dtype)
        for i in range(M):
            arr_flat[i] = convert_to_vect(arr[i])
        return arr_flat


def center_vect(vect, mean_vect):
    centered = vect - mean_vect
    centered = centered.clip(min=0)

    return centered


def test():

    load_weight = np.load('wt_A.npy')
    load_mean_vect = np.load('mean_vect.npy')

if __name__ == "__main__":
    response = input("train(1) or test(2)")
    if "Train" in response or response is "1":
        print("Training")
        train()
    elif "Test" in response or response is "2":
        print("Testing")
        test()
    elif response:
        print("did not match a command")
