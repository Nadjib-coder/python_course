"""
def sum_all(*args):
    _sum = 0
    for i in args:
        _sum += i
    return _sum


print("Sum =", sum_all(5, 3, 2, 15, 2, 1, 2))
"""
import math


def rectangle_area():
    length = float(input("Enter the Length of the rectangle : "))
    width = float(input("Enter the Width of the rectangle : "))
    area = length * width
    print("The area of this rectangle is :", area)


def circle_area():
    radius = float(input("Enter the radius of the circle : "))
    area = math.pi * math.pow(radius, 2)
    print("The area of this circle is {:.2f}".format(area))


def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please Enter 'rectangle' or 'circle'")


def main():
    shape_area = input("Get area for what shape : ")
    get_area(shape_area)


main()
