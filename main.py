import random
from asyncio import wait_for
import threading
import requests
import telebot
from datetime import datetime
# from selenium import webdriver
from telebot import types

bot = telebot.TeleBot({Token})


def only_one(string):
    print('Please, enter the url of the gif:')
    r = requests.get(string, allow_redirects=True)
    i = "1"

    open(i + 'gifca.webp', 'wb').write(r.content)
    pass

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет")
    btn2 = types.KeyboardButton("Показать функционал")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот Сергея".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text', 'document'])
def get_text_messages(message):
    if(message.text == "Показать функционал"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Погода")
        btn2 = types.KeyboardButton("Время")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Показать функционал...Ну на", reply_markup=markup)
    elif message.text == "Привет":
        print(bot.get_chat(message.from_user.id).id)
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "Погода":
        tempWeather = random.Random()
        bot.send_message(message.from_user.id, str(tempWeather.uniform(5, 20)) + " Да, тут так тепло!")
    elif message.text == 'Время':
        bot.send_message(message.from_user.id, datetime.now())
    elif message.text == 'Помощь':
        bot.send_message(message.from_user.id, 'Мои команды: Время, Погода. Я продолжаю учиться')
    elif message.text == 'Изменить имя':
        bot.send_message(message.from_user.id, 'Имя у какого канала Вы хотите изменить?')
        tread1 = threading.Thread(target=change_title_name(message))
        tread1.start()
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Привет")
        btn2 = types.KeyboardButton("Показать функционал")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}! Я тестовый бот Сергея".format(
                             message.from_user), reply_markup=markup)

    else:
        bot.send_message(message.from_user.id, "Ничего не понял")
        # bot.send_message(message.from_user.id,
        #                  "https://media3.giphy.com/media/G8rcbSPfCgs3VDrWi5/200.webp?cid=ecf05e47lniwgv3m6i6nijui4jlm0uj1abak69bas54tmgj8&rid=200.webp&ct=g")
bot.polling(none_stop=True, interval=0)

def time_now():
    current_datetime = datetime.now()
    print(current_datetime)


def change_title_name(message):
    new_title = message.text
    # try:
    #     bot.set_chat_title(message.text, 'message.text')
    # except Exception:
    #     bot.send_message(message.from_user.id, 'Неверное назначение имени или что то еще')

