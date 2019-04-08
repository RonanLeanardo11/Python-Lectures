# Lab 5.1 Ronan Breen X00152190

# 1. Create a class called Student with the following attributes:
# studentId
# name
# subject
# ca1Result
# ca2result
# Create a print definition in the student class to print the attributes
# Test the class, by creating one instance of the Student class. Set all attribute values and then
# using the class print definition, print out the students details.


# Create Class
class Student:
    studentID = "unknown"
    name = "unknown"
    subject = "unknown"
    ca1Result = "unknown"
    ca2result = "unknown"

    # Create Class print Definition
    def myStudentPrint(self):
        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}".format("Student ID", "Name", "Subject", "CA1 Result", "CA2 Result"))
        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}".format(self.studentID, self.name, self.subject, self.ca1Result, self.ca2result))








