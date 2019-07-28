from fieldsfromimages.main.constants.removables import removable_files
import os


def main(local_paths):
    if local_paths.keep_intermediate_data:
        for i in removable_files:
            os.remove(i)

