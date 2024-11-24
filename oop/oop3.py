# OOP Case Study: 2D Vector
from math import sqrt
class Vector:
    # Attributes: x,y Coordinates
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property #x getter
    def x(self):
        return self._x
    
    @property #y getter
    def y(self):
        return self._y

    #Make it representable and printable
    def __str__(self): # __str__() base override
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self): # __repr__() base override
        return self.__str__()
    
    # Vector Addition → returns a Vector
    # Let p = (x1, y1) and q = (x2, y2), the result of v + u is:
    # A new vector r = (x1+x2, y1+y2)
    
    def __add__(self, other_vector): # This allows Vector + Vector behaviour
        # self is Left operand of + operator
        # other_vector is the Right operand of the + operator
        return Vector(self.x + other_vector.x, self.y + other_vector.y)


    # Scalar Multiplication → returns a Vector
    # Let p = (x1,y1) and k be a scalar multiple, the result of k * Vector(u) is:
    # A new vector q = (k*x1, k*y2)
    def __mul__(self, scalar): # this is the base override of * operator
        return Vector(scalar*self.x , scalar*self.y)


    # Dot Product → returns a scalar numeric value
    # Let p = (x1, y1) and q = (x2, y2), then the dot product (p,q) is:
    # x1*x2 + y1*y2 → produces a scalar answer
    # Applications of dot product: angle b/w vectors, projection, Work & Force in Physics
    def dot_product(self, other_vector):
        return (self.x*other_vector.x) + (self.y*other_vector.y)


    # isOrthogonal → returns Boolean; True if two vectors are Orthogonal to each other
    # Let p = (x1, y1) and q = (x2, y2), then vectors p and q are orthogonal if the dot product of p and q equals 0.
    # Orthogonality of vectors means that the angle between the two vectors is 90 degrees
    def is_orthogonal(self, other_vector):
        return self.dot_product(other_vector) == 0


    # Scalar Distance from one to another → returns a scalar numeric value
    # Let p = (x1, y1) and q = (x2, y2), then the scalar distance from p to q is:
    # square_root( (x1-x2)^2 + (y1-y2)^2 )
    def distance(self, other_vector):
        return sqrt((self.x - other_vector.x)**2 + (self.y - other_vector.y)**2)

    # Magnitude of a Vector → returns a scalar numeric value
    # Let p = (x1, y1) then the magnitude of a vector |p| = the scalar distance from the origin (0,0) to the vector p
    def magnitude(self):
        return self.distance(Vector(0,0))
# end of Vector class

v1 = Vector(1,2)
v2 = Vector(5,10)
print(v1)
print(v2)

print(f"Distance from {v1} to {v2}: {v1.distance(v2)}")
print(f"Magnitude of {v2} is: {v2.magnitude()}")

dp = v1.dot_product(v2)
print(f"{v1} dot_product with {v2}: {dp}")

ortho = v1.is_orthogonal(v2)
print(f"Is {v1} orthongonal to {v2}?: {ortho}")

v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")

v4 = v1*3
print(f"{v1}*3 = {v4}")