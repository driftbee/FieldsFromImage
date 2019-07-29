from setuptools import setup

with open('requirements.txt', 'r') as fp:
    requirements = [x.strip() for x in fp.readlines()]

setup(name='fields-from-images',
      version='0.1.0',
      description='Extracts relevant text from images',
      author='Dionysis Varelas',
      install_requires=requirements)
