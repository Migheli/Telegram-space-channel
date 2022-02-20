import requests
import os
from pathlib import Path
from urllib.parse import urlsplit
from dotenv import load_dotenv
from img_saver import save_img


def get_img_url(url):
    response = requests.get(url)
    response.raise_for_status()
    jsn = response.json()
    url_imgs = jsn['links']['flickr_images']
    return url_imgs


def get_file_extension(url):
    parsed_url = urlsplit(url)
    filename = os.path.split(parsed_url.path)[1]
    file_extension = os.path.splitext(filename)[1]
    return file_extension


def get_spacex_imgs(api_key, count_of_imgs):
    payload = {"api_key": api_key,
               "count": count_of_imgs,
               }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    img_urls = []
    jsons = response.json()
    for jsn in jsons:
        img_url = jsn['url']
        img_urls.append(img_url)
    return img_urls


def fetch_spacex_last_launch(img_urls):
    Path('images').mkdir(parents=True, exist_ok=True)
    for img_index, img_url in enumerate(img_urls):
        img_id = img_index + 1
        img_ext = get_file_extension(img_url)
        path_to_save = f'images/spacex{img_id}{img_ext}'
        try:
            save_img(img_url, path_to_save)
        except requests.exceptions.MissingSchema:
            pass

def main():
    dotenv_path = 'dot.env'
    load_dotenv(dotenv_path)
    api_key = os.getenv('API_KEY')

    img_urls = get_spacex_imgs(api_key, 25)
    fetch_spacex_last_launch(img_urls)


if __name__ == '__main__':
    main()