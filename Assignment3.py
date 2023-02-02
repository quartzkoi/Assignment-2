import Shapes3D
import csv

class Solver:
    total = 0 #create and empty list
    shapes = [] #create a buffer for area/volume calculations

    with open("example.csv", mode='r') as file: #open csv file as read-only
        csvFile = csv.reader(file, delimiter=',')
        for lines in csvFile: #for each line in the file, calculate per shape
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
                    total += shape.area() # Add up previous shape areas, then clear shape list
                total *= float(lines[1])
                shapes.clear()
            elif lines[0] == "volume":
                for shape in shapes:
                    total += shape.volume() # Add up previous shape volumes, then clear shape list
                total *= float(lines[1])
                shapes.clear()

    print(total) #Print total added value