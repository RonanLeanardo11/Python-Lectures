class Car:
    make = ""
    model = ""
    cc = 0

    def __init__(self):
        self.model = "Honda"
        self.make = "Accord"
        self.cc = 1298

    def print(self):
        print("Make ", self.make)
        print("Model ", self.model)
        print("CC ", self.cc)

class RaceCar(Car):
    racesWon = 0

    def __init__(self):
        Car().__init__()
        self.racesWon = 0

    def print(self):
        Car().print()
        print("RacesWon", self.racesWon)


car1 = RaceCar()
car1.print()