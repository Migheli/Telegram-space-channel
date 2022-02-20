import requests
from pathlib import Path
from dotenv import load_dotenv
import os
from img_saver import save_img


def get_epic_imgs(api_key):
    payload = {"api_key": api_key,
               "images": "",
               }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=payload)
    response.raise_for_status()
    jsons = response.json()
    print(len(jsons))
    earth_urls = []
    for jsn in jsons:
        img_date, img_name = jsn['date'], jsn['image']
        img_date = img_date.split(' ')[0]
        year, month, day = img_date.split('-')
        earth_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{img_name}.png?api_key={api_key}'
        earth_urls.append(earth_url)
    return earth_urls


def fetch_epic_photos(earth_urls):
    Path('images').mkdir(parents=True, exist_ok=True)
    for img_index, earth_url in enumerate(earth_urls):
        img_id = img_index + 1
        path_to_save = f'images/earth{img_id}.png'
        try:
            save_img(earth_url, path_to_save)
        except requests.exceptions.MissingSchema:
            pass

def main():
    dotenv_path = 'dot.env'
    load_dotenv(dotenv_path)
    api_key = os.getenv('API_KEY')
    epic_photos = get_epic_imgs(api_key)
    fetch_epic_photos(epic_photos)


if __name__ == '__main__':
    main()
