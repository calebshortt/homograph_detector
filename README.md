# Homograph Detector
A basic python script that uses basic stats to identify homograph url attacks.

## Usage
Look at: base->analysis.py for example analysis

The 'resources' directory contains a url corpus to generate statistics on (resources/urls.txt) and known homograph urls (resources/known_external.txt)

**NOTE:** Some of the urls in 'known_external.txt' breaks the python script right now (when loading the file). Copy the text of the url and run the analysis on the example function shown in analysis.py.