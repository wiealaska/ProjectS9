# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:47:12 2019

@author: lucca
PROJET 29 - PART DU TRAITEMENT D'IMAGERIE
"""


import cv2.cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def noise_removal(img):              #Removing noise with mean and median filter
    imf = cv.medianBlur(img, 3)
    imf = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
    return imf


def clahe_img(img):
    clahe = cv.createCLAHE(clipLimit=4, tileGridSize=(8, 8))  # CLAHE APPLICATION
    imc = clahe.apply(img)           
    return imc


def segmentation_img(img):                               #SEGMENTATION OF IMAGE
    ret, seg_im = cv.threshold(img, 160, 255, cv.THRESH_BINARY)  
    return seg_im

# TO DO: Better arrangement of pics
def apply_filter(path):
    img = cv.imread(path, 0)
    img1 = noise_removal(img)
    img2 = clahe_img(img1)  # Calling the processing functions
    img3 = segmentation_img(img2)

    fig = plt.figure()
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222)

    ax2.imshow(img2)
    ax3.imshow(img3)
    plt.savefig('mama1.jpg') # to make it accessible for pixmap it has to be jpg (or similar)






