def compound_interest(principal_amount, interest, years = 1):
    amount_after_interest = principal_amount * ((1 + interest) ** years)
    print("{}".format(amount_after_interest))

principal_amount = int(input("Please enter amount: "))
interest = int(input("Please enter amount: "))
