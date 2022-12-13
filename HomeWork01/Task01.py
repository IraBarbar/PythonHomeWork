# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Input a number from 1 to 7 :')
n = int(input())

weekday = range(1,6)
weekend = range(6,8)

while not n in weekday and not n in weekend :
    print('Input a number from 1 to 7 :')
    n = int(input())

if n in weekday :
    print(f'{n} - weekday :)')
elif n in weekend:
    print(f'{n} - weekend !')

