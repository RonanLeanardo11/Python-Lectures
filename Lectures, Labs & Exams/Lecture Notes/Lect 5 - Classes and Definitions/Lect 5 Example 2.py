
# Define class and attributes
class rectangle:
    length = 0
    width = 0
     # Have to define length and width as numbers and not strings so can do calculations

# Define instances of a class
instance1 = rectangle()
instance2 = rectangle()

# Provide values to instance 1
instance1.length = 15.2
instance1.width = 12.4
instance1.area = round(instance1.length * instance1.width,2) # give a variable for area calculations

# Provide values to instance 2
instance2.length = 3.5
instance2.width = 4.6

# Output area
print("Area of instance 1 is {}".format(instance1.area))
print("Area of instance 2 is {}".format(round(instance2.length * instance2.width,2))) # do calculations in the print function here