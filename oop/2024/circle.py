# Circle Class in Python
from math import pi

class Circle:
    def __init__(self, radius, diameter=None):
        self.__radius = radius
        self.__diameter = 2 * self.radius
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def diameter(self):
        return self.__diameter
    
    def getArea(self):
        return pi * self.radius * self.radius
    
    def getCircumference(self):
        return 2 * pi * self.radius
# end of Circle()

test_circle = Circle(3)
print(test_circle.radius, test_circle.diameter)
print(test_circle.getArea(), test_circle.getCircumference())
