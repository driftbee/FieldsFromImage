#!/usr/bin/python
import os
import cv2
import numpy as np


def image_reader(img_path):
    print('Reading image from disk')
    img = cv2.imread(img_path)
    return img


"""
Rescales an Image
"""
def image_rescaler(cv_img, fx=5, fy=5):
    print('Rescaling the image')
    cv_img_rescaled = cv2.resize(
        cv_img,
        None,
        fx=fx,
        fy=fy,
        interpolation=cv2.INTER_CUBIC)
    return cv_img_rescaled


"""
Gray convertor
"""
def gray_convertor(cv_img):
    print('Convert the image to gray')
    cv_img_gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    return cv_img_gray


"""
Dilate and erode and image
"""
def dilation_erosion(cv_img, iter=1):
    print('Dilate and erode the image')
    kernel = np.ones((1,1), np.uint8)
    cv_img_dilated = cv2.dilate(cv_img, kernel, iterations=iter)
    cv_img__dilated_eroded = cv2.erode(cv_img_dilated, kernel, iterations=iter)
    return cv_img__dilated_eroded


"""
Apply blur
"""
def apply_blur(cv_img, params=(5,5)):
    print('Applying blur')
    cv_img_blur = cv2.GaussianBlur(cv_img, params, 0)
    return cv_img_blur


"""
Turn image to black and white
"""
def black_white_convertor(cv_img):
    print('Turning image black and white')
    cv_img_bw = cv2.threshold(cv_img,
                              0,
                              255,
                              cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv_img_bw


"""
Saves image to directory
"""
def save_image(cv_img, dir, file_name):
    save_path = os.path.join(
        dir,
        file_name +
        '_preproced'
        '.jpg')
    print('Saving image to ' + save_path)
    cv2.imwrite(save_path, cv_img)
