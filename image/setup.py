from distutils.core import setup
setup(
  name = 'toascii',
  packages = ['toascii'], # this must be the same as the name above
  version = '3.6',
  description = 'Turns images into ascii art',
  author = 'Michael Kaminsky',
  author_email = 'mkaminsky11@gmail.com',
  url = 'https://github.com/mkaminsky11/ascii', # use the URL to the github repo
  keywords = ['ascii', 'image', 'asciiart', 'ascii art', 'art'], # arbitrary keywords
  classifiers = [],
  install_requires=['Pillow','urllib3']
)
