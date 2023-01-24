import os

def clear_screen():
    os.system('cls')

def exit_to_menu():
    print('Для продолжения нажмите Enter')
    match input():
        case _: return



def print_all_data(file):
    count = 0
    with open(file,'r') as data:
        for line in data:
            count += 1
            print(str(count) + '.',line.strip('\n'))
        print()

def print_bus():
    print('Список автобусов:\n')
    print_all_data('bus.txt')

def print_driver():
    print('Список водителей:\n')
    print_all_data('driver.txt')

def print_route():
    print('Список маршрутов:\n')
    count = 0
    with open('marshrut.txt','r') as data_route:
        for line_route in data_route:
            count += 1
            split_line_route = line_route.strip('\n').split(', ')
            with open('bus.txt','r') as data_bus:
                for line_bus in data_bus:
                    split_line_bus = line_bus.strip('\n').split(', ')
                    if split_line_route[2] == split_line_bus[0]:
                        bus_in_route = split_line_bus[1]
            with open('driver.txt','r') as data_driver:
                for line_driver in data_driver:
                    split_line_driver = line_driver.strip('\n').split(', ')
                    if split_line_route[3] == split_line_driver[0]:
                        driver_in_route = split_line_driver[1]
            print(str(count) + '.',line_route[0] + ',',line_route[1] + ',',bus_in_route + ',',driver_in_route)
        print()



def add_bus():
    key_bus = input('Введите "ключ" автобуса: ')
    number_bus = input('Введите гос номер автобуса: ')
    data_to_save = key_bus + ', ' + number_bus + '\n'
    with open('bus.txt','a') as data:
        data.write(data_to_save)
    print('\nАвтобус добавлен\n')

def add_driver():
    key_driver = input('Введите "ключ" водителя: ')
    name_driver = input('Введите фамилию водителя: ')
    data_to_save = key_driver + ', ' + name_driver + '\n'
    with open('driver.txt','a') as data:
        data.write(data_to_save)
    print('\nВодитель добавлен\n')

def add_route():
    key_route = input('Введите "ключ" маршрута: ')
    number_route = input('Введите номер маршрута: ')
    key_bus = input('Введите "ключ" автобуса: ')
    key_driver = input('Введите "ключ" водителя: ')
    data_to_save = key_route + ', ' + number_route + ', ' + key_bus + ', ' + key_driver + '\n'
    with open('marshrut.txt','a') as data:
        data.write(data_to_save)
    print('\nМаршрут добавлен\n')



def delete_data(file):
    print_all_data(file)
    check_number = False
    count = 0
    temp_data = ''
    number = int(input('Введите номер контакта для удаления: '))
    with open(file,'r') as data:
        for line in data:
            count += 1
            if count == number:
                check_number = True
                continue
            temp_data += line
    with open(file,'w') as data:
        data.write(temp_data)
    if check_number:
        print('\nИнформация удалена\n')   
    else:
        print('\nВведен неверный номер\n')  

def delete_bus():
    delete_data('bus.txt')

def delete_driver():
    delete_data('driver.txt')

def delete_route():
    delete_data('marshrut.txt')