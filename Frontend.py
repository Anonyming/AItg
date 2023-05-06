import telebot

import Backend

def Frontend():
    while True:
        dlg = Backend.Chat # main chat object

        bot = telebot.TeleBot('6238669874:AAH_VdzYuNTnIZFXeQKBQLiVSFnWFIJvlT8')
        @bot.message_handler(commands=['start'])
        def start(message):
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            hibtn = telebot.types.KeyboardButton("Hello!")
            wsbtn = telebot.types.KeyboardButton("What is GPT-like chatbots?")
            wycbtn = telebot.types.KeyboardButton("What you can?")
            markup.add(wsbtn)
            markup.add(hibtn)
            markup.add(wycbtn)
            bot.send_message(message.from_user.id, "Welcome to AItg GPT-like chatbot")

        @bot.message_handler(content_types=['text'])
        def Dialogue(message):
            if message.text != "Show me your source code, please.":
                bot.send_message(message.from_user.id, dlg.getAnswer(self=dlg, question=message.text))
            else:
                bot.send_message(message.from_user.id, "https://GitHub.com/Anonyming/AItg")

        bot.polling(none_stop=True, interval=0)
