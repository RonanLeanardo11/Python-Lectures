# # Method Overloading
#
# #1
# def compound_interest(principal_amount, interest_rate, years=1):
#     amount = principal_amount * ((1 + (interest_rate / 100)) * years)
#     amount = round(amount, 2)
#     print("Total amount: ", amount)
#
# principal_amount = 50
# interest_rate = 2
# #years = 2
# compound_interest(principal_amount, interest_rate, years=2) # note if years set to 1 in def need to change when calling not set the variable as per line above

#2
#Definitions can have multiple purposes..

# def largest(number1, number2):
#     if len(number1) > len(number2):
#         print(number1)
#     elif len(number1) < len(number2):
#         print(number2)
#     else:
#         print("Numbers are equal")
#
# largest("Karen", "Mary")


# • Modify the above definition to allow for the user to
# either enter 2 numbers (to see which is larger), or enter
# two strings (to see which is longer):

def largest(number1=None, number2=None, name1=None, name2=None): # have to pass in None first
    if number1 is not None and number2 is not None:
        if number1 > number2:
            print(number1)
        elif number1 < number2:
            print(number2)
        else:
            print("Numbers are equal")
    if name1 is not None and name2 is not None:
        if len(name1) > len(name2):
            print(name1)
        elif len(name2) > len(name1):
            print(name2)
        else:
            print("Names length are equal")

largest(number1=10, number2=7)
largest(name1="Karent", name2="Darren")
