class Person:
    name = ""
    __age = 0

    def __init__(self, name_in, age_in):
        self.name = name_in
        self.__age = age_in
    def print_details(self):
        print("Name :", self.name)
        print("Age :", self.__age)

karen = Person("Karen Nolan", 21)
karen.name = "Ms. Karen Nolan"
karen.age = 22

karen.print_details() # Will print 21 as the variable __age is private