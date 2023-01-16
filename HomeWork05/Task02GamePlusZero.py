# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
win_field =[[1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7]]


def print_field(field):    
    print(*(field[0][0],field[1][0]),field[2][0])    
    print(*(field[0][1],field[1][1]),field[2][1])
    print(*(field[5][0],field[5][1]),field[5][2])
print_field(win_field)

def meeting(i):
    user_name = input(f"Player №{i+1}, what is your name? ")
    print(f'{user_name}, welcome!\n Good luck! ' )
    return user_name

user_name =['Player №1', 'Player №2']
plus = '+'
zero = '0'
print(f'{user_name[0]} - {plus}.\n{user_name[1]} - {zero}')

# for i in range(2):
#     user_name[i]  = meeting(i) 

def winner_is(win_field, simbol):
    for i in win_field:
        if i == [simbol,simbol,simbol]:
            return True

def move_player(field,user,simbol):
    move_us = int(input(f'{user}, input the number: '))
    for i in range(len(field)) :
        for j in range(3):
            if win_field[i][j] == move_us:
                win_field[i][j] = simbol
    return field

def no_move(field):
    for i in range(len(field)) :
        for j in range(1,10):
            if j not in field[i] :
                return True

            
while True:
    win_field = move_player(win_field,user_name[0],plus)
    print_field(win_field)
    x=winner_is(win_field,plus)
    if x == True:
        print(f'{user_name[0]} - winner!')
        break

    win_field = move_player(win_field,user_name[1],zero)
    print_field(win_field)
    x = winner_is(win_field, zero)
    if x == True:
        print(f'{user_name[1]} - winner!')
        break


     
   