from geotext import GeoText
import datefinder


def text_reader(text_path):
    print('Reading text from disk')
    with open(text_path, 'r') as f:
        text = f.read()
    return text


def get_dates(text):
    matches = datefinder.find_dates(text)
    return matches


def get_cities(text):
    places = GeoText(text)
    return places.cities

