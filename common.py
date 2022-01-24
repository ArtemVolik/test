from typing import Optional
from string import ascii_letters
from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def add_to_team(self):
        pass

    @abstractmethod
    def drop(self):
        pass


class ServiceFunctionality(Base):
    def add_to_team(self, object):
        if object not in self._team:
            self._team = object

    def drop(self, object):
        self._team.remove(object)


class VerifiedField:
    """Data descriptor for Hero class attributes"""
    allowed_letters = ascii_letters + " "

    def __init__(
            self, value_class,
            minimum_value: Optional[int] = None,
            maximum_value: Optional[int] = None,
            size: Optional[int] = None,
            tiny_int: int = 0,
    ):

        self.__value_class = value_class
        self.__minimum_value = minimum_value
        self.__maximum_value = maximum_value
        self.__size = size
        self.__tiny_int = tiny_int

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if self.name == "_is_good":
            return bool(instance.__dict__[self.name])

        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.__value_class):
            raise TypeError(f'Value should be {instance.__value_class}')

        if isinstance(value, int) and (self.__maximum_value or self.__minimum_value):
            if value > self.__maximum_value or value < self.__minimum_value:
                raise TypeError(f'Value should be in ({self.__minimum_value} {self.__maximum_value})')

        if isinstance(value, str):
            if len(value) < self.__size:
                raise TypeError(f'Value should be {self.__size} minimum')
            if not all([letter in self.allowed_letters for letter in value]):
                raise TypeError('Should contains latin alphabet letters only')

        if self.__tiny_int:
            if value not in [1, 0]:
                raise TypeError('Should be 0/1 value')
        instance.__dict__[self.name] = value


class Team:
    def __init__(self, value_class):
        self.__value_class = value_class

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value:
            instance.__dict__[self.name] = set()
        else:
            if not isinstance(value, self.__value_class):
                raise TypeError(f"Value should be {self.__value_class} object")
            if instance.is_good ^ value.is_good:
                raise TypeError("Team and Hero must be same good/bad type")
            instance.__dict__[self.name].add(value)