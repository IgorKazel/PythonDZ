import random

N = int(input('Введите количество элементов в массиве -> '))
if N < 0:
    exit('Массив не может состоять из отрицательного количества элементов')
if N == 0:
    exit('В пустом массиве не будет ближайшего элемента')
X = int(input('Введите число, которое необходимо проверить -> '))

array = []
for i in range(0, N):
    random_number = round(random.randint(1, N))
    array.append(random_number)

print('Случайный массив:')
print(array)

result = array[i]
for i in array:
    if abs(i - X) < abs(result - X) or abs(i - X) == abs(result - X) and i < result:
        result = i

print('Самый близкий по величине элемент к заданному:', result)
