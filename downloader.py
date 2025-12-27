#!/bin/python3
import re
import requests
from pathlib import Path

site = "https://sakhamusic.ru"
start = 1
limit = 6000
site_timeout = 3
dir = "sakhamusic/"

def create_dir():
     folder_path = Path(dir)
     folder_path.mkdir(parents=True, exist_ok=True)

def download():
    for i in range(start,limit+1):
        url = f'{site}/download/{i}'
        try:
            response = requests.get(url,stream=True,timeout=site_timeout)
        except requests.exceptions.RequestException:
            continue
        cd = response.headers.get("Content-Disposition", "")
        match = re.search(r'filename="(.+)"', cd)
        if match:
            raw_name = match.group(1)
            filename = raw_name.encode('latin-1').decode('utf-8')
            print(i,filename)
        filename=dir+filename
        print(filename)
        with open(filename, 'wb') as f:
            try:
                f.write(response.content)
            except (IOError, OSError):
                print("Error writing to file")

def main():
    create_dir()
    download()
    print("comlplete")

if __name__ == "__main__":
        main()
