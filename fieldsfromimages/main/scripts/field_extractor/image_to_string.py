import pytesseract
import os
from PIL import Image
from fieldsfromimages.main.constants.removables import removable_files


def main(local_paths):
    path_to_read = os.path.join(local_paths.output_dir, local_paths.output_file_name + '_preproced.jpg')
    text = pytesseract.image_to_string(Image.open(path_to_read))
    path_to_write = os.path.join(local_paths.input_dir, local_paths.output_txt_file_name + '.txt')
    with open(path_to_write, 'w') as f:
        f.write(text)
    removable_files.append(path_to_write)