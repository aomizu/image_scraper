# image_scraper
A python script for downloading max resolution images from any website.

## What it does
The script is running through the page source for any image tags and image references. It removes any parameters that might scale down or convert the image to a lower resolution.

## Prerequisites
- Python 3
  - Modules
    -  requests
    -  selenium

```
pip install requests
pip install selenium
```


## Usage

Navigate to the folder
Run run.py

```
python3 run.py
```
Follow the prompt instructions.

1. Enter folder path
2. Enter URL

All images should appear in the folder.




