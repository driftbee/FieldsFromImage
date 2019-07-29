#!/usr/bin/python
from fieldsfromimages import pipeline
from fieldsfromimages import cleanup
from fieldsfromimages.constants.paths import LocalPaths

if __name__ == '__main__':
    local_paths = LocalPaths(input_dir='./output/input_images',
                             input_file_name='itinerary.png',
                             output_dir='./output/preproc_images',
                             output_file_name='itinerary_',
                             output_txt_file_dir='./output/text',
                             output_txt_file_name='itinerary_txt_',
                             keep_intermediate_data=False)

    try:
        pipeline.main(local_paths)
        cleanup.main(local_paths)
    except:
        cleanup.main(local_paths)
