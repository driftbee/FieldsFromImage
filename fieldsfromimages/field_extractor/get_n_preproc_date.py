from fieldsfromimages.utilities.field_extractor_tools import *
import os

def main(local_paths):
    print('Getting all dates in the text file')
    input_path = os.path.join(local_paths.input_dir, local_paths.output_txt_file_name + '.txt')
    text = text_reader(input_path)
    parsed_dates = get_dates(text)
    for date in parsed_dates:
        print(date)
