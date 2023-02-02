import Shapes
import math
#Cuboid
class Cuboid:
    def __init__(self, height, width, length):
         self.width = width
         self.height = height    
         self.length = length
    def area(self):
        return 2 *((self.width * self.length)(self.height * self.length)(self.height * self.width))
    def volume(self):
        return self.height * self.length * self.width

#Cube, child of Cuboid
class Cube(Cuboid):
    def __init__(self, length):
        super().__init__(length, length, length)

#N-gonal prism
class Prism:
    def __init__(self, height, sideLength, sides):
        self.height = height
        self.base = Shapes.Polygon(sideLength, sides).GetArea
        self.perimeter = Shapes.Polygon(sideLength,sides).GetPerimeter

    def area(self):
        return (self.perimeter * self.height) + (2 * self.base)
    def volume(self):
        return self.base * self.height

#Cylinder
class Clyinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.base = Shapes.Circle(radius).GetArea()
        self.area = self.area()
        self.volume = self.volume()
    def area(self):
        return (self.base * self.height)+(2 * self.base)
    def volume(self):
        return self.base*self.height

#Sphere
class Sphere:
    def __(self, radius):
        self.radius = radius
    def area(self):
        return (4 * math.pi * (self.radius**2))
    def volume(self):
        return ((4/3) * math.pi * (self.radius**3))