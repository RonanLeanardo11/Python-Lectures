# Define class and attributes
class rectangle:
    length = 0
    width = 0
     # Have to define length and width as numbers and not strings so can do calculations

    def myRecPrint(self):
        print("*********************************")
        print("****** Area of a Rectangle ******")
        print("*********************************")
        print("Length is {}sm".format(self.length))
        print("Width is {}sm".format(self.width))
        print("Area of the Rectangle is {}sm".format(round(self.length * self.width, 2)))  # do calculations in the print function here

myRectangle = rectangle() # Assign class to a variable

myRectangle.length = 15.2
myRectangle.width = 12.4

myRectangle.myRecPrint()
