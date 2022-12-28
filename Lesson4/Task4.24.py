import random

def random_array(number):
    array = []
    for i in range(0, number):
        random_number = round(random.randint(1, 10))
        array.append(random_number)
    return array

n = int(input('Введите количество кустов -> '))
if n < 1:
    exit('Нет кустов - нет ягод)')

array_berries = random_array(n)
print('Список урожайности кустов:')
print(array_berries)

if n == 1:
    print('Количество ягод, которые можно собрать с одного куста ->', array_berries[0])
    exit()
if n == 2:
    print('Количество ягод, которые можно собрать с двух кустов ->', array_berries[0] + array_berries[1])
    exit()

max = 0
for i in range(n):
    if array_berries[i-2] + array_berries[i-1] + array_berries[i] > max:
        max = array_berries[i-2] + array_berries[i-1] + array_berries[i]
print('Максимальное количество ягод которое которое можно собрать с трех соседних кустов ->', max)
