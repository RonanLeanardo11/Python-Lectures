import math

list_ins_cost = []

class hotel:
    name = ""
    address = ""
    y_built = 0
    no_rooms = 0
    spa = bool(False)
    insurance_cost = 1000

    def __init__(self,name_in=None,address_in=None,y_built_in=None,no_rooms_in=None,spa_in=None,insurance_cost_in=None):
        if self.y_built < 0:
            self.y_built = 0
        else:
            self.y_built = y_built_in

        self.name = name_in
        self.address = address_in
        self.no_rooms = no_rooms_in
        self.spa =spa_in
        self.insurance_cost = insurance_cost_in == 1000

    def cost_insurance(self):
        self.insurance_cost = 1000 #have to set base within the definition or wont add
        if self.y_built < 1950:
            self.insurance_cost += 1000
        elif self.y_built > 1951 and self.y_built <= 1999:
            self.insurance_cost += 750
        elif self.y_built > 2000:
            self.insurance_cost += 500
        else:
            self.insurance_cost += 0

        if self.no_rooms < 25:
            self.insurance_cost += 300
        elif self.no_rooms > 25 and self.no_rooms <= 50:
            self.insurance_cost += 400
        elif self.no_rooms > 50 and self.no_rooms <= 100:
            self.insurance_cost += 650
        elif self.no_rooms > 100:
            self.insurance_cost += 900


        if self.spa == True:
            self.insurance_cost += 300



        list_ins_cost.append(self.insurance_cost)

    def print_details(self):
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Name", "Address", "Year Built", "Rooms NO's", "Spa", "Insurance Costs"))
        print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}\n".format(self.name, self.address, self.y_built, self.no_rooms, self.spa, self.insurance_cost))


# Instance 1 - H1
h1 = hotel()

h1.name = "Hotel Merrion"
h1.address = "Ballsbridge"
h1.y_built = 2001
h1.no_rooms = 200
h1.spa = True
h1.cost_insurance()


#Instance 2 - H2
h2 = hotel()

h2.name = "Hotel Lavery"
h2.address = "O'Connell Street"
h2.y_built = 1960
h2.no_rooms = 90
h2.spa = False
h2.cost_insurance()

for i in range(1):
    h1.print_details()
    h2.print_details()


#print(list_ins_cost)

    # Total costs
totalCosts = sum(list_ins_cost)

    # Average Costs
avergageCost = (totalCosts/2)

    # Hotel with highest costs
hotelhighestCosts = list_ins_cost.index(max(list_ins_cost)) #Find the index of the hotel with the highest costs
hotelhighestCosts += 1 # add one to index as starts at 0 not 1


    # Highest Costs per Hotel
highestCosts = max(list_ins_cost)


print("\n")
print("********************************************** Hotel Costs ***********************************************")
print("{0:<30} {1:<30} {2:<30} {3:<30}".format("Total Costs", "Average Costs", "Dearest Hotel", "Highest Costs"))
print("{0:<30} {1:<30} {2:<30} {3:<30}".format(totalCosts, avergageCost, hotelhighestCosts, highestCosts))
