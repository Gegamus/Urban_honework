class Building:

    def __init__(self, gift=None):
        self.buildingType = []
        self.numberOfFloors = []
        if gift:
            self.buildingType.append(gift)

    def __eq__(self):
        return self.numberOfFloors == self.buildingType

buildindType = Building(gift="Много этажей")
numberOfFloors = Building(gift="50 этажей")
