# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 
# или 10*x² = 0
import random

k_stepen = random.randint(1,20)

def polynomial(k):
    list_polynomial = []
    for i in range(k+1):
        koefficient = random.randint(-100,100)
        if i == 0:
            list_polynomial.append((f'{koefficient}'))
        elif i == 1:
            if koefficient != 0:
                list_polynomial.append((f'{koefficient}*x'))   
        else:
            if koefficient != 0:
                list_polynomial.append((f'{koefficient}*x**{i}'))
    list_polynomial.reverse()
    return list_polynomial

def list_to_function_str(list_polynomial):
    sum = list_polynomial[0]
    for i in list_polynomial[1::]:
        if i[0] == '-':
            i_rep = i.replace('-','')
            if i != list_polynomial[-1]:
                sum =  sum +' - '+ i_rep
            elif len(list_polynomial) == 2:
                sum = sum  +' - '+ i_rep +' = 0'
            else:
                sum = sum +' - ' + i_rep + ' = 0'
        else:
            if i != list_polynomial[-1]:
                sum =  sum +' + ' + i
            elif len(list_polynomial) == 2:
                sum = sum  +' + '+ i +' = 0'
            else:
                sum = sum +' + ' + i +' = 0'      
    return sum
    
list_polynomial_01 = polynomial(k_stepen)
fun_01 = list_to_function_str(list_polynomial_01)
print(fun_01)
print()

k_stepen = random.randint(1,20)
list_polynomial_02 = polynomial(k_stepen)
fun_02 = list_to_function_str(list_polynomial_02)
print(fun_02)
print()


result = fun_01 + ' + ' + fun_02
result = result.replace(' ', '').replace('=0', '').replace('-', '+-').split('+')
result = list(filter(len, result))


start_count = 0
for i in result:
    if '**' in i:
        if int(i[i.find('**')+2:]) > start_count:
            start_count = int(i[i.find('**')+2:])        

list_elements = []
for count in range(start_count, 1, -1):
    sum = 0
    for i in result:        
        if i[i.find('**')+2::] == str(count) and 'x**' in i:
            if i.find('x') != 0 and ('-x' not in i) :
                sum = sum + int(i[:i.find('*x'):])
                new_string = str(sum) + str(i[i.find('*x')::])    
            elif '-x' in i:
                sum = sum - 1
                new_string = str(sum) +'*'+ str(i[i.find('x')::])             
            else:
                sum = sum + 1
                new_string = str(sum) +'*'+ str(i[i.find('x')::])               
    list_elements.append(new_string)
sum_x = 0
sum_n = 0
for i in result:
    if 'x' in i:
        if i[0] != 'x' and ('-x'  not in i):
            sum_x = sum_x + int(i[:i.find('*'):])
            new_string_n = str(sum_x) + '*x'          
        elif '-x' in i:
            sum_x = sum_x - 1
            new_string_n = str(sum_x) + '*x'           
    elif 'x' not in i:
        sum_n = sum_n + int(i)
        new_string_n = str(sum_n)   
list_elements.append(new_string_n)
print(list_elements)

result_fun = ''
result_fun = list_to_function_str(list_elements)
 
print(result_fun)






