import os
import image_downloader
import url_converter

print("Image Scraper v0.1")
print("This script will download all images from a website in the highest quality.")

# asking for destination path
destination_path = input("Please enter the destination path (default: current directory in 'output'): ")
# wait for user input
if destination_path == "":
    destination_path = os.path.join(os.getcwd(), "output")
    #make folder if it does not exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    print("Using default path: " + destination_path)
else:
    #check if path is valid
    if not os.path.exists(destination_path):
        print("Invalid path!")
        exit(1)
    else:
        print("Using path: " + destination_path)

# ask for url
url = input("Please enter the full url of the website: ")
# wait for user input
if url == "":
    print("No url entered!")
    exit(1)
else:
    #check if valid url
    if not url.startswith("http"):
        print("Invalid url!")
        exit(1)
    else:
        print("Using url: " + url)


def batch_download(urls, destination_path):
    source_code = image_downloader.get_source_code(urls)
    image_links = image_downloader.get_images(source_code, urls)
    length = len(image_links)
    print(str(length) + " images found!")
    links = []
    for i in range(length):
        links.append(url_converter.url_converter(image_links[i-1]))
    image_downloader.download_images(links, destination_path)

    file_count = len([name for name in os.listdir(destination_path)])
    print(str(file_count) + " images downloaded!")


#downloads all images
batch_download(url, destination_path)