# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 
# или 10*x² = 0
import random

k_stepen = random.randint(1,20)
print(k_stepen)

def polynomial(k):
    list_polynomial = []
    for i in range(k+1):
        koefficient = random.randint(0,100)
        if i == 0:
            list_polynomial.append((f'{koefficient}'))
        elif i == 1:
            if koefficient != 0:
                list_polynomial.append((f'{koefficient}*x'))   
        else:
            if koefficient != 0:
                list_polynomial.append((f'{koefficient}*x ** {i}'))
    list_polynomial.reverse()
    return list_polynomial

def sum(list_polynomial: str):
    sum = list_polynomial[0] + ' + '
    for i in list_polynomial[1::]:
        if i != list_polynomial[-1]:
            sum =  sum + i + ' + '
        else:
            sum = sum + i +' = 0'
    return sum
    
list_polynomial_01 = polynomial(k_stepen)
sum_01 = sum(list_polynomial_01)
print(sum_01)
print()

list_polynomial_02 = polynomial(k_stepen)
sum_02 = sum(list_polynomial_02)
print(sum_02)
print()

list_polynomial_03 = polynomial(k_stepen)
sum_03 = sum(list_polynomial_03)
print(sum_03)

data = open('file01.txt', 'w')
data.writelines(sum_01)
data.writelines(sum_02)
data.writelines(sum_03)
data.close()



