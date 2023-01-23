# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
import random
num_start = random.randint(-100, 100)
list_two_num = []
if num_start < 0:
    num = -1*num_start
else:
    num = num_start

while num >= 1:
    i = num % 2
    num = num // 2
    list_two_num.append(i)
list_two_num.reverse()

result = str(list_two_num[0])
for i in list_two_num[1::]:
    i = str(i)
    result = result + i

if num_start < 0:
    result = '-' + result
print(f'{num_start} в двоичной системе = {result}')
