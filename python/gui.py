
import tkinter as tk
from tkinter import filedialog
import url_converter
import image_downloader
import os
from time import sleep

def convert_click():
    if text_field.get() == "":
        text_field.insert(0, "Enter URL!")
    else:
        input_text = text_field.get()
        text_field.delete(0, tk.END)
        text_field.insert(0, url_converter.url_converter(input_text))
    text_field.select_range(0, tk.END)

def batch_download(urls, folder_name):
    source_code = image_downloader.get_source_code(urls)
    image_links = image_downloader.get_images(source_code, urls)
    length = len(image_links)
    print(str(length) + " images found!")
    links = []
    for i in range(length):
        links.append(url_converter.url_converter(image_links[i-1]))
    image_downloader.download_images(links, folder_name)
    current_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_name)
    if not os.path.exists(current_directory):
        label.config(text="No images downloaded!")
        return
    file_count = len([name for name in os.listdir(current_directory)])
    print(file_count)
    label.config(text=str(file_count) + " images downloaded!")

def select_all(event):
    hotel_name_field.select_range(0, tk.END)
    hotel_name_field.icursor(tk.END)

def loading():
    batch_download(batch_field.get(), hotel_name_field.get())
    window.after(100, finished)

def finished():
    print("Done!")
    batch_button.config(text="Download")
    batch_button.config(state="normal")
    batch_button.pack()

def download_click():
    label.config(text="")
    if hotel_name_field.get() == "" or hotel_name_field.get() == "Folder name":
        hotel_name_field.delete(0, tk.END)
        hotel_name_field.insert(0, "Enter folder name!")
        print("Enter folder name!")
        return
    if batch_field.get() == "":
        print("Enter URL!")
        return
    if batch_field.get().startswith("http"):
        print("URL is invalid!")
    else:
        print("URL is invalid!")
        label.config(text="URL is invalid!")
        return
    print("Loading...")
    batch_button.config(text="Loading...")
    batch_button.config(state="disabled")
    batch_button.pack()
    window.after(1, loading)


window = tk.Tk()
window.title("image_scraper")
window.geometry("600x300")
window.configure(bg="white")
window.resizable(False, False)


frame = tk.Frame(window, bg="white", padx=25, pady=25)
frame.pack(fill=tk.BOTH, expand=True)

text_field = tk.Entry(frame, width=50, justify="center")
text_field.pack()

button = tk.Button(frame, text="Convert", command=convert_click, width=10, justify="center")
button.pack()

empty_space2 = tk.Label(frame, text="", bg="white")
empty_space2.pack()

hotel_name_field = tk.Entry(frame, width=25, justify="center")
hotel_name_field.insert(0, "Folder name")
hotel_name_field.bind("<FocusIn>", select_all)
hotel_name_field.pack()

batch_field = tk.Entry(frame, width=50, justify="center")
batch_field.pack()


batch_button = tk.Button(frame, text="Download", command=download_click, width=10, justify="center")
batch_button.pack()

label = tk.Label(frame, text="", bg="white")
label.pack()


# def delete_duplicates():
#     label.config(text="")
#     os.chdir(os.path.dirname(os.path.abspath(__file__)))
#     all_files = []
#     for root, dirs, files in os.walk(".", topdown=False):
#         for name in files:
#             all_files.append(os.path.join(root, name))
#     print('Triggered delete_duplicates()!')
#     vorhanden = []
#     duplikate = 0
#     for file in all_files:
#         if file[file.rfind("/")+1:] in vorhanden:
#             os.remove(file)
#             duplikate += 1
#             print("Removed " + file[file.rfind("/")+1:] + "!")
#         else:
#             vorhanden.append(file[file.rfind("/")+1:])
#             print("Added " + file[file.rfind("/")+1:] + " to duplicates!")
#     print(str(duplikate) + " duplicates deleted!")
#     label.config(text=str(duplikate) + " duplicates deleted!")

# delete_duplicates_button = tk.Button(frame, text="Delete duplicates", command=delete_duplicates, width=10, justify="center")
# delete_duplicates_button.pack()

window.mainloop()