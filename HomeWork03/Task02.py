# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
def random_list_int(lenth, start, finish):
    import random
    random_list = []
    for _ in range(lenth):
        index = 0
        random_list.append(int(random.uniform(start, finish)))
    return random_list


list01 = random_list_int(10, -10, 10)
list02 = random_list_int(9, -10, 10)

def product_elements(my_list):
    result = []
    j = -1
    i = 0
    for _ in range(i, len(my_list)):
        while i < (len(my_list)/2):
            sum = my_list[i] * my_list[j]
            result.append(sum)
            j = j - 1
            i = i + 1
    return print(f'Product of numbers is {result}')

print(list01)
result01 = product_elements(list01)

print(list02)
result02 = product_elements(list02)

