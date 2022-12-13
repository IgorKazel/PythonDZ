number = int(input('Введите трехзначное число -> '))
if 99 < number < 1000:
    sum_numbers = number % 10 + number // 10 % 10 + number // 100
    print('Сумма цифр трехзначного числа равна', sum_numbers)
else:
    print('Число не трехзначное')
