import Shapes3D
import csv

class Solver:
    with open("data.csv", mode ='r')as file:
        csvFile = csv.reader(file, delimiter=',')
        for lines in csvFile:
            print(lines)