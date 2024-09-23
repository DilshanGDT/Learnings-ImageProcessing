
import math

def rectangle_area(length, width):
    return length * width

def rectangle_circumference(length, width):
    return 2 * (length + width)

def rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("Rectangle Area : ", rectangle_area(length, width))
    print("Rectangle Circumference : ", rectangle_circumference(length, width))

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def circle():
    radius = float(input("Enter the radius of the circle: "))
    print("Circle Area : ", circle_area(radius))
    print("Circle Circumference : ", circle_circumference(radius))

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_circumference(base, length2, length3):
    return base + length2 + length3

def triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    length2 = float(input("Enter the length of the 2nd leg of the triangle: "))
    length3 = float(input("Enter the length of the 3rd leg of the triangle: "))
    print("Triangle Area : ", triangle_area(base, height))
    print("Triangle Circumference : ", triangle_circumference(base, length2, length3))

def parallelogram_area(base, height):
    return base * height

def parallelogram_circumference(base, side):
    return 2 * (base + side)

def parallelogram():
    base = float(input("Enter the base of the parallelogram: "))
    height = float(input("Enter the height of the parallelogram: "))
    side = float(input("Enter the side length of the parallelogram: "))
    print("Parallelogram Area:", parallelogram_area(base, height))
    print("Parallelogram Circumference:", parallelogram_circumference(base, side))

def shapeMenu():
    print('\na. Rectangle')
    print('b. Circle') 
    print('c. Triangle')
    print('d. Parallelogram')

    shape = input('\nEnter the shape that you want to find the Area & Circumstance - ')

    if(shape == 'a'):
        rectangle()
    elif(shape == 'b'):
        circle()
    elif(shape == 'c'):
        triangle()
    elif(shape == 'd'):
        parallelogram()
    else:
        print('Invalid Input!')

shapeMenu()