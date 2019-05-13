#!/usr/bin/python
from fieldsfromimages.main.utilities.generic_tools import *
from fieldsfromimages.main.utilities.image_processing_tools import *
from fieldsfromimages.main.constants.paths import LocalPaths


def main():
    local_paths = LocalPaths(input_dir='/home/dionysis/Documents/image_test',
                             input_file_name='itinerary.png',
                             output_dir='/home/dionysis/Documents/output_image_test',
                             output_file_name='itinerary')

    input_path = os.path.join(local_paths.input_dir, local_paths.input_file_name)
    img_to_preproc = image_reader(input_path)
    # rescale the image
    rescaled_img = image_rescaler(img_to_preproc)
    # turn image to gray
    gray_img = gray_convertor(rescaled_img)
    # dilate and erode and image
    dilated_eroded_img = dilation_erosion(gray_img)
    # apply blur
    blur_img = apply_blur(dilated_eroded_img)
    # turn to black and white
    bw_img = black_white_convertor(blur_img)
    # create dir for the output
    create_output_file_dir(local_paths.output_file_name, local_paths.output_dir)
    # save to the local path
    save_image(bw_img, local_paths.output_dir, local_paths.output_file_name)
