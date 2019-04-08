# Create a class called DebitCard:
#  Class Variables
#  balance
class variables:
    balance = 0

    def __init__(self, balance_in=10):
        self.balance = balance_in

        #  lodge(amount)
        #  One argument, amount. Adds amount to balance if amount if > 0
        #  Returns True if successful, False if unsuccessful
    def lodgement(self,amount=0):
        if amount > 0:
            print("Lodgement Succesfull")
            self.balance += amount
        else:
            print("Lodgement Unsuccesfull")

        #  withdraw(amount)
        #  Returns True if the amount is less than the current balance and the amount is > 0. If this is True it
        # removes the amount from the balance. If not True return False.
    def Withdrawal(self,amount):
        if amount < self.balance and amount > 0:
            print("Withdrawal Succesfull")
            self.balance -= amount
        else:
            print("Withdrawal Unsuccessful")


        #  print_details()
        # ◦ method that prints all DebitCards details
    def myPrint(self):
        print("Final Balance is €{}: ".format(self.balance))

#  Test the class, create an instance and pass in arguments
#  Create a debit card
#  Print details


#  Withdraw 2 euro and print appropriate message if successful of not
#  Print details
#  Lodge 180 euro, and print appropriate message if successful or not

balance = 500
myBalance = variables(balance)

#myBalance.myPrint()

myBalance.lodgement(180)
myBalance.myPrint()

myBalance.Withdrawal(2)
myBalance.myPrint()

