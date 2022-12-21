import random

N = int(input('Введите количество элементов в массиве -> '))
if N < 0:
    exit('Массив не может состоять из отрицательного количества элементов')
X = int(input('Введите число, которое необходимо проверить -> '))

array = []
for i in range(0, N):
    random_number = round(random.randint(1, N//2))
    array.append(random_number)

print('Случайный массив:')
print(array)

count = 0
for i in array:
    if i == X:
        count += 1

print('Введенное число встречается в массиве', count ,'раз(а)')
