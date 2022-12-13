# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print  ('Input X:') 
x = int(input())
print ('Input Y:') 
y = int(input())
print ('Input Z:') 
z = int(input())

a = not (x or y or z)
b = not x and not y and not z

print(a == b)