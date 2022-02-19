import telegram, os, time, fetch_nasa, fetch_spacex
from dotenv import load_dotenv


def main():
    dotenv_path = 'dot.env'
    load_dotenv(dotenv_path)
    token = os.getenv('TOKEN')
    post_delay = int(os.getenv('POST_DELAY'))
    chat_id = os.getenv('CHANNEL_ID')
    bot = telegram.Bot(token=token)

    images = os.listdir('images')

    api_key = os.getenv('API_KEY')

    epic_photos = fetch_nasa.get_epic_imgs(api_key)
    fetch_nasa.fetch_epic_photos(epic_photos)
    img_urls = fetch_spacex.get_spacex_imgs(api_key, 25)
    fetch_spacex.fetch_spacex_last_launch(img_urls)


    while True:
        for image in images:
            bot.send_photo(chat_id=chat_id, photo=open(f'images/{image}', 'rb'))
            time.sleep(post_delay)


if __name__ == '__main__':
    main()
