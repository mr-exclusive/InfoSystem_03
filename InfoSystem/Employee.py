from Person import Person
from Position import Position
from TypeOfDepartments import TypeOfDepartments

class Employee:

    department: TypeOfDepartments

    person: Person

    position: Position

    def __init__(self, department:TypeOfDepartments, person:Person, position:Position):

        self.department = department

        self.person = person

        self.position = position





