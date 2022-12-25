from Person import Person
from Position import Position
from TypeOfDepartments import TypeOfDepartments
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels
from DataManager import DataManager

class Employee:

    department: TypeOfDepartments

    person: Person

    position: Position

    def __init__(self, department:TypeOfDepartments, person:Person, position:Position):

        self.department = department

        self.person = person

        self.position = position
                

    # Функция представления персоны в виде строки (вывод на консоль)
    def to_string(self):

        return self.person.to_string() + '   ' + \
            self.position.to_string() + ' (' + \
            str(self.department.value) + ')'


    
    

    # Функция для сохранения всех полей в текстовый файл
    def to_txt_file(self, data_manager:DataManager):

        return self.department.value + ' ' + \
               data_manager.persons.index(self.person) + ' ' + \
               data_manager.positions.index(self.position)

    

    # Функция чтения всех полей их текстовой строки
    def from_txt_file(self, line:str, data_manager:DataManager):

        splitted = line.split(' ')

        if len(splitted) < 3:

            return False

        try:
            self.department = TypeOfDepartments[int(splitted[0])]
            self.person = data_manager.persons[splitted[1]]
            self.position = data_manager.positions[splitted[2]]

            return True

        except:

            return False




