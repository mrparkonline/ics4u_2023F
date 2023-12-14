# Polymorphism
# Rectangle & Circle
# Implement Area and Perimeter
# Both classes have the same method, but different behaviour.
# This shows how polymorphism works for oop

from math import sqrt, pi # for circle class

class Rectangle:
    def __init__(self, base, height):
        self._base = base # our attribute name cannot be the same as our property getter method names
        self._height = height
    
    # Setting up getter/setter for our two attributes
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, value):
        if isinstance(value, (int, float)):
            self._base = value
        else:
            raise ValueError("Improper Base Argument")
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if isinstance(value, (int, float)):
            self._height = value
        else:
            raise ValueError("Improper Height Argument")
    # Base/Height Setter Complete

    # Making our class printable
    def __str__(self):
        return f"Rectangle(base={self.base}, height={self.height})"
    
    def __repr__(self):
        return self.__str__()
    
    # Area
    def area(self):
        return self.base * self.height
    
    # Perimeter
    def perimeter(self):
        return 2 * (self.base + self.height)
# end of Rectangle

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def diameter(self):
        return self._radius*2
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if isinstance(value, (int, float)):
            self._radius = value
        else:
            raise ValueError("Improper radius")
    
    # Making our circle printable
    def __str__(self):
        return f"Circle(radius={self.radius})"
    
    def __repr__(self):
        return self.__str__()
    
    # Area
    def area(self):
        return pi * (self.radius ** 2)
    
    # Circumference
    def circumference(self):
        return 2 * pi * self.radius
# end of circle
    

rec1 = Rectangle(3,4)
print(f"rec1: {rec1}")
print(f"rec1 area: {rec1.area()} units squared")
print(f"rec1 perimeter: {rec1.perimeter()} units\n")

# Update rec1 attributes
print(f"Updated rec1 base to 5 and height to 10")
rec1.base = 5
rec1.height = 10
print(f"rec1: {rec1}")
print(f"rec1 area: {rec1.area()} units squared")
print(f"rec1 perimeter: {rec1.perimeter()} units\n")

# Created a Circle with a radius of 5.
cir1 = Circle(5)
print(f"cir1: {cir1}")
print(f"cir1 area: {round(cir1.area(), 2)} units squared")
print(f"cir1 circumference: {round(cir1.circumference(), 2)} units")
print(f"cir1 diameter: {cir1.diameter}")
