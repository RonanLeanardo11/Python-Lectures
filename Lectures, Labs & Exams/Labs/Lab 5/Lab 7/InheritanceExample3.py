class bankAccount:
    balance = 0
    deposit = 0
    withdraw = 0


    def __init__(self):
        self.balance = 0

    def depositdef (self,deposit_in):
        self.deposit = deposit_in
        self.balance += self.deposit


    def withdrawal (self, withdraw_amount):
        self.withdraw = withdraw_amount
        self.balance -= self.withdraw

    def getBalance (self):
        return self.balance

    def print(self):
        print("Balance is €{}".format(self.getBalance()))


# b1 = bankAccount()
# b1.depositdef(20)
# b1.withdrawal(15)
# b1.getBalance()
# b1.print()


class CurrentAccount(bankAccount):
    TransactionCount = 0

    def __init__(self):
        self.TransactionCount = 0



# ca1 = CurrentAccount()
# ca1.depositdef(20)
# ca1.withdrawal(15)
# ca1.print()

class SavingsAccount(bankAccount):
    interestRate = 0

    def __init__(self):
        self.interestRate = 0

    def add_interest(self):
        if self.balance < 0:
            self.interestRate += 2
        return self.interestRate

    def print(self):
        print("interest rate is {}".format(super.self.interestRate))

Sa1 = SavingsAccount()
Sa1.depositdef(30)
Sa1.withdrawal(15)
Sa1.print()
