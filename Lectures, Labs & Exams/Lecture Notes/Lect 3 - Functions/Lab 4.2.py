# Lab 4.2 X001522190

# Create a definition called “discount” that has two arguments. The first argument is the RRP and is
# required, the second argument is a percentage discount. The second argument should have a default
# value of 0.00% if the user only enters one argument the required RRP.
# The definition should print the sale price which is defined by the following formula:
# Test this definition with the values
# • 100, 50
# • 100
# • 100, 20

# Definition
def discount(RRP,discount_perc=0.00):
    sale_price = RRP * (1 - (discount_perc/100))
    sale_price = sale_price.__round__(2)
    print("Sale price is €{}".format(sale_price))

# inputs
RRP = int(input("Please enter the RRP: "))
discount_perc = float(input("Please enter discount %: "))

# Call Function - providing above inputs (RRP, discount_perc)
discount(RRP, discount_perc)



