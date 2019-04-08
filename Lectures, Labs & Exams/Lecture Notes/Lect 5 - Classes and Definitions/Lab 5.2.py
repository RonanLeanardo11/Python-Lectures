# Lab 5.2 Ronan Breen X00152190

# Create a class called PrintCard with the following attributes:
# accountNumber
# password
# numberOfCredits
# Create a print definition in the PrintCard class to print the attributes (excluding password)
# Test the class, by creating one instance of the PrintCard class. Set all attribute values and
# then using the class print definition, print out the PrintCard details.

# Create a Class
class PrintCard:
    accountNumber = "unknown"
    password = "unknown"
    numberOfCredits = "unknown"

    # Create a class definition
    def myPrintPrintCard(self):
        print("{0:<15} {1:<15}".format("Account Number", "Number of Credits")) # Leave out Password
        print("{0:<15} {1:<15}".format(self.accountNumber, self.numberOfCredits)) # Leave out Password


# Create a class instance
myPrintCard = PrintCard()

    # Assign attribute values to the class instance
myPrintCard.accountNumber = "12345465"
myPrintCard.password = "shdhsdhs"
myPrintCard.numberOfCredits = 10

    # Test outputting a class instance, calling the class print definition
myPrintCard.myPrintPrintCard()
