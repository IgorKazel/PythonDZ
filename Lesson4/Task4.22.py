import random

def random_array(number):
    array = []
    for i in range(0, number):
        random_number = round(random.randint(1, 10))
        array.append(random_number)
    return array

n = int(input('Введите количество чисел в первом наборе -> '))
m = int(input('Введите количество чисел во втором наборе -> '))
if n < 0 or m < 0:
    exit('Набор не может состоять из отрицательного количества чисел')

array_1 = random_array(n)
print('Первый случайный набор чисел:')
print(array_1)
array_2 = random_array(m)
print('Второй случайный набор чисел:')
print(array_2)

array_i = sorted(set(array_1).intersection(set(array_2)))
print('Числа которые встречаются в обоих наборах (в порядке возрастания):')
print(array_i)
