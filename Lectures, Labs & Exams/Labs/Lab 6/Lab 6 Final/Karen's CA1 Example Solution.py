class Hotel:
     hotelName = ""
     hotelAddress = ""
     yearBuilt = 0
     hotelRoomsQty = 0
     hotelHasSpa = False

     def __init__(self, hotel_name="", hotel_address="", year_built=0, hotel_rooms=0, hotel_spa=False):
        self.hotelName = hotel_name
        self.hotelAddress = hotel_address

        if year_built >= 0:
            self.yearBuilt = year_built
        else:
            self.yearBuilt = 0

        if hotel_rooms >= 0:
            self.hotelRoomsQty = hotel_rooms
        else:
            self.hotelRoomsQty = 0
            self.hotelHasSpa = hotel_spa


     def print_details(self):
        print("*******************************")
        print(" Hotel Details ")
        print("*******************************")
        print("Name :", self.hotelName)
        print("Address :", self.hotelAddress)
        print("Year Built :", self.yearBuilt)
        print("Spa :", self.hotelHasSpa)
        print("Insurance Cost :", self.cost_insurance())

     def cost_insurance(self):
        base_price = 1000
        surcharge = 0

     # get surcharge based on year
        if self.yearBuilt < 1951:
            surcharge += 1000
        elif self.yearBuilt > 1999:
            surcharge += 500
        else:
            surcharge += 750

         # get surcharge based on room numbers
        if self.hotelRoomsQty < 25:
            surcharge += 300
        elif self.hotelRoomsQty < 51:
            surcharge += 400
        elif self.hotelRoomsQty < 101:
            surcharge += 650
        else:
            surcharge += 900

         # get spa surcharge
        if self.hotelHasSpa:
            surcharge += 300
         # finally return surcharge
        return base_price + surcharge

h1 = Hotel("Hotel Marion", "Ballsbridge", 2001, 200, True)
h2 = Hotel("Hotel Lavery", "O'Connell St", 1960, 90, False)
avergeCost = round((h1.cost_insurance() + h2.cost_insurance()) / 2,)

print("Hotel 1 insurance cost :", h1.cost_insurance())
print("Hotel 2 insurance cost :", h2.cost_insurance())
print("-------------------------------------------------")
print("Average insurance cost :", avergeCost)

if h1.cost_insurance() > h2.cost_insurance():
    h1.print_details()
elif h2.cost_insurance() > h1.cost_insurance():
    h2.print_details()
else:
    h1.print_details()
    h2.print_details()