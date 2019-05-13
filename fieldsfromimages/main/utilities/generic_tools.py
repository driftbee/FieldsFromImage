import os


def create_output_file_dir(image_path, output_dir):
    print('Creating output directory')
    output_dir_path = os.path.join(output_dir)
    print(output_dir_path)
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

