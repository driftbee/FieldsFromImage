from fieldsfromimages.main.constants.paths import LocalPaths
from fieldsfromimages.main.utilities.field_extractor_tools import *


def main():
    local_paths = LocalPaths(input_dir='/home/dionysis/Documents/image_test/converted-text',
                             input_file_name='itinerary.txt',
                             output_dir='/home/dionysis/Documents/output_image_test',
                             output_file_name='fields')

    input_path = os.path.join(local_paths.input_dir, local_paths.input_file_name)
    text = text_reader(input_path)
    parsed_dates = get_dates(text)
    for date in parsed_dates:
        print(date)
