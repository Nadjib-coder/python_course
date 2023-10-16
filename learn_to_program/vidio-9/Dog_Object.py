class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.weight = weight
        self.height = height

    def run(self):
        print("{} dog is runs".format(self.name))

    def eat(self):
        print("{} dog is eats".format(self.name))

    def bark(self):
        print("{} dog is barks".format(self.name))


def main():
    spot = Dog("Spot", 66, 26)
    spot.bark()

    bowser = Dog()
    bowser.bark()
    bowser.name = "Bowser"
    bowser.bark()


main()
