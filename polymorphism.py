class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass

class Plane(Vehicle):
    pass

car1 = Car("audi", 750484)
boat1 = Boat("Ibiza", 93039)
plane1 = Plane("Boeing", 847)

for bluePrint in (car1, boat1, plane1):
    print(bluePrint.brand)
    print(bluePrint.model)