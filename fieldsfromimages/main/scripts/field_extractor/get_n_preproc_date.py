from fieldsfromimages.main.utilities.field_extractor_tools import *


def main(local_paths):
    input_path = os.path.join(local_paths.input_dir, local_paths.output_txt_file_name + '.txt')
    text = text_reader(input_path)
    parsed_dates = get_dates(text)
    for date in parsed_dates:
        print(date)
