# Define a superclass with a method to be overidden
class Animal:
    def speak(self):
        print("This is the generic speek method in Animal.")

# Define a subclass that overrides the method
class Dog(Animal):
    def speak(self):
        print("Woof! This the speak method in Dog.")

# Creat  instance of the subclass
dog = Dog()
cat = Animal()

# Call the overriden method
dog.speak()
cat.speak()