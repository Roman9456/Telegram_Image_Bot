import os
import random
import telebot 
from telebot import types

# Path to the image folder
IMAGE_FOLDER = 'Enter the path to the directory'

TOKEN_FILE = 'token.txt'

import os
import random
import telebot
import logging
from telebot import types

# Путь к папке с картинками
IMAGE_FOLDER = 'E:/Пикчи'

TOKEN_FILE = 'token.txt'

# Конфигурирование логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

# Получение токена
def get_token():
    with open(TOKEN_FILE, 'r') as file:
        token_line = file.readline()
        token = token_line.strip().split('=')[1]
        return token

# Функция старта
bot = telebot.TeleBot(get_token())

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет, путник: выбери папку', reply_markup=get_folder_keyboard())
    logging.info('Start command received')

# Получение сообщения от пользователя
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.startswith('Папка: '):
        folder_name = message.text.replace('Папка: ', '')
        send_random_image(message.chat.id, folder_name)
    else:
        bot.send_message(message.chat.id, 'Неверный выбор. Попробуйте еще раз.', reply_markup=get_folder_keyboard())
        logging.warning('Invalid choice')

# Отправка случайной картинки из выбранной папки
def send_random_image(chat_id, folder_name):
    folder_path = os.path.join(IMAGE_FOLDER, folder_name)
    image_files = os.listdir(folder_path)
    if image_files:
        random_image = random.choice(image_files)
        image_path = os.path.join(folder_path, random_image)
        with open(image_path, 'rb') as f:
            bot.send_photo(chat_id, f)
            logging.info(f'Sending random image from folder {folder_name}')
    else:
        bot.send_message(chat_id, f'В папке {folder_name} нет изображений.')
        logging.warning(f'No images found in folder {folder_name}')

# Получение клавиатуры с кнопками выбора папок
def get_folder_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    folders = os.listdir(IMAGE_FOLDER)
    for folder in folders:
        button = types.KeyboardButton(f'Папка: {folder}')
        keyboard.add(button)
    return keyboard

bot.polling(none_stop=True, interval=0)


def get_token():
    with open(TOKEN_FILE, 'r') as file:
        token_line = file.readline()
        token = token_line.strip().split('=')[1]
        return token

# Start function
bot = telebot.TeleBot(get_token())
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello traveler, choose a folder", reply_markup=get_folder_keyboard())

# Receive user messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.startswith('Folder: '):
        folder_name = message.text.replace('Folder: ', '')
        send_random_image(message.chat.id, folder_name)
    else:
        bot.send_message(message.chat.id, 'Invalid choice. Please try again.', reply_markup=get_folder_keyboard())

# Send a random image from the selected folder
def send_random_image(chat_id, folder_name):
    folder_path = os.path.join(IMAGE_FOLDER, folder_name)
    image_files = os.listdir(folder_path)
    if image_files:
        random_image = random.choice(image_files)
        image_path = os.path.join(folder_path, random_image)
        with open(image_path, 'rb') as f:
            bot.send_photo(chat_id, f)
    else:
        bot.send_message(chat_id, f'There are no images in the folder: {folder_name}.')

# Get the keyboard with folder selection buttons
def get_folder_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    folders = os.listdir(IMAGE_FOLDER)
    for folder in folders:
        button = types.KeyboardButton(f'Folder: {folder}')
        keyboard.add(button)
    return keyboard

bot.polling(none_stop=True, interval=0)

