
# Точка входа программы
# Здесь будет вызываться головной метод из класса DataManager
# Что-то вроде init_system()

from Menutext import *
import os
import click
from IO_system import IO_system
from DataManager import DataManager
from QueryManager import QueryManager as qm
from TypeOfDepartments import TypeOfDepartments


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def zaglushka():
    print('Здесь могла бы быть ваша реклама')


def menu(list_command: dict, invate: str):
    flag = True
    while flag:
        print(invate)
        command = input('Команда: > ')
        if command in list_command:
            list_command[command]()
            if command != '9':
                click.pause()
        elif command == "0" or command == '':
            flag = False
        else:
            print('Такой команды нет!!!')


def sub_menu_print_base(data_manager:DataManager):

    def print_per():
        IO_system().print_a_list_with_indexes(data_manager.persons)

    def print_pos():
        IO_system().print_a_list_with_indexes(data_manager.positions)

    def print_emp():
        IO_system().print_a_list_with_indexes(data_manager.employees)

    print_command = {'1': print_per,
                     '2': print_pos, '3': print_emp, '9': clear}
    menu(print_command, menu_print)


def sub_menu_append():
    append_command = {'1': DataManager().add_person,
                      '2': DataManager().add_employee, '9': clear}
    menu(append_command, menu_append)


def sub_menu_delete():
    delete_command = {'1': zaglushka, '2': zaglushka, '9': clear}
    menu(delete_command, menu_delete)


def sub_menu_query():
    def query_by_dep():
        print(' Выберите отдел:')
        for dt in TypeOfDepartments:
            print(str(dt.value) + ': ' + str(dt.name))
        availableDepartmentCodes = [e.value for e in TypeOfDepartments]
        selectedDepartment = -1
        while selectedDepartment not in availableDepartmentCodes:
            selectedDepartment = int(input(' Введите код отдела: '))
        IO_system().print_a_list_with_indexes(qm().EmpluyeesFromDepartmentQuery(
            TypeOfDepartments(selectedDepartment), DataManager()))
    query_command = {'1': query_by_dep, '2': zaglushka, '9': clear}
    menu(query_command, menu_query)


def main():
    DataManager().init_system()
    head_command = {'1': sub_menu_print_base, '2': sub_menu_append,
                    '3': sub_menu_delete, '4': sub_menu_query, '9': clear}
    menu(head_command, menu_head)
    # Тут должен быть метод сохранения базы


main()
