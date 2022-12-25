
# Класс персоны (человека)
from datetime import date
from TypeOfGenders import TypeOfGenders

class Person:

    # Имя
    first_name: str
       
    # Фамилия
    last_name: str
       
    # Отчество
    middle_name: str
        
    # Дата рождения в структуре datetime
    date_of_birth: date

    # Пол
    gender: TypeOfGenders

    # Это "контсруктор" экземпляра класса. 
    # Здесь происходи создание нового человека из внешнего кода
    # self - это ключевое слово, указывающее на то, что это не просто функция,
    # а функция только для экземпляра класса
    def __init__(self, firstName:str, lastName:str, middleName:str, dob:date, gender:TypeOfGenders):

        self.first_name = firstName

        self.last_name = lastName

        self.middle_name = middleName

        self.date_of_birth = dob

        self.gender = gender


    # Функция представления персоны в виде строки (вывод на консоль)
    def to_string(self):

        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name + ' (' + \
            str(self.date_of_birth.day).zfill(2) + '.' + \
            str(self.date_of_birth.month).zfill(2) + '.' + \
            str(self.date_of_birth.year).zfill(4) + ')'


    # Функция для сохранения всех полей в текстовый файл
    def to_txt_file(self):

        return self.last_name + ' ' + \
               self.first_name + ' ' + \
               self.middle_name + ' ' + \
               str(self.date_of_birth.day).zfill(2) + ' ' + \
               str(self.date_of_birth.month).zfill(2) + ' ' + \
               str(self.date_of_birth.year).zfill(4) + ' ' + \
               str(self.gender.value)

    

    # Функция чтения всех полей их текстовой строки
    def from_txt_file(self, line:str):

        splitted = line.split(' ')

        if len(splitted) < 7:

            return False

        try:
            self.last_name = splitted[0]
            self.first_name = splitted[1]
            self.middle_name = splitted[2]
            self.date_of_birth = date(int(splitted[3]),int(splitted[4]),int(splitted[5]))
            self.gender = TypeOfGenders(int(splitted[6]))

            return True

        except:

            return False


