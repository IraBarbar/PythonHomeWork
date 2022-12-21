# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def random_list_float(lenth, start, finish):
    import random
    random_list = []
    for _ in range(lenth):
        index = random.randint(0,3)
        random_list.append(round(random.uniform(start,finish),index))
    return random_list

list01 = random_list_float(10,0,20)
print(list01)

list_str =[]
for i in list01:
    list_str.append(str(i))

list_point=[]
for i in list_str:
    x = i.find('.')
    list_point.append(x)

list_result = []
j = 0
for i in list_str:
    x=i[list_point[j]::]
    a = '0'+x
    list_result.append(float(a))
    j+=1  
print(list_result)

num_max = list_result[0]
for i in list_result:
    if i != 0:
        num_min = i
        break

for i in list_result:
    if i < num_min and i !=0:
        num_min = i
    elif i > num_max:
        num_max = i
result = round((num_max - num_min),3)
print(result)







        
           

 

    






  
