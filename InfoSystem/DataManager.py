# Класс, в котором будут функции работы с данными.
# Здесь хранятся все данные о людях в компании, доступных должностях и прочее.
# Здесь добавление, удаление людей, должностей, отделов, чтение и запись текущего состяния 
# базы данных в файл и устройство связей

from datetime import date
from Position import Position
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels
from TypeOfGenders import TypeOfGenders
from TypeOfDepartments import TypeOfDepartments
from Person import Person
from IO_system import IO_system
from Employee import Employee

class DataManager:
    
    positions = [] # массив должностей. Элементы массива - экземпляры класса Position

    persons = [] # массив людей. Элементы массива - экземпляры класса Person

    employees = [] # сотрудников.  Элементы массива - экземпляр класса Employee


    # Обратите внимание. Тут мы создаем не какие-то повисающие в воздухе пременные, а модифицируем переменные данного
    # экземпляра класса DataManager, работа с которым может вестись из InfoSyste
    def init_system(self):

        # Создаем новую компанию, если ничего не считалось или нет файлов

        """Создаем пустой список должностей"""
        self.positions = []

        """Добавляем в него людей в формате: зарплата, занимаемая должность, уровень знаний (junior, middle, senior)"""
        self.positions.append(Position(600.0,TypeOfPositions.boss,TypeOfLevels.senior))
        self.positions.append(Position(200.0,TypeOfPositions.manager, TypeOfLevels.middle))
        self.positions.append(Position(50.0,TypeOfPositions.cleaner, TypeOfLevels.junior))

        """Создаем пустой список людей"""
        self.persons = []

        """Добавляем в него людей в формате: имя, фамилия, отчество, дата рождения, гендер"""
        self.persons.append(Person('Илья', 'Васильев', 'Андреевич', date(1988, 1, 15), TypeOfGenders.male))
        self.persons.append(Person('Вася', 'Ильин', 'Пупкин', date(1993, 5, 28), TypeOfGenders.male))

        """Создаем пустой список сотрудников"""
        self.employees = []

        """Добавляем в него людей в формате: принадлежность к отделу компании, индекс человека, индекс должности"""
        self.employees.append(Employee(TypeOfDepartments.head, self.persons[0], self.positions[0]))
        self.employees.append(Employee(TypeOfDepartments.stuff, self.persons[1], self.positions[2]))

        """Результат на примере первого сотрудника компании: 
        Илья Васильев Андреевич 15.01.1988 г.р. 600$ зарплата, должность: босс, уровень знаний: middle, руководящее звено. """

        """Теперь мы можем добавить человека с помощью консоли (завернув это в функцию)
        После назначить должность. Перед этим предложить выбрать человека из списка (ввод только номера из имеющихся) и т.д."""
        
        return



    # Функция добавляет человека. Это не влияет пока ни на что далее
    def add_person(self):
        """Метод добавление нового человека (не путать с сотрудником)"""

        print('Добавьте нового человека: ')

        # Пока общая идея. Без проверок ввода

        self.persons.append(Person(
            input('Введите имя: '), 
            input('Введите фамилию: '), 
            input('Введите отчество: '), 
            date(int(input('Год рождения: ')), int(input('Месяц рождения: ')), int(input('День рождения: '))), 
            TypeOfGenders(int(input('Выберите пол. Мужской: 1 , Женский: 2 ')))))
    
        return


    def add_position(self):
        """Метод добавления новой должности для нового сотрудника"""

        print('Добавьте новую должность: ')

        selected_position = IO_system.select_from_enum(TypeOfPositions, "Выберите должность и введите ее код: ")

        selected_level = IO_system.select_from_enum(TypeOfLevels, "Выберите уровень знаний и введите его код: ")
        
        self.positions.append(Position(
            input("Введите заработную плату в месяц в $: "),
            selected_position, selected_level))
        
        print("\nСотрудник успешно добавлен!\n")
    
        return


    def get_employee(self):
        """Метод получения информации о сотруднике и его выбора из списка"""

        IO_system.print_a_list_with_indexes(self.employees)

        empl_index = IO_system.read_index("Введите номер сотрудника: ", 0, len(self.employees) - 1)

        return self.employees[empl_index]


        
    def change_position(self):
        """Метод изменения должности сотрудника"""

        print("Выберите сотрудника для изменения ему должности.\n")

        selected_employee = self.get_employee()

        answer = input("Вы действительно хотите изменить должность данному сотруднику? Введите 'Да' или 'Нет': ")

        if answer.lower() == "да":
            
            IO_system.print_a_list_with_indexes(self.positions)

            position_index = IO_system.read_index("Введите номер должности: ", 0, len(self.positions) - 1)

            selected_employee.position = self.positions[position_index]

            print("\nДолжность сотрудника успешно изменена!\n")

        elif answer.lower() == "нет":

            print("\nДолжность не будет изменен!\n")
        
        else:

            print("\nНекорректный ввод!\n")

        return



    def change_salary(self):
        """Метод изменения заработной платы сотрудника"""

        print("Выберите сотрудника для изменения ему заработной платы.\n")

        selected_employee = self.get_employee()

        answer = input("Вы действительно хотите изменить зарплату данному сотруднику? Введите 'Да' или 'Нет': ")

        if answer.lower() == "да":

            new_salary = float(input("Введите новую заработную плату в месяц в $: "))

            new_position = Position(new_salary, selected_employee.position.position_type, selected_employee.position.position_level)

            self.positions.append(new_position)

            selected_employee.position = new_position

            print("\nЗарплата сотрудника успешно изменена!\n")

        elif answer.lower() == "нет":

            print("\nЗарплата сотрудника не будет изменена!\n")
        
        else:

            print("\nНекорректный ввод!\n")
            
        return

        
    def change_department(self):
        """Метод изменения отдела для сотрудника"""

        print("Выберите сотрудника для изменения ему отдела.\n")

        selected_employee = self.get_employee()

        answer = input("Вы действительно хотите изменить отдел данному сотруднику? Введите 'Да' или 'Нет': ")

        if answer.lower() == "да":

            selected_department = IO_system.select_from_enum(TypeOfDepartments, "Введите код отдела: ")

            selected_employee.department = selected_department

            print("\nСотрудник успешно переведен в другой отдел\n")

        elif answer.lower() == "нет":

            print("\nОтдел сотрудника не будет изменен!\n")

        else:

            print("\nНекорректный ввод!\n")
            
        return

    
    def delete_employee(self): # тестовая функция
        """Метод увольнения сотрудника из компании"""

        print("Выберите сотрудника, которого вы хотите уволить.\n")

        print("Выберите доступного сотрудника: ")

        selected_employee = self.get_employee()

        answer = input("Вы действительно хотите удалить данного сотрудника из компании? Введите 'Да' или 'Нет': ")

        if answer.lower() == 'да':

            self.employees.remove(selected_employee)

            print("\nСотрудник был уволен из компании, осталось только убрать из базы его имя!\n")
                    
        elif answer.lower() == "нет":

            print("\nСотрудник не будет уволен!\n")

        else:

            print("Некорректный ввод!")
            
        return


    # Функция добавляет сотрудника. Устанавливает связь элемента массива persons и элемента массива position
    def add_employee(self):

        print('Добавьте нового сотрудника.')
                
        print('Выберите доступного человека: ')

        # Элементы массива или списка, поступающего на вход этой функции должны иметь функцию to_string() 
        IO_system.print_a_list_with_indexes(self.persons)

        person_index = IO_system.read_index('Введите номер человека: ', 0, len(self.persons) - 1)

                
        print(' Выберите доступную должность:')

        IO_system.print_a_list_with_indexes(self.positions)

        position_index = IO_system.read_index(' Введите номер должности', 0, len(self.positions) - 1)

                
        print(' Выберите отдел:')

        selected_department = IO_system.select_from_enum(TypeOfDepartments, "Введите код отдела: ")


        # все готово для добавления сотрудника
        self.employees.append(Employee(TypeOfDepartments(selected_department), self.persons[person_index], self.positions[position_index])) 

        return