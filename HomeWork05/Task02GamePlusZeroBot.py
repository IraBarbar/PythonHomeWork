# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
import random
win_field = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3],
             [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]


def print_field(field):
    print(*(field[0][0], field[1][0]), field[2][0])
    print(*(field[0][1], field[1][1]), field[2][1])
    print(*(field[5][0], field[5][1]), field[5][2])


print_field(win_field)

user_name = ['Player', 'Bot']
plus = '+'
zero = '0'
print(f'{user_name[0]} - {plus}.\n{user_name[1]} - {zero}')

def winner_is(field, simbol):
    for i in field:
        if i == [simbol, simbol, simbol]:
            return True

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
field_bot = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3],
             [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]

def move_player(field, user, simbol, num, bot):
    move_us = int(input(f'{user}, input the number: '))
    while move_us not in num:
        move_us = int(input(f'{user}, input the number: '))
    for i in range(len(field)):
        for j in range(3):
            if field[i][j] == move_us:
                field[i][j] = simbol
    num = list(filter((lambda i: i != move_us), num))
    bot = list(filter((lambda i: move_us not in i), bot))
    return field, num, bot   

def move_bot(field, user, simbol, num, bot):
    if len(bot) != 0:
        for e in bot:
            for j in e:
                move_us = random.choice(e)
    else:
        move_us = random.choice(num)
    print((f'{user}, input the number {move_us}'))
    for i in range(len(field)):
        for j in range(3):
            if field[i][j] == move_us:
                field[i][j] = simbol
    num = list(filter((lambda i: i != move_us), num))
    for e in bot:
        for j in e:
            if j == move_us:
                e.remove(j)
    return field, num, bot

while True:
    win_field, list_num, field_bot = move_player(
        win_field, user_name[0], plus, list_num, field_bot)
    print_field(win_field)
    x = winner_is(win_field, plus)
    if x == True:
        print(f'{user_name[0]} - winner!')
        break

    if len(list_num) == 0:
        print('End!')
        break

    win_field, list_num, field_bot = move_bot(
        win_field, user_name[1], zero, list_num, field_bot)
    print_field(win_field)
    # print(field_bot)
    x = winner_is(win_field, zero)
    if x == True:
        print(f'{user_name[1]} - winner!')
        break
