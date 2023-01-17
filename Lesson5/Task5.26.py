def exponent(number, degree):
    if degree == 0:
        return 1
    if degree < 0:
        return 1 / number * exponent(number, degree + 1)
    return number * exponent(number, degree - 1)

n = int(input('Введите число -> '))
m = int(input('Введите степень, в которую его необходимо возвести -> '))
result = exponent(n, m)
print('Результат ->', result)
