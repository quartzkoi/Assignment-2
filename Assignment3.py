import Shapes3D
import csv

class Solver:
    total = 0
    shapes = []

    with open("example.csv", mode='r') as file:
        csvFile = csv.reader(file, delimiter=',')
        for lines in csvFile:
            if lines[0] == "cube":
                shapes.append(Shapes3D.Cube(float(lines[1])))
            elif lines[0] == "cuboid":
                shapes.append(Shapes3D.Cuboid(float(lines[1]), float(lines[2]), float(lines[3])))
            elif lines[0] == "sphere":
                shapes.append(Shapes3D.Sphere(float(lines[1])))
            elif lines[0] == "cylinder":
                shapes.append(Shapes3D.Cylinder(float(lines[1]), float(lines[2])))
            elif lines[0] == "prism":
                shapes.append(Shapes3D.Prism(float(lines[1]), float(lines[2]), float(lines[3])))
            elif lines[0] == "area":
                for shape in shapes:
                    total += shape.area()
                total *= float(lines[1])
                shapes.clear()
            elif lines[0] == "volume":
                for shape in shapes:
                    total += shape.volume()
                total *= float(lines[1])
                shapes.clear()

    print(total)