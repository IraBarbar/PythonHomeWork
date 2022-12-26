# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

data01 = open('file01.txt', 'r')
funk01 = data01.read()
data01.close()
print(funk01)
print()
data02 = open('file02.txt', 'r')
funk02 = data02.read()
data02.close()
print(funk02)
result = funk01 + ' + ' + funk02
result = result.replace(' ', '').replace('=0', '').split('+')

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
result_fun = ''
result_fun = list_to_function_str(list_elements)
print() 
print(result_fun)
