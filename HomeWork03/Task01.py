# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def random_list_int(lenth, start, finish):
    import random
    random_list = []
    for _ in range(lenth):
        index = 0
        random_list.append(int(random.uniform(start,finish)))
    return random_list

my_list = random_list_int(10,-10,10)
print(my_list)

negative_list = []
sum = 0
for i in my_list[::2]:
    sum +=i
    negative_list.append(i)
print(f'Elements in odd positions - {negative_list} . Sum = {sum}')
