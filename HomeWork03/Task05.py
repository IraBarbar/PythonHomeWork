# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


def fib_minus(n):
    if n in [-1]:
        return 1
    elif n in [-2]:
        return -1
    else:
        return fib_minus(n+2) - fib_minus(n+1)

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


import random
n = random.randint(1,13)
list_fib = []

for i in range(1, n+1):
    i = -i
    list_fib.append(fib_minus(i))
list_fib.reverse()


for i in range(0,n+1):
    if i == 0:
        list_fib.append(i)
    else:
        list_fib.append(fib(i))


print(f'Fibonacci list for number {n} :\n{list_fib}')
