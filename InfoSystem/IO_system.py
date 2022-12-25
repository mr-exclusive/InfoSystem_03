
# Класс для работы с файлами и вводом/выводом

from enum import Enum
from typing import Tuple


class IO_system:

    def read_statement(file_name:str):

        # Функция чтения файла состяния базы
        # вызываем в начале работы программы из DataManager
        # На входе имя файла или полный путь к нему
        # На выходе кортеж типа (persons, position, departments, employees)

        return

    def write_statement(statement:Tuple):

        # Функция записи состояния базы данных в файл
        # вызываем в конце работы программы из DataManager
        # На входе кортеж типа (persons, position, departments, employees)

        return
    

    def read_index(message:str, minIndex:int, maxIndex:int):

        index = minIndex - 1

        while index < minIndex or index > maxIndex:

            index = int(input(message)) - 1

        return index
    

    def print_a_list_with_indexes(list_to_print):

        index = 1

        for item in list_to_print:

            print(str(index) + '. ' + item.to_string())

            index += 1


    def select_from_enum(enm:Enum, message:str):

        for dt in enm:
            
            print(str(dt.value) + ': ' + str(dt.name))

        availableDepartmentCodes = [e.value for e in enm]

        selectedDepartment = -1

        while selectedDepartment not in availableDepartmentCodes:

            selectedDepartment = int(input(message))

        return selectedDepartment


