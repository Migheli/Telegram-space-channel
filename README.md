# Telegram-space-channel
Автоматический постинг фото космоса в телеграмм-канал.

##### Проект позволяет, используя Python автоматически публиковать фотографии космического пространства, полученные посредством API сервисов NASA и SPACE-X в телеграмм-канал с помощью чат-бота.

### Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Для начала работы Вам потребуется:
1. Токен для доступа к API NASA. 

Регистрируемся и получаем токен по адресу: https://api.nasa.gov/#signUp. Токен придет на Ваш адрес электронной почты, поэтому важно, чтобы Вы указали его корректно.
Полученный токен сохраните в переменную `NASA_API_KEY` файла `dot.env` проекта:
```
NASA_API_KEY='YOUR_SPACEX_TOKEN'
```
2. Телеграмм чат-бот.

Инструкция по регистрации бота и получению токена здесь: https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/ или здесь: https://habr.com/ru/post/262247/.
Кратко: просто напишите в телеграмм боту @BotFather и следуйте его инструкциям. 
Полученный токен сохраните в переменную `TELEGRAM_TOKEN` файла `dot.env` проекта:
```
TELEGRAM_TOKEN='YOUR_TELEGRAM_BOT_TOKEN'
```
3. Создаем свой телеграмм канал

Подробная инструкция по созданию канала здесь: https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/.
Имя канала сохраняем в переменную `TELEGRAM_CHANNEL_ID` файла `dot.env` проекта:
```
TELEGRAM_CHANNEL_ID='YOUR_CHANNEL_ID'
```
### Описание работы программы
Наша программа использует три скрипта: fetch_nasa.py, fetch_spacex.py, telebot.py:
 * fetch_nasa.py - загружает фотографии из API-сервиса NASA и сохраняет их в папке images проекта.
 * fetch_spacex.py - загружает фотографии из API-сервиса SPACEX и также сохраняет их в папке images проекта.
 * telebot.py - отвечает за работу бота - автоматический постинг загруженных фото в Ваш телеграмм-канал.

После выполнения шагов, указанных в предыдущем разделе добавляем Вашего бота в качестве администратора канала.
Как это можно сделать описано здесь: https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/ (раздел "Добавляем бота в канал (или в чат)").
Вот и все, нам осталось лишь выбрать интервал постинга (в секундах) и занести его в переменную `POST_DELAY` файла dot.env проекта:
```
POST_DELAY='DELAY_IN_SECONDS'
```
Например, для задержки постинга в сутки, код будет выглядеть так (в сутках 86400 секунд):
```
POST_DELAY='86400'
```
### Перед запуском проекта
Теперь Вы готовы к запуску проекта.
Все скрипты проекта работают автономно. 
В код внесены импорты для того, чтобы его можно было собрать в одном проекте Python, а именно в файле `telebot.py`:
  
```  
import fetch_nasa, fetch_spacex
from pathlib import Path

```  
  
```  
Path('images').mkdir(parents=True, exist_ok=True)
api_key = os.getenv('API_KEY')

epic_photos = fetch_nasa.get_epic_imgs(api_key)
fetch_nasa.fetch_epic_photos(epic_photos)
img_urls = fetch_spacex.get_spacex_imgs(api_key, 25)
fetch_spacex.fetch_spacex_last_launch(img_urls)
```
Данный блок кода дает возможность пользователю не запускать скрипты `fetch_nasa.py`, `fetch_spacex.py`.
 Импорты и блок кода, указанные выше в файле `telebot.py` без потери функциональности можно удалить при отсутствии необходимости интеграции и автоматической загрузки фото при запуске только файла `telebot.py` и/или раздельном использовании скриптов.

### Пример запуска скрипта

Запускаем скрипт из терминала стандартно, командой `telebot.py`: 


```  
your-computer:~/your-directory/this-project-name$ telebot.py
```  
В случае запуска отдельных скриптов, запускаем их аналогичным образом, командами `fetch_nasa.py`, `fetch_spacex.py` в терминале соответственно:

```  
your-computer:~/your-directory/this-project-name$ fetch_nasa.py
```  
```  
your-computer:~/your-directory/this-project-name$ fetch_spacex.py
```  

