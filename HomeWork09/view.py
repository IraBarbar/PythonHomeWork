name_bot = 'Bro_Bot 🍒'
num_start =150


def answer_list():
    bot_answer = ['Какой хитрый ход!',
                'Вот это ты молодец!',
                'Xм, а тут надо подумать ;)',
                'Вау! У тебя есть все шансы на победу! ',
                'Давай старайся, я знаю, ты можешь хуже ))']
    return bot_answer

def rul():
    rule =(f' Правила :\n'
    f'☑️ Кто последний заберет со стола конфеты, тот и победил 🏆.\n'
    f'☑️ Нельзя брать больше 28 шт.\n'
    f'☑️ Команда:\n'
    f'           /set и число\n'
    f'определит изначальное количество конфет.\n'
    f'☑️ Иначе на столе будет {num_start} конфет.\n'
    f'☑️ В дельнейшем просто шли мне число, указывающее сколько конфет взято со стола.\n'
    f'Всё просто 👌\n'
    f'Удачи')
    return rule