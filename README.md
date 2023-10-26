# image_scraper
A python script for downloading max resolution images from any website.

## What it does
The script is running through the page source for any image tags and image references. It removes any parameters that might scale down or convert the image to a lower resolution.

## Prerequisites
- Python 3
  - Modules
    -  requests
    -  selenium
    -  tkinter

```
pip install requests
pip install selenium
pip install tkinter
```

### macOS
```
brew install python-tk
```


## Usage

Run gui.py

```
python3 guiy.py
```
1. Convert any URL. Example: www.google.com/image.jpg?&w=3840&q=75 turns into www.google.com/image.jpg
2. Enter any URL. Name a folder. That folder will be created in the home directory. All images from the URL will be downloaded.

<img width="643" alt="Screenshot 2023-10-26 at 20 19 32" src="https://github.com/aomizu/image_scraper/assets/72222850/d789e765-0464-4b24-9348-131af6ede185">





