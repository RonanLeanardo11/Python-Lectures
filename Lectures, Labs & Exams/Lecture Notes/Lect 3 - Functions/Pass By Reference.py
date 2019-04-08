# # Pass By reference
#
# 1
# # Defining outside the Function
# def print_number():
#     print(myNumber)
#
# myNumber = 5 # must be passed in for myNumber +=1 to work
# print_number() #5
#
# myNumber += 1
# print_number() #6

# 2
# Defining inside the Function - will get error as number not defined outside the function
# def print_number():
#     myNumber = 5
#     print(myNumber)
#
# myNumber += 1 #NameError: name 'myNumber' is not defined
# print_number()

# 3
# variables modified in loop don't stay outside the definition
# def print_number(number_in):
#     number_in += 1
#     print("printed in the definition:", number_in) #8
#
# x = 7
# print("printed before definition:", x) #7
# print_number(x)
# print("printed after definition:", x) #7

# # 4 Global and local Variables
# x = 7 # Global Variable
# y = 10
# def print_number():
#     print(x) # Prints Global Variable i.e 7
#     y = 9 # Local Variable
#     print(y) # Prints Local Variable i.e 9
#
# print_number()

# x = 7 # Global Variable
# # # def print_number(x): # Local Variable
# # #     x += 1
# # #     print(x)
# # # print_number(x)  # 8 - local
# # # print(x) # 7 - Global


# 5 Shadow and Deep Copies

# Shadow copy - x and y are seperate to eachother i.e. change one it doesnt change the other
# x = 7
# y = x
# y += 1
# print(x) # 7
# print(y) # 8

# Deep Copy - If we change a list within a loop (Local) it remains that way outside it (Global)
# x = [1, 2, 3]
# y = x
# y[0] = 9
# print(x) # - [9,2,3]
# print(y) # - [9,2,3]

# Deep Copy - If we change a list within a loop (Local) it remains that way outside it (Global)
# myList = [1, 2, 3, 4] # Global Variable
#
# def print_number(myList):
#     myList[3] = 33 # This will change the 4th value inside (Local) and outside (Global) the Function
#     print(myList) # [1, 2, 3, 33]
# print_number(myList)
# print(myList) # [1, 2, 3, 33]

# 6 - More Deep Copies - Avoid a deep copy by ceating a local list
# myList = [1, 2, 3, 4] # Global Variable
# def print_number(myList):
#     myLocalList = myList[:] # Deep copy to local variable. *** Map to a new list so myList is unchanged outside the function
#     print(myLocalList) #[1, 2, 3, 4]
#     myLocalList[0] = 99
#     print(myLocalList) #[99, 2, 3, 4]
#
#
# print_number(myList)
# print(myList)#[1, 2, 3, 4]
# #if try and print local list will get an error
# #print(myLocalList) #NameError: name 'myLocalList' is not defined


# 7 - Return Functions
# We can use returns to send information back to code
# which called the definition.
def volume_of_a_sphere(radius):
    volume = (4.0 / 3.0) * 3.14 * (radius ** 3)
    return volume # can use this outside the function now i.e Globally

volume = volume_of_a_sphere(6371000) # return function i.e. "volume" called here
mass = volume * 5513.5
#print(volume)
print("Mass of earth is:", mass, "KG")