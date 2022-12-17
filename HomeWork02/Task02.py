# Задайте список из n чисел последовательности (1 + 1/n)^n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

num = (input('Input a  positive integer number: '))
while num.isdigit() != True:
    num = (input('Input a  positive integer number: '))
    
num = int(num)
num_list = []
sum = 0

for i in range(1, num+1, 1):
    num_list.append(round(float(1/i+1)**i, 2))
print(f'The list of {num} - {num_list}')

for i in num_list:
    sum += i
print('The sum of the elements of the list: ', sum)
