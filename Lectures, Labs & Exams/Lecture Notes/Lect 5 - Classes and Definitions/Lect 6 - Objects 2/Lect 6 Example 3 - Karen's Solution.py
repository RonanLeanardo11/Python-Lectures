# Create a class called DebitCard:
#  Class Variables
#  balance
class DebitCard:
    #balance = 0
    __balance = 0

    def __init__(self):
            self.__balance = 10

        #  lodge(amount)
        #  One argument, amount. Adds amount to balance if amount if > 0
        #  Returns True if successful, False if unsuccessful
    def lodge(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

        #  withdraw(amount)
        #  Returns True if the amount is less than the current balance and the amount is > 0. If this is True it
        # removes the amount from the balance. If not True return False.
    def withdraw(self, amount):
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

        #  print_details()
        # ◦ method that prints all DebitCards details
    def print_details(self):
        print("Balance :", self.__balance)

#  Test the class, create an instance and pass in arguments
#  Create a debit card
#  Print details

#  Withdraw 2 euro and print appropriate message if successful of not
#  Print details

#  Lodge 180 euro, and print appropriate message if successful or not

karenAcc = DebitCard()
karenAcc.print_details()

if karenAcc.withdraw(2):
    print("Money withdrew successfully")
else:
    print("Error, not enough funds")

karenAcc.print_details()
karenAcc.balance = 5000 # if want to reset the balance (Direct access to the variable - i have closed variable now though so this 5000 wont lodge)

if karenAcc.lodge(180):
    print("Money Lodged successfully")
else:
    print("error contact bank")

karenAcc.print_details()



