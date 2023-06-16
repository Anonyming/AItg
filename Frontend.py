from aiogram import Bot, Dispatcher, executor, types
import Backend

async def Frontend():
    while True:
        chat = Backend.Dialog()
        bot = Dispatcher(Bot('6238669874:AAH_VdzYuNTnIZFXeQKBQLiVSFnWFIJvlT8'))

        async def sample_buttons():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            hibtn = types.KeyboardButton("Hello!")
            await markup.add(hibtn)
            wsbtn = types.KeyboardButton("What is GPT-like chatbots?")
            await markup.add(wsbtn)
            wycbtn = types.KeyboardButton("What you can?")
            await markup.add(wycbtn)
            scbtn = types.KeyboardButton("Show me your source code, please.")
            await markup.add(scbtn)
            hbtn = types.KeyboardButton("/help")
            await markup.add(hbtn)
            yield markup

        @bot.message_handler(commands=['start'])
        async def start(message):
            markup = sample_buttons()
            await message.answer(message.chat.id, "Welcome to AItg GPT-like chatbot", reply_markup=markup)

        @bot.message_handler(commands=['help'])
        async def help(message):
            markup = sample_buttons()
            await message.answer(message.chat.id, '''
            Welcome to AItg GPT-like bot \n
            This is a chat with Artificial Intelligence, than created in OpenAI \n
            For free using it uses gpt4free \n
            You messages haven't history and context \n
            I going to fix it \n
            You can't ask illegal questions \n
            You can use ChatGPT Jailbreak to solve it (https://github.com/GabryB03/ChatGPT-jailbraks) \n
            Talk to him for work, fun and anymore you can mind \n
            But know, AI can imagine wrong facts (artificial hallucinations) \n
            Useful use, \n
            AItg's creator \n
            \n
            Simple phrases to type: 
            ''', reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        async def Dialogue(message):
            if message.text != "Show me your source code, please.":
                await message.answer(message.chat.id, chat.getAnswer(prompt=message.text, iteration=1))
            else:
                await message.answer(message.chat.id, "https://GitHub.com/Anonyming/AItg")

        executor.start_polling(dispatcher=bot)
