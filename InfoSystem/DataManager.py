
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
    # эксземпляра класса DataManager, работа с которым может вестить из InfoSyste
    def init_system(self):

        # Создаем новую компнию, если ничего н считалось или нет файлов
        
        self.positions = []

        self.positions.append(Position(200.0,TypeOfPositions.boss,TypeOfLevels.senior))
        
        self.positions.append(Position(50.0,TypeOfPositions.manager, TypeOfLevels.middle))
        
        self.positions.append(Position(600.0,TypeOfPositions.cleaner, TypeOfLevels.senior))



        self.persons = []

        self.persons.append(Person('Илья', 'Васильев', 'Андреевич', date(1988, 1, 15), TypeOfGenders.male))

        self.persons.append(Person('Вася', 'Ильин', 'Пупкин', date(1993, 5, 28), TypeOfGenders.male))


        self.employees = []

        self.employees.append(Employee(TypeOfDepartments.head, self.persons[0], self.positions[0]))
        
        self.employees.append(Employee(TypeOfDepartments.stuff, self.persons[1], self.positions[2]))

        # Теперь мы модем добавить человека с помощью консоли (завернув это в функцию)
        # После назначить должность. Перед эти предждложить выбрать человека из списка (ввод тлько номера из имеющися)  и тд

        return

    # Функиця добавляет человека. Это не влияет пока ни на что далее
    def add_person(self):

        print(' Добавте нового человека:')

        # Пока общая идея. Без проверок ввода

        self.persons.append(Person(
            input('Имя:'), 
            input('Фамилия:'), 
            input('Отчество:'), 
            date(input('Год рождения:'), input('Месяц рождения:'), input('Дата рождени:')), 
            TypeOfGenders(input('Выберите пол. Мужской пол: 1 , женский пол: 2'))))

        return

    # Функиця добавляет сотруника. Устанавлливает связь элемента массива persons и элемента массива position
    def add_employee(self):

        print(' Добавте нового сотрудника.')
                
        print(' Выберите доступного человека:')

        # Элементы массива или списка, поступающего на вход этой функции должены иметь функцию to_string() 
        IO_system.print_a_list_with_indexes(self.persons)

        person_index = IO_system.read_index(' Введите номер человека', 0, len(self.persons) - 1)

        
                
        print(' Выберите доступную должность:')

        IO_system.print_a_list_with_indexes(self.positions)

        position_index = IO_system.read_index(' Введите номер ддолжности', 0, len(self.positions) - 1)


                
        print(' Выберите отдел:')

        for dt in TypeOfDepartments:

            # Печатаем доступные варианты из перечисления TypeOfDepartments (код и имя)
            print(str(dt.value) + ': ' + str(dt.name))

        availableDepartmentCodes = [e.value for e in TypeOfDepartments]

        selectedDepartment = -1

        while selectedDepartment not in availableDepartmentCodes:

            selectedDepartment = int(input(' Введите код должности:'))


        # все готово для добавления сотрудника
        self.employees.append(Employee(TypeOfDepartments(selectedDepartment), self.persons[person_index], self.positions[position_index])) 

        return