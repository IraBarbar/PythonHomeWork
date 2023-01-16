# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random
def meeting():
    user_name = input("Player, what is your name? ")
    print(f'{user_name}, welcome!\n Good luck! ' )
    return user_name
count_player = 1
user_name =[]
for i in range(count_player):
    i = meeting()
    user_name.append(i)


all_candy = random.randint(10,200)
print(f'{all_candy} - all candies on the table.')

level_input = int(input(f'Input level: \n 1 - easy \n 2 - hard \n'))
while level_input not in range(2):
    level_input = int(input(f'Input level: \n 1 - easy \n 2 - hard \n'))
level = [1, 2]
if level_input  == level[0]:
     pass

taken_candy = 0
# first_move = random.choice(user_name)
# print(f'Player {first_move}  goes first!')


def move_player(player, taken, all):
    count = int(input(f'{player}, how many candies you take? : '))
    while count not in  range(1,29):
        count = int(input(f'{player}, input a number from 1 to 28. How many candies you take? : '))
    taken = taken + count
    print(f'{all - taken} - leftover candies')
    return taken
def move_bot(taken,all):
    count = random.randint(1,28)
    print(f'{count} - taken Bot. ')   
    taken = taken + count
    print(f'{all - taken} - leftover candies')
    return taken

def move_bot(taken,all):
    count = random.randint(1,28)
    print(f'{count} - taken Bot. ')   
    taken = taken + count
    print(f'{all - taken} - leftover candies')
    return taken
# for i in user_name:
#     if i != first_move:
#         second_move = i

# user_name[0]=first_move
# user_name[1]=second_move

while True:
    taken_candy = move_player(user_name[0], taken_candy, all_candy)
    if taken_candy > all_candy-1:
        print (f'{user_name[0]} - winner!')
        break              
    taken_candy = move_bot(taken_candy,all_candy)
    if taken_candy > all_candy-1:
        print (f'Bot - winner!')
        break
    
    
       