# import Definitions
import myDefinitions as mD

# pass in the two class instances - ** link class in Md to final costs
h1 = mD.Hotel("Hotel Marrion", "Ballsbridge", 2001, 200, True)
h2 = mD.Hotel("Hotel Lavery", "O'Connell Street", 1960, 90, False)

# Get Total and Average Costs
TotalCosts = h1.cost_insurance() + h2.cost_insurance()
AverageCosts = int(TotalCosts/2)
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


