
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels

class Position:
    
    # Зарплата
    salary: float

    # Тип ддолжности
    position_type: TypeOfPositions

    # Уровень должности
    position_level: TypeOfLevels

    def __init__ (self, salary:float,position_type:TypeOfPositions, position_level:TypeOfLevels):

        self.salary = salary

        self.position_type = position_type

        self.position_level = position_level

    # Функция представления должности в виде строки (вывод на консоль)
    def to_string(self):

        return str(self.position_level) + ' ' + str(self.position_type) + ' (' + str(self.salary) + ' рублей)'
