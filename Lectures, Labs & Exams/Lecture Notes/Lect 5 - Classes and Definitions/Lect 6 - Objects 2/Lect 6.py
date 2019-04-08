# 1. Initializers _ _init_ _(self):


# 2.  Class and instance variables


# 3.  Behaviour methods (getters, setters and behaviours)
#  Validation on class and instance variables (using methods and private
# variables)


# 4.  Private class / instance variables
#  Getters and Setters



# 1. Initializers _ _init_ _(self):

    #create a class
class student:
    id = "unknown"
    name = "unknown"
    dob = "unknown"
    address = "unknown"
    grade = "unknown"

    def MyPrintStudent(self):
        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}".format("Student ID", "Name", "DOB", "Address","Grade"))
        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}".format(self.id, self.name, self.dob, self.address,
                                                               self.grade))

    # First - instance of a class
myStudent = student()
myStudent.id = "S01"
myStudent.name = "Ronan Breen"
myStudent.dob = "03-Feb-1988"
myStudent.address = "3 The Gallops"
myStudent.grade = 80

    # Second - instance of a class
myStudent = student()
myStudent.id = "S02"
myStudent.name = "Roger Jones"
myStudent.dob = "24-Feb-1978"
myStudent.address = "3 The Mews"
myStudent.grade = 40

    # call Defintion with class instances
myStudent.MyPrintStudent()

