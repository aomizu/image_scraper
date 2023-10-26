import urllib.parse


# Shortens a URL to the base URL of an image (e.g. https://www.example.com/image.jpg?width=1000 -> https://www.example.com/image.jpg)
def url_converter(url):
    parsed_url = urllib.parse.unquote(url)
    if parsed_url.find(".jpg") != -1:
        parsed_url = parsed_url[:parsed_url.find(".jpg")+4]
    elif parsed_url.find(".png") != -1:
        parsed_url = parsed_url[:parsed_url.find(".png")+4]
    elif parsed_url.find(".gif") != -1:
        parsed_url = parsed_url[:parsed_url.find(".gif")+4]
    elif parsed_url.find(".jpeg") != -1:
        parsed_url = parsed_url[:parsed_url.find(".jpeg")+5]
    elif parsed_url.find(".webp") != -1:
        parsed_url = parsed_url[:parsed_url.find(".webp")+5]
    elif parsed_url.find(".tiff") != -1:
        parsed_url = parsed_url[:parsed_url.find(".tiff")+5]
    elif parsed_url.find(".ashx") != -1:
        parsed_url = parsed_url[:parsed_url.find(".ashx")+5]
    else:
        print("No image found!")
        return "No image found!"
    
    if parsed_url.find("url=") != -1:
        parsed_url = parsed_url[parsed_url.find("url=")+4:]

    return parsed_url