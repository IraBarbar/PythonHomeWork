# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
win_field = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3],
             [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]

def print_field(field):
    print(*(field[0][0], field[1][0]), field[2][0])
    print(*(field[0][1], field[1][1]), field[2][1])
    print(*(field[5][0], field[5][1]), field[5][2])

print_field(win_field)

def meeting(i):
    user_name = input(f"Player №{i+1}, what is your name? ")
    print(f'{user_name}, welcome!\n Good luck! ')
    return user_name

user_name = ['Player №1', 'Player №2']
plus = '+'
zero = '0'
print(f'{user_name[0]} - {plus}.\n{user_name[1]} - {zero}')

# for i in range(2):
#     user_name[i]  = meeting(i)

def winner_is(field, simbol):
    for i in field:
        if i == [simbol, simbol, simbol]:
            return True

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def move_player(field, user, simbol, num):
    move_us = int(input(f'{user}, input the number: '))
    while move_us not in num:
        move_us = int(input(f'{user}, input the number: '))
    for i in range(len(field)):
        for j in range(3):
            if field[i][j] == move_us:
                field[i][j] = simbol
    num = list(filter((lambda i: i != move_us), num))
    return field, num

count = 0
while True:
    win_field, list_num = move_player(win_field, user_name[0], plus, list_num)
    count += 1
    print_field(win_field)
    x = winner_is(win_field, plus)
    if x == True:
        print(f'{user_name[0]} - winner!')
        break

    if count > 8:
        print('End!')
        break

    win_field, list_num = move_player(win_field, user_name[1], zero, list_num)
    count += 1
    print_field(win_field)
    x = winner_is(win_field, zero)
    if x == True:
        print(f'{user_name[1]} - winner!')
        break
