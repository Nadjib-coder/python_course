class CarInfo:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        (print(f"Make: {self.make}, Model: {self.model}"))


class Engine:
    def __init__(self, fuel_type, hp, liters, nm):
        self.fuel_type = fuel_type
        self.hp = hp
        self.liters = liters
        self.nm = nm

    def info_engine(self):
        print(f"Horse Power: {self.hp}")
        print(f"liters: {self.liters}")
        print(f"neoten meters: {self.nm}")


class Car(CarInfo, Engine):
    def __init__(self, make, model, fuel_type, hp, liters, nm):
        CarInfo.__init__(self, make, model)
        Engine.__init__(self, fuel_type, hp, liters, nm)

    def display_info(self):
        CarInfo.display_info(self)
        print(f"Fule Type: {self.fuel_type}")

    def start_engine(self):
        Engine.info_engine(self)

car1 = Car("BMW",  "M5 competition", "gasoline", 650, 4.4, 755)
ayoub_car = Car("mercedes", "gle", "Disel", 300, 3, 450)

# car1.display_info()
# car1.start_engine()

ayoub_car.display_info()
ayoub_car.start_engine()