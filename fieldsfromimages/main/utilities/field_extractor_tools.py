from fieldsfromimages.main.utilities.generic_tools import *
import datefinder

def text_reader(text_path):
    print('Reading text from disk')
    with open(text_path, 'r') as f:
        text = f.read()
    return text


def get_dates(text):
    matches = datefinder.find_dates(text)
    return matches

