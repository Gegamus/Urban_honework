class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1000000

    def horse_powers(self):
        return 0


class Nissan(Car):

    def __init__(self):
        super().__init__()
        self.vehicle_type = "Nissan"
        self.price = 1500000

    def horse_powers(self):
        return 255


nissan = Nissan()
print(nissan.vehicle_type)
print(nissan.price)