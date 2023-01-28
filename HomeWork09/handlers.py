from aiogram import types
from create import dp
import random
import view


name_bot = 'Reby'
total = 150


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(
        (f'Привет, {message.from_user.first_name} :)\n'
         f'Меня зовут {name_bot}. \n'
         f'Я бот. Если хочешь узнать , что я умею, вышли /menu .'))


@dp.message_handler(commands=['menu'])
async def mes_menu(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, давай поиграем в конфетки. '
                         f'Здесь правила игры /rule .\n')


@dp.message_handler(commands=['rule'])
async def mes_rule(message: types.Message):
    await message.answer(f'{view.rul()}, {message.from_user.first_name}! ')


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'Всего на столе конфет  - {count} шт.\n'
                         f'{message.from_user.first_name}, сколько ты возьмешь?')


@dp.message_handler()
async def mes_all(message: types.Message):
    global total

    if message.text.isdigit():
        user = int(message.text)
        if user in range(1, 29):
            total -= user  
            if total == 0:
                await message.answer(f'{message.from_user.first_name}, поздравляю!'
                f' \nТы победитель!!!')
            else:        
                take_bot = taken_bot()
                total = total-take_bot          
                if total <= 0:
                    await message.answer(f' Победа сегодня за мной!\n ')
                else:
                    await message.answer(f'{random.choice(view.answer_list())}\n'
                                        f'Тогда я возьму  {take_bot} шт. '
                                        f'\nНа столе осталось  конфет - {total} шт. ')
            
        elif user not in range(1,29):
            await message.answer(f'Не хитри, не больше 28 конфет возьми ;)')
        elif user <= total:
            await message.answer(f'Нельзя взять конфет больше, чем на столе {total}')

    else:
        await message.answer(f':)')


def taken_bot():
    global total
    bad_list = [0, -1]
    n = total//28
    if n % 2 == 0:
        one = 1
    else:
        one = -1
    taken = total - n*28 + one
    if (total - n*28 + one) in bad_list:
        taken = 28
    
    elif total/28 <= 1:
        taken = total
    return taken
