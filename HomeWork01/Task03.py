# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#  в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print ('Please, input X :')
x = int(input())
print ('Please, input Y :')
y = int(input())

while x == 0 or y == 0:
    print('The wrong number!!!')
    print ('Please, input X :')
    x = int(input())
    print ('Please, input Y :')
    y = int(input())

if x > 0 and y > 0 :
    print (f'{x} and {y} - 1 quarter')
elif x < 0 and y > 0 :
    print (f'{x} and {y} - 2 quarter')
elif x < 0 and y < 0 :
    print (f'{x} and {y} - 3 quarter')
elif x > 0 and y < 0 :
    print (f'{x} and {y} - 4 quarter')

