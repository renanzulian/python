from datetime import datetime


class Person:
    def __init__(self, name: str, date_of_birth: datetime, document: str, height: float, weight: float):
        self.__name = name.title()
        self.__data_of_birth = date_of_birth
        self.__document = document
        self.__height = height
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def date_of_birth(self):
        return self.__data_of_birth

    @property
    def document(self):
        return self.__document

    @property
    def weight(self):
        return self.__weight

    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.name} - {self.__document}"


class Developer(Person):
    def __init__(self, name: str, date_of_birth: datetime, document: str, height: float, weight: float, language: str):
        Person.__init__(self, name, date_of_birth, document, height, weight)
        self.language = language


d = Developer("Renan", datetime.now(), "123456789", 1.87, 86.5, "Python")
print(d)
