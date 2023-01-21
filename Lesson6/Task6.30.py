import os

def clear_screen():
    os.system('cls')

def exit_to_menu():
    print('Для перехода в меню нажмите Enter')
    match input():
        case _: return

def print_all_data():
    clear_screen()
    count = 0
    print('Список контактов:\n')
    with open('phone_book.txt','r') as data:
        for line in data:
            count += 1
            split_line = line.split(', ')
            print(str(count) + '.',split_line[0],split_line[1],split_line[2],split_line[3])
    exit_to_menu()

def search_data_name():
    clear_screen()
    name_found = False
    count = 0
    name = input('Введите имя (фамилию, отчество) или часть: ')
    print()
    with open('phone_book.txt','r') as data:
        for line in data:
            if name in line:
                split_line = line.split(', ')
                print('Фамилия:',split_line[0],'\nИмя:',split_line[1],'\nОтчество:',split_line[2],'\nТелефон:',split_line[3])
                count += 1
                name_found = True
    if name_found:
        print('По вашему запросу найдено',count,'контактов\n')
    else:
        print('Контакта с таким именем не существует\n')
    exit_to_menu()

def search_data_phone():
    clear_screen()
    phone_not_found = True
    phone_number = input('Введите номер телефона: ')
    with open('phone_book.txt','r') as data:
        for line in data:
            split_line = line.split(', ')
            if split_line[3] == phone_number + '\n':
                print('\nКонтакт найден:\n')
                print('Фамилия:',split_line[0],'\nИмя:',split_line[1],'\nОтчество:',split_line[2],'\nТелефон:',split_line[3])
                phone_not_found = False
    if phone_not_found:
        print('\nКонтакта с таким номером телефона не существует\n')
    exit_to_menu()

def add_data():
    clear_screen()
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    second_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    data_to_save = last_name + ', ' + first_name + ', ' + second_name + ', ' + phone_number + '\n'
    with open('phone_book.txt','a') as data:
        data.write(data_to_save)
    print('\nКонтакт добавлен\n')
    exit_to_menu()

def delete_data():
    clear_screen()
    count = 0
    print('Список контактов:\n')
    with open('phone_book.txt','r') as data:
        for line in data:
            count += 1
            split_line = line.split(', ')
            print(str(count) + '.',split_line[0],split_line[1],split_line[2],split_line[3])
    check_number = False
    count = 0
    temp_data = ''
    number = int(input('Введите номер контакта для удаления: '))
    with open('phone_book.txt','r') as data:
        for line in data:
            count += 1
            if count == number:
                check_number = True
                continue
            temp_data += line
    with open('phone_book.txt','w') as data:
        data.write(temp_data)
    if check_number:
        print('\nКонтакт удален\n')   
    else:
        print('\nВведен неверный номер\n')  
    exit_to_menu()
   

def change_phone():
    clear_screen()
    count = 0
    print('Список контактов:\n')
    with open('phone_book.txt','r') as data:
        for line in data:
            count += 1
            split_line = line.split(', ')
            print(str(count) + '.',split_line[0],split_line[1],split_line[2],split_line[3])
    check_number = False
    count = 0
    temp_data = ''
    number = int(input('Введите номер контакта для смены номера телефона: '))
    with open('phone_book.txt','r') as data:
        for line in data:
            count += 1
            if count == number:
                phone_number = input('\nВведите новый номер телефона: ')
                split_line = line.split(', ')
                temp_data += split_line[0] + ', ' + split_line[1] + ', ' + split_line[2] + ', ' + phone_number + '\n'
                check_number = True
                continue
            temp_data += line
    with open('phone_book.txt','w') as data:
        data.write(temp_data)
    if check_number:
        print('\nНомер телефона изменен\n')   
    else:
        print('\nВведен неверный номер\n')  
    exit_to_menu()


menu = 'Введите номер действия:\n1 - Показать все записи\n2 - Найти запись по вхождению частей имени\n3 - Найти запись по телефону\n4 - Добавить новый контакт\n5 - Удалить контакт\n6 - Изменить номер телефона у контакта\n7 - Выход'

while (True):
    clear_screen()
    print(menu)
    number_action = input('\n> ')
    match number_action:
        case '1':
            print_all_data()
        case '2':
            search_data_name()
        case '3':
            search_data_phone()
        case '4':
            add_data()
        case '5':
            delete_data()
        case '6':
            change_phone()
        case '7':
            exit('\nСпасибо за использование телефонного справочника, до встречи)\n')
        case _:
            print('\nНеверный ввод\n')
            exit_to_menu()
        