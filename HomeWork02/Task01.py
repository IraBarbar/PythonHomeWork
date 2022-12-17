# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

str_list = []
str_list = input('Input a real number: ')

sum = 0
for number in str_list:
    if number == '.' or number == '-':
        del number
    else:
        sum += int(number)
print('The sum of the digits of your number:' , sum)    

