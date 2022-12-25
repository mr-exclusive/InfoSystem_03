
# Класс, в котором будут все запросы в базу данных и логика из обработки
# Вроде "Найти всех мидл-инженеров с такой-то зарплатой"

from DataManager import DataManager
from TypeOfDepartments import TypeOfDepartments 


class QueryManager:

    def EmpluyeesFromDepartmentQuery(dep:TypeOfDepartments, dataManager:DataManager):

        result = []

        for e in dataManager.employees:

            if e.department == dep:

                result.append(e)

        return result

    pass