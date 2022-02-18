import telegram, os, time, fetch_nasa, fetch_spacex
from dotenv import load_dotenv


def main():
    dotenv_path = 'dot.env'
    load_dotenv(dotenv_path)
    token = os.getenv('TOKEN')
    post_delay = int(os.getenv('POST_DELAY'))
    chat_id = "@SpaceDis"
    bot = telegram.Bot(token=token)

    images = os.listdir('images')

    while True:
        for image in images:
            bot.send_photo(chat_id=chat_id, photo=open(f'images/{image}', 'rb'))
            time.sleep(post_delay)


if __name__ == '__main__':
    main()
