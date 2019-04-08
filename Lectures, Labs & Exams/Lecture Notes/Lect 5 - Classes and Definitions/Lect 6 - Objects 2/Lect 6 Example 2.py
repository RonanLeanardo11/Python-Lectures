#Create a class called MotorBike:
# 1. Class Variables
#  Make
#  currentGear
class motorbike:
    make = "unknown"
    currentGear = 0

    # 2.Initialiser
    #  Default arguments for only the make class variable
    #  Only set make if its value is not none(no else )
    #  Always set currentGear to 0 -> represents neutral
    def __init__(self, make_in=None):
        if make_in is not None:
            self.make = make_in
        else:
            self.make = "Not Defined"
        self.currentGear = 0

    # up_gear()
    # No arguments that increases the MotorBikes gear (there is a maximum of 6
    # gear)
    def up_gear(self):
        if self.currentGear < 6:
            self.currentGear += 1


    # down_gear()
    # No arguments that increases the MotorBikes gear (there is a Minimum of 0 gear)
    def down_gear(self):
        if self.currentGear > 6:
            self.currentGear -= 1

    # Print_details()
    #  method that prints all MotorBikes details
    def myPrint(self):
        print("Make is {} and current gear is {}".format(self.make, self.currentGear))

# Test the class, create an instance and pass in arguments
# mymake = "Honda"
# mycurrentGear = 6
#
# myMotorbike = motorbike(mymake)
#
# myMotorbike.myPrint()

r1 = motorbike("Yamaha")
# r1.myPrint() # will print number i.e if set as 1 in __init__ will print 1
# r1.up_gear() # if number is below 6 will add 1 and print, i.e. if currentGear is 1 will print 2 - in myPrint() below
# r1.down_gear() # if number is above 6 will minus 1 and print, i.e. if currentGear is 7 will print 6 - in myPrint() below
# r1.myPrint() # prints all above if conditions inside met

for i in range(100): # will work where gears less than 6
     r1.up_gear()
     r1.down_gear()
     r1.myPrint()


