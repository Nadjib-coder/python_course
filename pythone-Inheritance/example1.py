# Define a superclass (parent class) for general cars
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.year} {self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.year} {self.make} {self.model} is stopping.")

# Define a subclass (dreived class) for electric cars, inheriting from Car


class ElectricCar(Car):
    def __init__(self, make, model, year, battrey_size):
        # Call the constructor of the superclass (Car) using super()
        super().__init__(make, model, year)
        self.battrey_size = battrey_size

    def charge(self):
        print(f"{self.year} {self.make} {self.model} with a {self.battrey_size}--kwh is charging.")


# Creat instance of the classes
car1 = Car("Toyota", "Camry", 2022)
electric_car1 = ElectricCar("Tesla", "Model S", 2023, 100)

# Call method on the instances
car1.start()
car1.stop()

electric_car1.start()
electric_car1.stop()
electric_car1.charge()
