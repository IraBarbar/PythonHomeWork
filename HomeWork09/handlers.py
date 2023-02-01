from aiogram import types
from keyboards import kb_main_menu, kb_main_set
from create import dp
import random
import view
from datetime import datetime

total = view.num_start


def write_data(message: types.Message):
    user_come = []
    user_come.append(str(datetime.now())[:-7])
    user_come.append(message.from_user.full_name)
    user_come.append(message.from_user.id)
    user_come.append(message.from_user.username)
    user_come.append(message.location)
    user_come = list(map(str, user_come))
    with open('C:/Users/Ирина/Downloads/forBot/userCome.txt', 'a', encoding='UTF-8') as data:
        data.write('🔺'.join(user_come) + '\n')


def list_winner_write(message: types.Message):
    win = []
    win.append(message.from_user.full_name)
    with open('C:/Users/Ирина/Downloads/forBot/winner.txt', 'a', encoding='UTF-8') as data:
        data.write('|'.join(win)+'|')


def list_winner():
    winner = []
    with open('C:/Users/Ирина/Downloads/forBot/winner.txt', 'r', encoding='UTF-8') as data:
        file = str()
        file = data.readline()[:-1]
        winner = file.split('|')
    return winner


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'🎊🎊 Привет, {message.from_user.first_name} !\n'
                         f'Меня зовут {view.name_bot}.',
                         reply_markup=kb_main_menu)


@dp.message_handler(commands=['game'])
async def mes_game(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, давай поиграем в конфетки. ',
                         reply_markup=kb_main_set)


@dp.message_handler(commands=['rule'])
async def mes_rule(message: types.Message):
    await message.answer(f'{view.rul()}, {message.from_user.first_name}!',
                         reply_markup=kb_main_set)


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'Всего на столе конфет  - {count} шт.\n'
                         f'{message.from_user.first_name}, сколько ты возьмешь?')


@dp.message_handler(commands=['winner'])
async def mes_winner(message: types.Message):
    
    winner = list_winner()
    await message.answer(f'Пъедестал трюмфаторов 🍾🍾🍾:\n'
                         f'       1.🥇  {winner[-1]} \n'
                         f'       2.🥈  {winner[-2]} \n'
                         f'       3.🥉  {winner[-3]} \n',
                         reply_markup=kb_main_set)


@dp.message_handler()
async def mes_all(message: types.Message):
    global total

    if message.text.isdigit():
        user = int(message.text)
        if user in range(1, 29):
            total -= user
            if total == 0:
                await message.answer(f'🎈 {message.from_user.first_name}, поздравляю! \n'
                                     f'Ты победитель!!!')
                list_winner_write(message)
                winner = list_winner()
                await message.answer(f'Пъедестал трюмфаторов 🍾🍾🍾: \n'
                                     f'       1.🏅  {winner[-1]} \n'
                                     f'       2.🏅  {winner[-2]} \n'
                                     f'       3.🏅  {winner[-3]} \n')

            else:
                take_bot = taken_bot()
                total = total-take_bot
                if total <= 0:
                    await message.answer(f'🎉 Победа сегодня за мной!\nТы достойный соперник! ')
                    total = view.num_start
                else:
                    await message.answer(f'{random.choice(view.answer_list())}\n'
                                         f'Тогда я возьму - {take_bot} шт.\n '
                                         f'На столе осталось  конфет - {total} шт. ')

        elif user not in range(1, 29):
            await message.answer(f'Не хитри, не больше 28 конфет возьми ;)')
        elif user <= total:
            await message.answer(f'Нельзя взять конфет больше, чем на столе {total}')

    else:
        await message.answer(f':-) 😚')
    write_data(message)


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


@dp.message_handler(content_types='location')
async def mes_loc(message: types.Message):
    write_data(message)



