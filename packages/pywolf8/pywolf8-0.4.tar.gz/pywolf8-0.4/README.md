# pywolf8
Extends the python module wolf_ism8 by marcschmiedchen (https://pypi.org/project/wolf-ism8/)

# Original Description
A class implementation of a http server which listens for messages from Wolf's Heating ISM8 module. Received messages are printed and data is held in an array for further usage. This module was built in order to integrate a Wolf heating system into Home Assistant.

# Build
py -m build

# Upload
py -m twine upload dist/*