#!/usr/bin/python
from fieldsfromimages.main.scripts.image_preprocessing import image_preproc
from fieldsfromimages.main.scripts.field_extractor import get_n_preproc_date
from fieldsfromimages.main.scripts.field_extractor import get_n_preproc_location
from fieldsfromimages.main.scripts.field_extractor import image_to_string
from fieldsfromimages.main.constants.paths import LocalPaths



def main(local_paths):
    image_preproc.main(local_paths)
    image_to_string.main(local_paths)
    get_n_preproc_date.main(local_paths)
    get_n_preproc_location.main(local_paths)