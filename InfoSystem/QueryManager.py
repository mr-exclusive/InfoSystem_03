# Класс, в котором будут все запросы в базу данных и логика из обработки
# Вроде "Найти всех мидл-инженеров с такой-то зарплатой"

from DataManager import DataManager
from TypeOfDepartments import TypeOfDepartments


def employees_from_department(department: TypeOfDepartments, data_manager: DataManager):

    result = []

    for e in data_manager.employees:

        if e.department == department:

            result.append(e)

    return result
