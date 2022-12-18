import random

number = int(input('Введите количество монеток -> '))
if number < 1:
    exit('Монетка должна быть хотя бы одна)')

coins = []
for i in range(0, number):
    random_side = round(random.randint(0, 1))
    coins.append(random_side)

print('Последовательность монеток:')
print(coins)

count = 0
for i in coins:
    if i == 0:
        count += 1
if number - count < count:
    count = number - count

print('Чтобы все монетки были повернуты одной стороной нужно перевернуть', count)
