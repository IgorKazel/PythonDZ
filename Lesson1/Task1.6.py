number = int(input('Введите номер билета -> '))
if 99999 < number < 1000000:
    if number // 100000 + number // 10000 % 10 + number // 1000 % 10 == number // 100 % 10 + number // 10 % 10 + number % 10:
        print('Поздравляю! Ваш билет счастливый')
    else:
        print('У вас обычный билет')
else:
    print('Номер билета должен быть шестизначным')
