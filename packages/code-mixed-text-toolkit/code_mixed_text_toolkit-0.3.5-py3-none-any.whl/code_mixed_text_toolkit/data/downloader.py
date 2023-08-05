# Download dataset given name (list) or url
# Save into folder corpora in C file
# Show progress in command line
# Download finished

import pickle
import os
import json
import pandas as pd
import urllib.request
import requests
from urllib.request import urlopen
from tqdm import tqdm


AUTO_FORMATS = {
  "pickle": "pickle",
  "json": "json",
  "txt": "text",
  "text": "text",
  "csv": "csv"
}


FORMATS = {
  "pickle": "A serialized python object, stored using the pickle module.",
  "json": "A serialized python object, stored using the json module.",
  "text": "The raw (unicode string) contents of a file.",
  "csv": "A serialized python object, stored using the pandas module."
}

def download(name, 
    format="auto",
    encoding=None):

    '''suported resource formats:
        -"txt"
        -"csv"
        -"pickle"
        -"json"
        -"raw"
    '''

    resource_url = ""
    # path = os.getcwd()
    path = os.path.dirname(os.path.realpath(__file__))
    # f = open(os.path.join(path, "code_mixed_text_toolkit\data\data.json"))
    f = open(os.path.join(path, "data.json"))
    data = json.load(f)
    for i in data['datasets']:
        if i['name'] == name:
            resource_url = i['url']
            break
    
    if format == "auto":
        resource_url_parts = resource_url.split(".")
        ext = resource_url_parts[-1]
        if ext == "gz":
            ext = resource_url_parts[-2]
        format = AUTO_FORMATS.get(ext)
        if format is None:
            raise ValueError(
                "Could not determine format for %s based "
                'on its file\nextension; use the "format" '
                "argument to specify the format explicitly." % resource_url
            )
  
    if format not in FORMATS:
        raise ValueError(f"Unknown format type: {format}!")

    # TODO:: Path for MAC?
    newpath = r'C:\cmtt' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    else:
        if os.path.exists(os.path.join(newpath, name+"."+format)):
            print("Dataset " + name + " already exists at path: "  + newpath)
        else:
            print("Dataset " + name + " Download Starting...")
            # download_url(resource_url, newpath, name, format)
            download_url(resource_url, newpath, name, format)
            print("\nDataset " + name + " downloaded into path: " + newpath)
            print("\nDataset " + name + " Download Finished.")

# def download_url(url, output_path, name, format):
#     with DownloadProgressBar(unit='iB', unit_scale=True,
#                              miniters=1, desc=url.split('/')[-1]) as t:
#         urllib.request.urlretrieve(url, filename=os.path.join(output_path, name+"."+format), reporthook=t.update_to)

def download_url(url, output_path, name, format):
    fname = os.path.join(output_path, name+"."+format)
    # resp =  requests.get(url, stream=True)
    # total = int(resp.headers.get('content-length', 0))
    # with open(fname, 'wb') as file, tqdm(
    #     desc=fname,
    #     total=total,
    #     unit='iB',
    #     unit_scale=True,
    #     unit_divisor=1024,
    # ) as bar:
    #     for data in resp.iter_content(chunk_size=1024):
    #         size = file.write(data)
    #         bar.update(size)

    response = requests.get(url, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(fname, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")


# class DownloadProgressBar(tqdm):
#     def update_to(self, b=1, bsize=1, tsize=None):
#         if tsize is not None:       
#             self.total = tsize
#         self.update(b * bsize - self.n)