import random
class DebitCard:
    __balance = 0
    __pinNumber = 0


    def __init__(self):
        self.__balance = 10
        self.__pinNumber = random.randint(1000, 9999)
        print("Pin number:", self.__pinNumber)


    def lodge(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False


    def withdraw(self, amount, pin_number):
        if amount > 0 and amount < self.__balance and pin_number == self.__pinNumber:
            self.__balance -= amount
            return True
        else:
            return False


    def print_details(self):
        print("Balance :", self.__balance)

# Instance
karenAcc = DebitCard()

karenAcc.print_details()

amount = float(input("Please enter amount :"))
pin = int(input("please enter pin :"))

if karenAcc.withdraw(amount, pin):
    print("Money withdrew successfully")
else:
    print("Error, not withdrawn")

karenAcc.print_details()