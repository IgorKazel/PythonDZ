import functions as fn

def menu_print():
    menu_print_info = 'Введите номер действия:\n1 - Вывод списка автобусов\n2 - Вывод списка водителей\n3 - Вывод списка маршрутов\n4 - Выход в основное меню\n'
    while (True):
        fn.clear_screen()
        print(menu_print_info)
        number_action = input('> ')
        match number_action:
            case '1':
                fn.clear_screen()
                fn.print_bus()
                fn.exit_to_menu()
            case '2':
                fn.clear_screen()
                fn.print_driver()
                fn.exit_to_menu()
            case '3':
                fn.clear_screen()
                fn.print_route()
                fn.exit_to_menu()
            case '4':
                return            
            case _:
                print('\nНеверный ввод\n')
                fn.exit_to_menu()

def menu_add():
    menu_add_info = 'Введите номер действия:\n1 - Добавление автобуса\n2 - Добавление водителя\n3 - Добавление маршрута\n4 - Выход в основное меню\n'
    while (True):
        fn.clear_screen()
        print(menu_add_info)
        number_action = input('> ')
        match number_action:
            case '1':
                fn.clear_screen()
                fn.add_bus()
                fn.exit_to_menu()
            case '2':
                fn.clear_screen()
                fn.add_driver()
                fn.exit_to_menu()
            case '3':
                fn.clear_screen()
                fn.add_route()
                fn.exit_to_menu()
            case '4':
                return            
            case _:
                print('\nНеверный ввод\n')
                fn.exit_to_menu()

def menu_delete():
    menu_delete_info = 'Введите номер действия:\n1 - Удаление автобуса\n2 - Удаление водителя\n3 - Удаление маршрута\n4 - Выход в основное меню\n'
    while (True):
        fn.clear_screen()
        print(menu_delete_info)
        number_action = input('> ')
        match number_action:
            case '1':
                fn.clear_screen()
                fn.delete_bus()
                fn.exit_to_menu()
            case '2':
                fn.clear_screen()
                fn.delete_driver()
                fn.exit_to_menu()
            case '3':
                fn.clear_screen()
                fn.delete_route()
                fn.exit_to_menu()
            case '4':
                return            
            case _:
                print('\nНеверный ввод\n')
                fn.exit_to_menu()
