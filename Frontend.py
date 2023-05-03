import telebot
from telebot import types


def Frontend():
    bot = telebot.TeleBot('')

    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        wsbtn = types.KeyboardButton("What is GPT-like chatbots?")
        hibtn = types.KeyboardButton("Hello!")
        wycbtn = types.KeyboardButton("What you can?")
        markup.add(wsbtn)
        markup.add(hibtn)
        markup.add(wycbtn)
        bot.send_message(message.from_user.id, "Welcome to AItg GPT-like chatbot")

    @bot.message_handler(content_types='text')
    def Dialogue(message):
        pass
