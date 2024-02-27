class House:

    def __init__(self):
        self.numberOfFloors = 10

        for i in range(10):
            print("Текущий этаж равен", i + 1)

House()