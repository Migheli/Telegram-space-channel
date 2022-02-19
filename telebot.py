import telegram, os, time
import fetch_nasa, fetch_spacex
from pathlib import Path
from dotenv import load_dotenv


def main():
    dotenv_path = 'dot.env'
    load_dotenv(dotenv_path)
    token = os.getenv('TOKEN')
    post_delay = int(os.getenv('POST_DELAY'))
    chat_id = os.getenv('CHANNEL_ID')
    bot = telegram.Bot(token=token)

    Path('images').mkdir(parents=True, exist_ok=True)
    api_key = os.getenv('API_KEY')

    epic_photos = fetch_nasa.get_epic_imgs(api_key)
    fetch_nasa.fetch_epic_photos(epic_photos)
    img_urls = fetch_spacex.get_spacex_imgs(api_key, 25)
    fetch_spacex.fetch_spacex_last_launch(img_urls)

    images = os.listdir('images')

    while True:
        for image in images:
            bot.send_photo(chat_id=chat_id, photo=open(f'images/{image}', 'rb'))
            time.sleep(post_delay)


if __name__ == '__main__':
    main()
