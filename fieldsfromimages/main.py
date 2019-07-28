#!/usr/bin/python
from fieldsfromimages.image_preprocessing import image_preproc
from fieldsfromimages.field_extractor import get_n_preproc_date
from fieldsfromimages.field_extractor import get_n_preproc_location
from fieldsfromimages.field_extractor import image_to_string


def main(local_paths):
    image_preproc.main(local_paths)
    image_to_string.main(local_paths)
    get_n_preproc_date.main(local_paths)
    get_n_preproc_location.main(local_paths)