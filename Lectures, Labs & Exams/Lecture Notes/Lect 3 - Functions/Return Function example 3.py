# Modify the below definition, to return the compound
# interest to the program body:
# • The years is 5
# • The principle amount is taken in from the user
# • The interest rate is 3.23%
# • Print out the total amount and interest made over the 5 years (Program Body)

# def compound_interest(principal_amount, interest_rate, years=1):
# amount = principal_amount * ((1 + (interest_rate / 100)) ** years)
# print("Total amount: ", amount)

# Print out the total amount and interest made over the 5
# years (Program Body)

def compound_interest(principal_amount, interest_rate, years=5):
    amount = principal_amount * ((1 + (interest_rate / 100)) ** years)
    return amount

interest_rate = 3.5
Amount = compound_interest(14,3)
principal_amount = int(input("Enter Principal amount: "))
print("Interest Rate: {}".format(interest_rate))
print("Amount: {}".format(Amount)) # Some reason amount not being picked up from return function
