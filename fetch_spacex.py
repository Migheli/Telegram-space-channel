import requests
import os
from pathlib import Path
from urllib.parse import urlsplit
from dotenv import load_dotenv
from img_downloader import download_img


def get_file_extension(url):
    parsed_url = urlsplit(url)
    filename = os.path.split(parsed_url.path)[1]
    file_extension = os.path.splitext(filename)[1]
    return file_extension


def get_spacex_urls(api_key, count_of_imgs):
    payload = {
        "api_key": api_key,
        "count": count_of_imgs,
        }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    img_urls = []
    response_datasets = response.json()
    for response_dataset in response_datasets:
        img_url = response_dataset['url']
        img_urls.append(img_url)
    return img_urls


def fetch_spacex_last_launch(img_urls):
    Path('images').mkdir(parents=True, exist_ok=True)
    for img_index, img_url in enumerate(img_urls, start=1):
        img_ext = get_file_extension(img_url)
        path_to_save = f'images/spacex{img_index}{img_ext}'
        try:
            download_img(img_url, path_to_save)
        except requests.exceptions.MissingSchema:
            pass


def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    img_urls = get_spacex_urls(api_key, 25)
    fetch_spacex_last_launch(img_urls)


if __name__ == '__main__':
    main()