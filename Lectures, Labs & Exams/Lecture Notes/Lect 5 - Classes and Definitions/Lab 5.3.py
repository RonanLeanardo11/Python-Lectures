# Lab 5.3 Ronan Breen X00152190

# Building upon Q1 and Q2. You can assume that the instance of the Student and the instance
# of the PrintCard are related. That is to say that the Print Card is the Students print card.
# Then (using both instances only): Calculate the average of the Students 2 CA grades. If the
# students average CA grade is >= 70, you may add a bonus of 400 credits to the PrintCard.
# Then print the PrintCard credits to confirm if this code worked successfully.

# Create Class
class Student:
    studentID = "unknown"
    name = "unknown"
    subject = "unknown"
    ca1Result = 0 # made int
    ca2result = 0 # made int
    averageCAResult = 0 # made int

    # Create Class print Definition
    def myStudentPrint(self):
        print("\n**************************************** Student Details ******************************************")
        print("---------------------------------------------------------------------------------------------------")
        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15} {5:<15}".format("Student ID", "Name", "Subject", "CA1 Result", "CA2 Result", "Average Grade"))
        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15} {5:<15}".format(self.studentID, self.name, self.subject, self.ca1Result, self.ca2result, self.averageCAResult))


# Create a class instance
myStudent = Student()

        # Assign attribute values to the class instance
myStudent.studentID = "X00152190"
myStudent.name = "Ronan Breen"
myStudent.subject = "OO SDP"
myStudent.ca1Result = 70 # made int
myStudent.ca2result = 75 # made int
myStudent.averageCAResult = (myStudent.ca1Result + myStudent.ca2result)/2 # made int

        # Test outputting a class instance, calling the class print definition
myStudent.myStudentPrint()

# Create a Class
class PrintCard:
    accountNumber = "unknown"
    password = "unknown"
    numberOfCredits = "unknown"

    # Create a class definition
    def myPrintPrintCard(self):
        print("\n******* Student Print Card Details *******")
        print("------------------------------------------")
        print("{0:<20} {1:<20}".format("Account Number", "Number of Credits")) # Leave out Password
        print("{0:<20} {1:<20}".format(self.accountNumber, self.numberOfCredits)) # Leave out Password


# Create a class instance
myPrintCard = PrintCard()

    # Assign attribute values to the class instance
myPrintCard.accountNumber = "12345465"
myPrintCard.password = "shdhsdhs"
myPrintCard.numberOfCredits = 10
if myStudent.averageCAResult > 70:
    myPrintCard.numberOfCredits += 400

    # Test outputting a class instance, calling the class print definition
myPrintCard.myPrintPrintCard()
