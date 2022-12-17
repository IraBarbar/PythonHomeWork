# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

from random import randint
no_mix = range(20)

print(list(no_mix))

mix_list = []
for i in no_mix:
    i = randint(0,len(no_mix)-1)
    while len(no_mix) != len(mix_list):
        i = randint(0,len(no_mix)-1)
        if i not in mix_list:
            mix_list.append(i)
        else:
            del i
print(mix_list)

