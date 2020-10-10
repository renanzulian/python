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


p = Person("Renan", datetime(1996, 6, 4), "123456789", 1.87, 86.513)
print(p.name)
