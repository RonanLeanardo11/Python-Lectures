
# Define class and attributes
class car:
    make = "Unknown"
    model = "Unknown"
    engineCC = 1.2

# "Objects" or "Instances" of a class
Mercedes = car()  # assign Mercedes object to car class
BMW = car() # assign BMW object to car class
Audi = car() # assign Audi object to car class

print(car) # prints <class '__main__.Car’>
print(Mercedes) # prints <__main__.Car object at 0x029636D0>
print(BMW) # prints <__main__.Car object at 0x029636D0>
print(Audi) # prints <__main__.Car object at 0x029636D0>

print("\n-------------------\n")

print(Mercedes.make) # prints make from class above i.e. Unknown
print(Mercedes.model) # prints model from class above i.e. Unknown
print(Mercedes.engineCC) # prints engine size from class above i.e 1.2

print("\n-------------------\n")

Mercedes.make = "Mercedes" # assign new values to the object
Mercedes.model = "C-Class" # assign new values to the object
Mercedes.engineCC = 3.0 # assign new values to the object
print(Mercedes.make) # prints newly assigned make value
print(Mercedes.model) # prints newly assigned model value
print(Mercedes.engineCC) # prints newly assigned engine CC value