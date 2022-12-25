# Класс, в котором будут все запросы в базу данных и логика из обработки
# Вроде "Найти всех мидл-инженеров с такой-то зарплатой"

import DataManager
import TypeOfDepartments
import TypeOfPositions
import TypeOfLevels
from enum import Enum
import operator
import IO_system


class ComparisonOperator(Enum):
    EMPTY = -1
    GREATER = 1
    GREATER_OR_EQUAL = 2
    LESS = 3
    LESS_OR_EQUAL = 4
    EQUAL = 5


def get_operator(op):
    match op:
        case ComparisonOperator.GREATER:
            return operator.gt
        case ComparisonOperator.GREATER_OR_EQUAL:
            return operator.ge
        case ComparisonOperator.LESS:
            return operator.lt
        case ComparisonOperator.LESS_OR_EQUAL:
            return operator.le
        case ComparisonOperator.EQUAL:
            return operator.eq


# ищем сотрудников по отделу
def employees_from_department(department: TypeOfDepartments, data_manager: DataManager):
    return [empl for empl in data_manager.employees if empl.department == department]


def compare_salary(salary, salary_from, left_operand, salary_to=-1, right_operand=ComparisonOperator.EMPTY):
    if left_operand != ComparisonOperator.EMPTY:
        left_result = get_operator(left_operand)(salary, salary_from)

        if right_operand != ComparisonOperator.EMPTY:
            return left_result and get_operator(right_operand)(salary, salary_to)
        else:
            return left_result

    return False


# ищем сотрудников по диапазону зарплат
# можно использовать строгое или не строгое неравенство
# а так же сравнивать только с одним значением, тогда второе значение и оператор не передаются
def employees_salary(data_manager: DataManager, salary_from, left_operand, salary_to=-1, right_operand=ComparisonOperator.EMPTY):
    return [empl for empl in data_manager.employees if compare_salary(empl.position.salary,
                                                                      salary_from,
                                                                      left_operand,
                                                                      salary_to,
                                                                      right_operand)]


# ищем сотрудников по занимаемой должности
def employees_of_position(data_manager: DataManager, position: TypeOfPositions):
    return [empl for empl in data_manager.employees if empl.position.position_type == position]


# ищем сотрудников по уровню
def employees_of_level(data_manager: DataManager, level: TypeOfLevels):
    return [empl for empl in data_manager.employees if empl.position.position_level == level]


import QueryManager
from QueryManager import ComparisonOperator as cop

if __name__ == "__QueryManager__":
    data_manager = DataManager()
    data_manager.init_system()

    print('50 <= salary < 200')
    filtered_employees = QueryManager.employees_salary(data_manager, 100.0, cop.GREATER_OR_EQUAL, 200.0, cop.LESS)
    IO_system.print_a_list_with_indexes(filtered_employees)
    print('salary <= 200')
    filtered_employees = QueryManager.employees_salary(data_manager, 200.0, cop.LESS_OR_EQUAL)
    IO_system.print_a_list_with_indexes(filtered_employees)
    print('salary == 600')
    filtered_employees = QueryManager.employees_salary(data_manager, 600.0, cop.EQUAL)
    IO_system.print_a_list_with_indexes(filtered_employees)

    print('position == Boss')
    filtered_employees = QueryManager.employees_of_position(data_manager, data_manager.positions[0].position_type)
    IO_system.print_a_list_with_indexes(filtered_employees)

    print('level == middle')
    filtered_employees = QueryManager.employees_of_level(data_manager, data_manager.positions[1].position_level)
    IO_system.print_a_list_with_indexes(filtered_employees)