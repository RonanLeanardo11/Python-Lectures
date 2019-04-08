#  Create a class called Student:
class student:
    # Class Variables - we don't actually need them
    #  name
    #  fees
    name = "Unknown"
    fees = 0

    # Initialiser
    def __init__(self,name_in=None, fees_in=None): # Default arguments for each class variable
        if name_in is not None:
            self.name = name_in # Only set name if its value is not none (no else)
        else:
            self.name = "Not Set"
        if fees_in is not None:
            if fees_in > 0: # If fees are not none and fees are > 0, set the fees to the argument
                self.fees = fees_in
            else:
                self.fees = "50000" #Else set the fees to 50000 (the colleges most expensive course)
        # Methods
        #  printDetails() method that prints all student details
    def print_details(self):
        print("Student name is {}".format(self.name))
        print("Student fees are {}".format(self.fees))


nameInput = input("What is your name: ")
feesInput = int(input("What are the fees: "))
#
myStudent = student(nameInput,feesInput)

myStudent.print_details(self)



