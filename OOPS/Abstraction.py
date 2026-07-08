
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = math.pi * self.radius **2

        print(f"The area of circle is {circle_area}sq.cm")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        rectangle_area = self.length * self.breadth
        
        print(f"The area of rectangle is {rectangle_area}sq.cm")

obj1 = Rectangle(4,5)
obj2 = Circle(3)

obj1.area()
obj2.area()

