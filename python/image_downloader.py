import requests
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from urllib.parse import urljoin
import os
from time import sleep
from concurrent.futures import ThreadPoolExecutor

timeout = 5
webdriver_instance = None

def check_file_extension(url):
    if url.find(".jpg") != -1:
        return ".jpg"
    elif url.find(".png") != -1:
        return ".png"
    elif url.find(".gif") != -1:
        return ".gif"
    elif url.find(".jpeg") != -1:
        return ".jpeg"
    elif url.find(".webp") != -1:
        return ".webp"
    elif url.find(".tiff") != -1:
        return ".tiff"
    elif url.find(".ashx") != -1:
        return  ".jpg"
    else:
        return "No image found!"

def check_name(url):
    if url.find(".jpg") != -1:
        return url[url.rfind("/")+1:url.find(".jpg")]
    elif url.find(".png") != -1:
        return url[url.rfind("/")+1:url.find(".png")]
    elif url.find(".gif") != -1:
        return url[url.rfind("/")+1:url.find(".gif")]
    elif url.find(".jpeg") != -1:
        return url[url.rfind("/")+1:url.find(".jpeg")]
    elif url.find(".webp") != -1:
        return url[url.rfind("/")+1:url.find(".webp")]
    elif url.find(".tiff") != -1:
        return url[url.rfind("/")+1:url.find(".tiff")]
    elif url.find(".ashx") != -1:
        return url[url.rfind("/")+1:url.find(".ashx")]
    else:
        return "No image found!"
    
def initialize_webdriver():
    global webdriver_instance
    if webdriver_instance is None:
        options = Options()
        options.headless = True
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
        options.add_argument('user-agent={0}'.format(user_agent))
        options.add_argument("--header='accept-language: en-US,en;q=0.9'")
        options.add_argument("--headless")
        webdriver_instance = webdriver.Chrome(options=options)


def get_source_code(url):
    initialize_webdriver()
    webdriver_instance.get(url)
    # print(webdriver_instance.page_source)
    return webdriver_instance.page_source


def get_images(source_code, url):
    images = []

    base_url = url[:url.find("/", 8)]

    img_pattern = re.compile(r'<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    anchor_pattern = re.compile(r'<a[^>]+href=["\'](.*?)["\'][^>]*>', re.IGNORECASE)
    srcset_pattern = re.compile(r'<source[^>]+srcset=["\'](.*?)["\']', re.IGNORECASE)

    img_matches = img_pattern.findall(source_code)
    anchor_matches = anchor_pattern.findall(source_code)
    srcset_matches = srcset_pattern.findall(source_code)

    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.tiff', '.ashx')

    for img_match in img_matches:
        if any(ext in img_match for ext in image_extensions):
            absolute_img_url = urljoin(base_url, img_match)
            images.append(absolute_img_url)
            
    for anchor_match in anchor_matches:
        if any(ext in anchor_match for ext in image_extensions):
            absolute_img_url = urljoin(base_url, anchor_match)
            images.append(absolute_img_url)
    
    for srcset_match in srcset_matches:
        if any(ext in srcset_match for ext in image_extensions):
            absolute_img_url = urljoin(base_url, srcset_match)
            images.append(absolute_img_url)

    return images


def download(url, destination_path):
    extension = check_file_extension(url)
    name = check_name(url)
    os.chdir(destination_path)
    if(extension == "No image found!" or name == "No image found!"):
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=timeout, stream=True)
        print('Saving ' + name + extension + '...')
    except:
        print('Image ' + name + extension + " couldn't be downloaded.")

    if response.status_code == 200:
        with open(destination_path + "/" + name + extension, 'wb') as file:
            file.write(response.content)
        print(name + extension)
        print('Image saved successfully.')
    else:
        print("Image couldn't be downloaded. Status Code: " + str(response.status_code) + '.')

def download_images(urls, destination_path):
    with ThreadPoolExecutor() as executor:
        for url in urls:
            executor.submit(download, url, destination_path)