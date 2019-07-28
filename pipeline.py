#!/usr/bin/python
from fieldsfromimages import main
from fieldsfromimages import cleanup
from fieldsfromimages.constants.paths import LocalPaths

if __name__ == '__main__':
    local_paths = LocalPaths(input_dir='/home/dionysis/Documents/image_test',
                             input_file_name='itinerary.png',
                             output_dir='/home/dionysis/Documents/output_image_test',
                             output_file_name='itinerary_',
                             output_txt_file_name='itinerary_txt_',
                             keep_intermediate_data=True)

    try:
        main.main(local_paths)
        cleanup.main(local_paths)
    except:
        cleanup.main(local_paths)
