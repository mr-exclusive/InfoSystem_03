
# Класс для работы с файлами и вводом/выводом

from enum import Enum
import json
from DataManager import DataManager


class IO_system:

    def save_data_base(file_name:str, data_manager:DataManager, extention:str):

        if extention.lower() == '.txt':

            with open(file_name + '_persons' + extention, 'r', encoding="utf-8") as file:
                file.write(len(data_manager.persons) + '\n')

                for person in data_manager.persons:
                    file.write(person.to_txt_file() + '\n')

            with open(file_name + '_positions' + extention, 'r', encoding="utf-8") as file:
                file.write(len(data_manager.positions) + '\n')

                for position in data_manager.positions:
                    file.write(position.to_txt_file() + '\n')

            with open(file_name + '_employees' + extention, 'r', encoding="utf-8") as file:
                file.write(len(data_manager.employees) + '\n')

                for employee in data_manager.employees:
                    file.write(employee.to_txt_file(data_manager) + '\n')
                    


    def read_statement(file_name:str):
        with open (file_name, 'r', encoding="utf-8") as file:
            result = json.load(file)

        # Функция чтения файла состяния базы
        # вызываем в начале работы программы из DataManager
        # На входе имя файла или полный путь к нему
        # На выходе кортеж типа (persons, position, departments, employees)

        return result


    def write_statement(statement, file_name:str):
        with open (file_name,'w', encoding="utf-8") as file:
            json.dump(statement, file)

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

    pass


