
# 1. __init__(self):
    # Used to call a initialiser in a class. Purpose is Create instance variables and not class variables
# class Robot:
#     numberOfLegs = 2
#
#     def __init__(self):
#         print("I am alive")
#
# johnny5 = Robot() # When this instance calls the class the initialiser gets called and prints ("I am alive")

# 2. Objects init variables
# class Robot:
#     numberOfLegs = 0
#
#     def __init__(self):
#         self.numberOfLegs = 9
#         print("init variables {}".format(self.numberOfLegs)) #- alternative way have print in the definition
#
# johnny5 = Robot()
#print(johnny5.numberOfLegs)


# 3. Objects init instance variables
# class Robot:
#
#     def __init__(self):
#         self.numberOfLegs = 9
#
# johnny5 = Robot()
# print("instance variables {}".format(johnny5.numberOfLegs))


# 4. Objects init arguments
# class Robot:
#     numberOfLegs = 0
#     name = ""
#
#     # Definition
#     def __init__(self, name_in, number_of_legs_in): # Must pass in Arguments as per line 49.
#         self.name = name_in
#         self.numberOfLegs = number_of_legs_in
#                 # output in definition
#         print("Number of legs = {}".format(self.numberOfLegs))
#         print("Name is {}".format(self.name))
#
#
#     # create instance of a variable
# johnny5 = Robot("Asimo", 2) # pass in two arguments for name_in, number_of_legs_in
#  #or alternatively write as
# #johnny5 = Robot(name_in="Asimo", number_of_legs_in=2) # pass in two arguments for name_in, number_of_legs_in
#         #output globally
# # print(johnny5.numberOfLegs)
# # print(johnny5.name)


# 5. Objects init Default Arguments
class Robot:
    numberOfLegs = 0
    name = ""

    def __init__(self, name_in=None, number_of_legs_in=None):
        if name_in is not None:
            self.name = name_in
        else:
            self.name = "Not Set"
        if number_of_legs_in is not None:
            if number_of_legs_in < 0:
                self.numberOfLegs = "Invalid number"
            else:
                self.numberOfLegs = number_of_legs_in
        else:
            self.numberOfLegs = 0
        print(self.name)
        print(self.numberOfLegs)

#Robot() # Outputs "Not Set" and "0"
#Robot("Ronan", 3) # Outputs "Ronan" and "3"

# Or taking inputs
nameR = input("Please enter your name: ")
numberLegsR = int(input("Please enter legs: "))

Robot(nameR,numberLegsR)