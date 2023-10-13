# Define a superclass with an attribute to be overridden
class Shape:
    color = "Blue"

    def print_color(self):
        print("color is Blue")


class Square(Shape):
    color = "red"

    def print_color(self):
        print("color is red")


shape = Shape()
square = Square()

shape.print_color()
square.print_color()
