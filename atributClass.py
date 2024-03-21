from random import randint


class Building:
    total = 0

    def __init__ (self):
        Building.total += 1

Floors = []
NumberOfFloors = randint(0, 40)
while len(Floors) < NumberOfFloors:
    NewFloors = Building()
    Floors.append(NewFloors)
print(Building.total)