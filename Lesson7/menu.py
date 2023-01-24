import functions as fn
import submenu as sub

menu_info = 'Введите номер действия:\n1 - Вывод списков\n2 - Добавление в списоки\n3 - Удаление из списков\n4 - Выход\n'

while (True):
    fn.clear_screen()
    print(menu_info)
    number_action = input('> ')
    match number_action:
        case '1':
            sub.menu_print()
        case '2':
            sub.menu_add()
        case '3':
            sub.menu_delete()
        case '4':
            exit('\nСпасибо за использование справочника автобусного парка, до встречи)\n')
        case _:
            print('\nНеверный ввод\n')
            fn.exit_to_menu()
