#!/usr/bin/python
from fieldsfromimages.main import pipeline
from fieldsfromimages.main import cleanup
from fieldsfromimages.main.constants.paths import LocalPaths

if __name__ == '__main__':
    local_paths = LocalPaths(input_dir='/home/dionysis/Documents/image_test',
                             input_file_name='itinerary.png',
                             output_dir='/home/dionysis/Documents/output_image_test',
                             output_file_name='itinerary_',
                             output_txt_file_name='itinerary_txt_',
                             keep_intermediate_data=True)

    try:
        pipeline.main(local_paths)
        cleanup.main(local_paths)
    except:
        cleanup.main(local_paths)
