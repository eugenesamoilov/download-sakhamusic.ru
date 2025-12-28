#!/bin/python3
import re
import requests
from pathlib import Path

site = "https://sakhamusic.ru"
site_timeout = 3
start = 1
limit = 10
download_dir = "sakhamusic/"

def create_dir():
     folder_path = Path(download_dir)
     folder_path.mkdir(parents=True, exist_ok=True)

def check_file(m_name: str):
    path = Path(m_name)
    if path.exists():
        return True
    else:
        return False

def download(m_id: int = 1):
    url = f'{site}/download/{m_id}'
    try:
        response = requests.get(url,stream=True,timeout=site_timeout)
    except requests.exceptions.RequestException:
        print("common exception")
        return
    if response.headers.get("Content-Length", "") == "4096":
        if response.headers.get("Content-Disposition", "") == 'attachment; filename=" - .mp3"':
            print("pusto")
            return
    cd = response.headers.get("Content-Disposition", "")
    match = re.search(r'filename="(.+)"', cd)
    if match:
        raw_name = match.group(1)
        filename = raw_name.encode('latin-1').decode('utf-8')
    filename=download_dir+filename
    if check_file(filename):
        return
    else:            
        with open(filename, 'wb') as f:
            try:
                f.write(response.content)
                print(f"{m_id} {filename} saved")
            except (IOError, OSError):
                print("Error writing to file")

def main():
    create_dir()
    for i in range(start,limit+1):
        download(i)
    print("completed")

if __name__ == "__main__":
        main()
