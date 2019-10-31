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

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('18-21', '22-25', '26-30', '30+')


@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard2)
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    bot.send_message(message.chat.id, 'Давай знакомиться, как тебя зовут?')


@bot.message_handler(content_types=['text'])
def send_name(message):
    name = message.text
    bot.send_message(message.chat.id, 'Привет, {}!'.format(name))
    bot.send_message(message.chat.id, 'Меня зовут RuMTelegramBot! Сколько тебе лет?', reply_markup=keyboard2)
    return name


def send_age(message, name='None'):
    if message.text == '18-21' or message.text == '22-25' or message.text == '26-30' or message.text == '30+':
        age = message.text
        bot.send_message(message.chat.id, 'Тебя зовут {} и тебе {} лет, все верно?'.format(name, age))


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Сколько стоит BTC?':
        bot.send_message(message.chat.id, get_btc())


if __name__ == '__main__':
    print("Bot started...")
    bot.polling(none_stop=True)
