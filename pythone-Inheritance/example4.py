class CarInfo:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        (print(f"Make: {self.make}, Model: {self.model}"))


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start_engine(self):
        print("Engine started.")


class Car(CarInfo, Engine):
    def __init__(self, make, model, fuel_type):
        CarInfo.__init__(self, make, model)
        Engine.__init__(self, fuel_type)

    def display_info(self):
        CarInfo.display_info(self)
        print(f"Fule Type: {self.fuel_type}")

    def start_engine(self):
        Engine.start_engine(self)
        print(f"Car engine started")

car1 = Car("BMW",  "M5 competition", "gasoline")

car1.display_info()
car1.start_engine()