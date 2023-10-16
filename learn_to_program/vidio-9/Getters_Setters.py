class Square:
    def __init__(self, height=0, width=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        print('Retrieving the height')

        return self.__height

    @height.setter
    def height(self, value):
        value_str = str(value)
        if value_str.isdigit():
            self.__height = value_str
        else:
            print('Please only enter number for height')

    @property
    def width(self):
        print('Retrieving the width')

        return self.__width

    @width.setter
    def width(self, value):
        value_str = str(value)
        if value_str.isdigit():
            self.__width = value_str
        else:
            print('Please only eneter number for width')

    def get_area(self):
        return int(self.__width) * int(self.__height)


def main():
    a_square = Square()

    width = input('Enter the width :')
    height = input('Enter the height :')

    a_square.width = width
    a_square.height = height

    print('Height :', a_square.height)
    print('Width :', a_square.width)

    print("The Area of the square is : ", a_square.get_area())


main()
