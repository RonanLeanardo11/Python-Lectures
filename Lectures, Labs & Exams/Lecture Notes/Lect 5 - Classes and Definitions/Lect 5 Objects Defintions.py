# Define our Class and objects
class car:
# Attributes first
    make = "unknown"
    model = "unknown"
    engineCC = 0.0

# Definitions - note the indentation
    def my_print(self):
        print("*********************************")
        print("********** Car Details **********")
        print("*********************************")
        print("Car Make :", self.make)
        print("Car Model :", self.model)
        print("Engine Size (cc) :", self.engineCC)

# Assign values to car Class
Mercedes = car()  # assign Mercedes object to car class
BMW = car() # assign BMW object to car class

    # assign valaues to attributes
Mercedes.make = "Mercedes" # assign new values to the object
Mercedes.model = "C-Class" # assign new values to the object
Mercedes.engineCC = 3.0 # assign new values to the object

# Call the my_print definition passing in the Mercedes/BMW instances from car class.
# car.my_print(Mercedes) # outputs Mercedes values in Definition structure above
# car.my_print(BMW) # outputs Mercedes values in Definition structure above

# Alternatively can assign a variable to hold class details - this print the values in the class i.e. unknown, unknown, 0.00cc
myCar = car()
myCar.my_print()

    # To avoid this you can assign values above calling the function
myCar = car()

myCar.make = "Honda"
myCar.model = "Civic Turbo"
myCar.engineCC = 1.4

myCar.my_print()