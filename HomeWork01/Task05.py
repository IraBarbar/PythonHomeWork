# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
point_a = []
for i in range(2):
    point_a.append(int(input('Input coordinate point A pressing ENTER:')))

point_b = []
for i in range(2):
    point_b.append(int(input('Input coordinate point B pressing ENTER:')))

print('Coordinate A:', point_a, 'Coordinate B:', point_b)

if point_b[0] > point_a[0]:
    ac = point_b[0] - point_a[0]
else:
    ac = point_a[0] - point_b[0]

if point_b[1] > point_a[1]:
    bc = point_b[1] - point_a[1]
else:
    bc = point_a[1] - point_b[1]

ab = round(math.sqrt(ac**2 + bc**2),2)
print('Lenght AB = ', ab)
