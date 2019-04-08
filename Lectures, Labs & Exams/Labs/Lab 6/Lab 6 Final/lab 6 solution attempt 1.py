# set class
class Hotel:
    hotelName = ""
    hotelAddress = ""
    yearBuilt = 0
    numberRooms = 0
    hasSpa = False

    # define initialiser
    def __init__(self, hotel_name="", hotel_address="", year_built=0, number_rooms=0, has_spa=False):
        self.hotelName = hotel_name
        self.hotelAddress = hotel_address
        self.hasSpa = has_spa

        # get year built
        if year_built < 0:
            self.yearBuilt = 0
        else:
            self.yearBuilt = year_built

        # get number of rooms
        if number_rooms < 0:
            self.numberRooms = 0
        else:
            self.numberRooms = number_rooms

    # definition for insurance cost calculations
    def cost_insurance(self):
        base_price = 1000
        surcharge = 0

        # get surcharge based on year built - we use the class now as all variables defined
        if self.yearBuilt <= 1950:
            surcharge += 1000
        elif self.yearBuilt >= 1951 and self.yearBuilt <= 1999:
            surcharge += 750
        elif self.yearBuilt >= 2000:
            surcharge += 500
        else:
            surcharge += 0

        # get surcharge based on number of rooms
        if self.numberRooms <= 25:
            surcharge += 300
        elif self.numberRooms >= 26 and self.numberRooms <= 50:
            surcharge += 400
        elif self.numberRooms >= 51 and self.numberRooms <= 100:
            surcharge += 650
        else:
            surcharge += 900

        # get surcharge if has spa
        if self.hasSpa:
            surcharge += 300

        # ** return insurance cost adding surcharge to base **
        return base_price + surcharge #returns value to the definition i.e. Cost insurance holds the total cost

    # define print function
    def print_details(self):
        print("*****************************")
        print("******* Hotel Details *******")
        print("*****************************")
        print("Hotel Name: {}".format(self.hotelName))
        print("Hotel Address: {}".format(self.hotelAddress))
        print("Year Built: {}".format(self.yearBuilt))
        print("Room Numbers: {}".format(self.numberRooms))
        print("Has Spa: {}".format(self.hasSpa))
        print("Insurance Cost: €{}".format(self.cost_insurance()))

# pass in the two class instances
h1 = Hotel("Hotel Marrion", "Ballsbridge", 2001, 200, True)
h2 = Hotel("Hotel Lavery", "O'Connell Street", 1960, 90, False)

# Get Total and Average Costs
TotalCosts = h1.cost_insurance() + h2.cost_insurance()
AverageCosts = round(TotalCosts/2,)
print("----------------------------")
print("Total Costs: €{}".format(TotalCosts))
print("Average Costs: €{}".format(AverageCosts))

# print individual hotel costs
print("----------------------------")
print("Hotel 1 Costs: €{}".format(h1.cost_insurance()))
print("Hotel 2 Costs: €{}".format(h2.cost_insurance()))
print("----------------------------")

# print most expensive hotel details - both if they match
if h1.cost_insurance() > h2.cost_insurance():
    print(h1.print_details())
elif h1.cost_insurance() < h2.cost_insurance():
    print(h2.print_details())
else:
    print(h1.print_details())
    print(h2.print_details())


