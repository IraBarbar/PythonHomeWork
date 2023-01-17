# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
data_open = open('HomeWork05/text1.txt', 'r')
data = data_open.read()
data_open.close()
print(data)

new_data = set(data)
new_data=sorted(list(new_data))
num = []
for i in new_data:  
    if i in data:
        x=data.count(i)
        num.append(x)

result = str(str(num[0]) + str(new_data[0]))
for i in range(1,len(num))   :
    result = result +  str(num[i]) + str(new_data[i])
print(result)



# data = open('file01.txt', 'w')
# data.writelines(fun_01)
# data.close()    




        