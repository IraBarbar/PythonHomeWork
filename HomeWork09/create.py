from aiogram import Bot, Dispatcher, executor, types
def open_token():
    data =str()
    with open('C:/Users/Ирина/Downloads/forBot/token.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
    return data


bot = Bot(open_token())
dp = Dispatcher(bot)