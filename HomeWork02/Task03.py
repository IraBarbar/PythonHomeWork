# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

import random
from random import randint
no_mix = range(20)
print(list(no_mix))

mix_list = []
for i in no_mix:
    i = random.choice(no_mix)
    while len(no_mix) != len(mix_list):
        i = random.choice(no_mix)
        if i not in mix_list:
            mix_list.append(i)
        else:
            del i
print(mix_list)

