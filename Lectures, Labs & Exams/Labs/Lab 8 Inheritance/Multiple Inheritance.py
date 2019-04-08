class Car:
    def __init__(self, makein):
        self.make = makein
        self.cc = 1600
    def print_car(self):
        print("Make ", self.make)
        print("CC ", self.cc)


class Driver:
    def __init__(self, namein):
        self.name = namein
        self.age = 30
    def print_driver(self):
        print("Driver Name ", self.name)
        print("Age ", self.age)

class RaceCar(Car, Driver):

    def __init__(self, makein, namein):
        Car.__init__(self, makein)
        Driver.__init__(self, namein)
        self.racesWon = 0
    def print(self):
        Car.print_car(self)
        Driver.print_driver(self)
        print("Races Won ", self.racesWon)

rc1 = RaceCar("Toyota", "Karen")
rc1.print()