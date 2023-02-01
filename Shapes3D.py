import Shapes
import math
#Cuboid
    #Cube, child of Cuboid
#Cylinder / Sphere, both need circle
#N-gonal prism
class Cuboid:
    def __init__(self, height, width, length):
         self.width = width
         self.height = height    
         self.length = length
    def GetArea(self):
        return 2 *((self.width*self.length)(self.height*self.length)(self.height*self.width))
    def GetVolume(self):
        return self.height * self.length * self.width

class Clyinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.GetArea = self.GetArea()
        self.GetVolume = self.GetVolume()
    def GetArea(self):
        return (2*math.pi*self.radius*self.height)+(2*math.pi*(self.radius**2))
    def GetVolume(self):
        return math.pi*(self.radius**2)*self.height

class Sphere:
    def __(self, radius):
        self.radius = radius
    def GetArea(self):
        return (4*math.pi*(self.radius**2))
    def GetVolume(self):
        return ((4/3)*math.pi*(self.radius**3))

class Prism:
    def __init__(self, height, sideLength, sides):
        self.height = height
        self.base = Shapes.Polygon(sideLength, sides).GetArea
        self.perimeter = Shapes.Polygon(sideLength,sides).GetPerimeter

    def GetArea(self):
        return (self.perimeter * self.height) + (2 * self.base)
    def GetVolume(self):
        return self.base * self.height

class Cube(Cuboid):
    def __init__(self, length):
        self.length = length
    def GetArea(self):
        return super().GetArea()
    def GetVolume(self):
        return super().GetVolume()