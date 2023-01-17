def sum(number1, number2):
    if number2 == 0:
        return number1
    return sum(number1 + 1, number2 - 1)

a = int(input('Введите первое число -> '))
b = int(input('Введите второе число -> '))
result = sum(a,b)
print('Сумма чисел равна', result)
