class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height

# Creat an instance
rectangle = Rectangle(5, 3)

# calculate the area
area = rectangle.calculate_area()

# print the result of calculation
print("area:", area)