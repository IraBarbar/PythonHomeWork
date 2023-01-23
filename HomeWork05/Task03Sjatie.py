# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
import string
data_open = open('HomeWork05/text1.txt', 'r')
data = data_open.read()
data_open.close()
print(data)

new_data = set(data)
new_data = sorted(list(new_data))
num = []
for i in new_data:
    if i in data:
        num_letters = data.count(i)
        num.append(num_letters)

result = str()
for i in range(len(num)):
    result = result + str(num[i]) + str(new_data[i])
print(result)


alph = []
for i in result:
    if i in string.ascii_lowercase:
        alph.append(i)

for i in alph:
    result = result.replace(i, ' ')
    
nums = result.split()
nums = list(map(int, nums))

my_revers = str()
for i in range(len(alph)):
    my_revers = my_revers + alph[i]*nums[i]
print(my_revers)

data_write = open('HomeWork05/text_write.txt', 'w')
data_write.writelines(my_revers)
data_write.close()
