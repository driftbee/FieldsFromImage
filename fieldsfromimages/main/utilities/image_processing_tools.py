import os
import cv2
import numpy as np


def image_reader(img_path):
    img = cv2.imread(img_path)


def create_output_file_dir(image_path, output_dir):
    output_dir_path = os.path.join(output_dir, image_path)
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)


"""
Rescales an Image
"""
def image_rescaler(cv_img, fx, fy):
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
    cv_img_gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    return cv_img_gray


"""
Dilate and erode and image
"""
def dilation_erosion(cv_img, iter=1):
    kernel = np.ones((1,1), np.uint8)
    cv_img_dilated = cv2.dilate(cv_img, kernel, iterations=iter)
    cv_img__dilated_eroded = cv2.erode(cv_img_dilated, kernel, iterations=iter)
    return cv_img__dilated_eroded


"""
Apply blur
"""
def apply_blur(cv_img, params=(5,5)):
    cv_img_blur = cv2.GaussianBlur(cv_img, params, 0)


"""
Turn image to black and white
"""
def black_white_convertor(cv_img):
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
    cv2.imwrite(save_path, cv_img)
