class Car:

    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 0


class Nissan(Car):

    def __init__(self):
        super().__init__()
        self.price = 1800000

    def horse_powers(self):
        return 250


class Kia(Car):

    def __init__(self):
        super().__init__()
        self.price = 1250000

    def horse_powers(self):
        return 115