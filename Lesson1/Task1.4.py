number = int(input('Введите общее число журавликов -> '))
if number % 6 == 0:
    print('Петя сделал', number // 6, 'журавликов')
    print('Катя сделала', number // 6 * 4, 'журавликов')
    print('Сережа сделал', number // 6, 'журавликов')
else:
    print('Число не подходит для решения задачи')