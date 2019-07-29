from fieldsfromimages.utilities.field_extractor_tools import *
import os

def main(local_paths):
    print('Getting all the cities in the text file')
    input_path = os.path.join(local_paths.output_txt_file_dir, local_paths.output_txt_file_name + '.txt')
    text = text_reader(input_path)
    parsed_loc = get_cities(text)
    print(parsed_loc)
