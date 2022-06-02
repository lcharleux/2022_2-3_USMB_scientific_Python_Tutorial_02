# A VECTOR/POINT CLASS DEMO
from math import sqrt
import numpy as np
import numbers

class MetaVector:
    def __init__(self, x=0., y=0., z=0.):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        x = self.x
        y = self.y
        z = self.z
        name = self.__class__.__name__
        return f"<{name}:x={x},y={y},z={z}>"

    def asarray(self):
        return np.array([self.x, self.y, self.z])

class Vector(MetaVector):
    """
    A vector class.
    """

    def norm(self):
        """
        Returns the norm of the vector.
        """
        x = self.x
        y = self.y
        z = self.z    
        return sqrt(x**2 + y**2 + z**2)

    def normalize(self):
        x = self.x
        y = self.y
        z = self.z    
        n = self.norm()
        out = Vector(x/n, y/n, z/n)
        return out

    def cross(self, other):
        a = self.asarray()
        oa = other.asarray()
        return Vector(*np.cross(a, oa))

    def scalarmul(self, other):
        return Vector(*(self.asarray() * other))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.cross(other)
        elif isinstance(other, numbers.Number):
            return self.scalarmul(other)   

    __rmul__ = scalarmul

class Point(MetaVector):
    def __sub__(self, other):
        a = self.asarray()
        oa = other.asarray()
        return Vector(*(a-oa))
        

u = Vector(x=3)
v = Vector(y=5)
A = Point()
B = Point(z = -5)