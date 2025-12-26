#!/usr/bin/python3
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14159265359 * (self.radius ** 2)
        return f"Area: {area}"

    def perimeter(self):
        perimeter = 2 * 3.14159265359 * abs(self.radius)
        return f"Perimeter: {perimeter}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return f"Area: {area}"

    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return f"Perimeter: {perimeter}"


def shape_info(fiqur):
    print(fiqur.area())
    print(fiqur.perimeter())


circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
