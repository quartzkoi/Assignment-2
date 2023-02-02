import Shapes
import math

#Define variables of each shape, and set up calculation for area and volume
#Cuboid
class Cuboid:
    def __init__(self, height, width, length):
         self.width = width
         self.height = height    
         self.length = length
    def area(self):
        return 2 *((self.width * self.length) + (self.height * self.length) + (self.height * self.width))
    def volume(self):
        return self.height * self.length * self.width

#Cube, child of Cuboid
class Cube(Cuboid):
    def __init__(self, length):
        super().__init__(length, length, length)

#N-gonal prism
class Prism:
    def __init__(self, sides, sideLength, height):
        self.height = height
        self.base = Shapes.Polygon(sides, sideLength).GetArea()
        self.perimeter = Shapes.Polygon(sides, sideLength).GetPerimeter()

    def area(self):
        return (self.perimeter * self.height) + (2 * self.base)
    def volume(self):
        return self.base * self.height

#Cylinder
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius**2)
    def volume(self):
        return math.pi * self.height * (self.radius**2)

#Sphere
class Sphere:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (4 * math.pi * (self.radius**2))
    def volume(self):
        return ((4/3) * math.pi * (self.radius**3))