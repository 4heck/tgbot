#!/usr/bin/env python3

import misc
import telebot
from telebot import apihelper
from yobit import get_btc


token = misc.token
login = misc.login
password = misc.password
url = misc.url
port = misc.port
user_agent = misc.user_agent

URL = 'https://api.telegram.org/bot' + token + '/'

apihelper.proxy = {'https': f"socks5h://{login}:{password}@{url}:{port}"}

bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Сколько стоит BTC?')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message, answer="Wait a second, please..."):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Сколько стоит BTC?':
        bot.send_message(message.chat.id, get_btc())


print ("Bot started...")
bot.polling()
