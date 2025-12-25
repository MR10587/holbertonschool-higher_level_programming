#!/usr/bin/python3
"""asda"""


class BaseGeometry:
    """sadasdas"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is int:
            if value > 0:
                pass
            else:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = integer_validator(self, name, width)
        self.__height = integer_validator(self, name, height)
