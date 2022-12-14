# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
quart_list = [1, 2, 3, 4]
plus = 'from 0 to plus infinity'
minus = 'from 0 to minus infinity'

user = int(input(f'Input a number of the quarter : 1 or 2 or 3 or 4 : '))

while user not in quart_list:
    print = ('The wrong number !!!')
    user = int(input(f'Input a number of the quarter  1 or 2 or 3 or 4 : '))

if user == quart_list[0]:
    print (f' Range {user} of the quarte: \n X {plus}  \n Y {plus}')
elif user == quart_list[1]:
    print (f' Range {user} of the quarte: \n X {minus}  \n Y {plus}')
elif user == quart_list[2]:
    print (f' Range {user} of the quarte: \n X {minus}  \n Y {minus}')
elif user == quart_list[3]:
    print (f' Range {user} of the quarte: \n X {plus}  \n Y {minus}')