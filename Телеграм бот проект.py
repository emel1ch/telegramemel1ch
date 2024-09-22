import telebot
import random
import requests
from bs4 import BeautifulSoup
from telebot import TeleBot

token = ''
bot: TeleBot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def get_message(message):
    bot.send_message(message.chat.id, text='Привет! Это бот для анекдотов. Чтобы получить все команды, пропиши команду /help')


@bot.message_handler(commands=['help'])
def get_help(message,):
    bot.send_message(message.chat.id, text=u"""/anecdote_small - Небольшие анекдоты
/anecdote_andrey - Анекдоты про Андрея
/anecdote_max - Анекдоты про Максима
/anecdote_shtirlic - Анекдоты про Штирлица
/anecdote_evrei - Анекдоты про евреев""")



@bot.message_handler(commands=['anecdote_small'])
def send_small(message):
    response = requests.get('https://anekdoty.ru/korotkie/').content
    html = BeautifulSoup(response, 'lxml')
    small = random.choice(html.find_all(class_='holder-body'))
    small_text = small.text
    bot.send_message(message.chat.id, small_text)


@bot.message_handler(commands=['anecdote_andrey'])
def send_andrey(message):
    response = requests.get('https://anekdoty.ru/search/?s=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9').content
    html = BeautifulSoup(response, 'lxml')
    andrey = random.choice(html.find_all(class_='holder-body'))
    andrey_text = andrey.text
    bot.send_message(message.chat.id, andrey_text)


@bot.message_handler(commands=['anecdote_max'])
def send_maxim(message):
    response = requests.get('https://anekdoty.ru/pro-maksima/').content
    html = BeautifulSoup(response, 'lxml')
    maxim = random.choice(html.find_all(class_='holder-body'))
    maxim_text = maxim.text
    bot.send_message(message.chat.id, maxim_text)


@bot.message_handler(commands=['anecdote_shtirlic'])
def send_vanya(message):
    response = requests.get('https://anekdoty.ru/pro-shtirlica/').content
    html = BeautifulSoup(response, 'lxml')
    vanya = random.choice(html.find_all(class_='holder-body'))
    vanya_text = vanya.text
    bot.send_message(message.chat.id, vanya_text)


@bot.message_handler(commands=['anecdote_evrei'])
def send_evrei(message):
    response = requests.get('https://anekdoty.ru/pro-evreev/').content
    html = BeautifulSoup(response, 'lxml')
    evrei = random.choice(html.find_all(class_='holder-body'))
    evrei_text = evrei.text
    bot.send_message(message.chat.id, evrei_text)




bot.polling(none_stop=True, interval=0)
