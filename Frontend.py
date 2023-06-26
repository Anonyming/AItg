from aiogram import Bot, Dispatcher, executor, types
import Backend

class Chat():
    def __init__(self):
        self.__phonebook = dict()

    async def set(self, tg_chat_id, value):
        self.__phonebook = self.__phonebook + {tg_chat_id:value}

    async def get(self, tg_chat_id):
        return self.__phonebook.get(tg_chat_id, Backend.Dialog())
async def Frontend():
    while True:
        chat = dict()
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
            You can't ask illegal questions \n
            You can use ChatGPT Jailbreak to solve it (https://github.com/GabryB03/ChatGPT-jailbraks) \n
            Talk to him for work, fun and anymore you can mind \n
            But know, AI can imagine wrong facts (artificial hallucinations) \n
            Images, GIFs and all except text is not supported \n
            I going to support it in next versions \n
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

def ERROR(Exception):
    print("seting error mode")
    bot = Dispatcher(Bot('6238669874:AAH_VdzYuNTnIZFXeQKBQLiVSFnWFIJvlT8'))
    @bot.message_handler(content_types=['text'])
    async def WarnUsers(message, Exception=Exception):
        await message.answer(message.chat.id, f'''
        ERROR MESSAGE!!! \n
        BOT IS NOT WORKING \n
        ERROR: \n
        {Exception} \n
        ''' )

    print("seted error mode")
