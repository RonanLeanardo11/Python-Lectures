class Result:
    moduleName = ""
    Grade = 0


    def __init__(self, Mod_Name="", Grade=0):
        self.moduleName = Mod_Name
        self.grade = Grade

    def print(self):
        print("Module Name: ".format(self.moduleName))
        print("Grade Name: ".format(self.grade))


class Student:
    name = ""
    XNumber = "X"
    StudentResults = []

    def __init__(self, name_in, X_in, Results_in):
        self.name = name_in
        self.XNumber = X_in
        self.StudentResults = Results_in

    def add_result(self, grade):
        self.grade = grade
        self.StudentResults.append(self.grade)

    def print(self):
        Result.print(self)
        print("Student Name: ".format(self.name))
        print("X Number: ".format(self.XNumber))
        print("Results: ".format(self.StudentResults))


# In your main program body:
#  Create a Student with appropriate arguments.
Student1 = Student("Ronan", "X00152190", 80)

#  Add three results (with arguments of your choice)
Result1 = Result("KComp", 40)
Result2 = Result("BComp", 50)
Result3 = Result("FComp", 60)

#  Print the Students details
Student1.print()