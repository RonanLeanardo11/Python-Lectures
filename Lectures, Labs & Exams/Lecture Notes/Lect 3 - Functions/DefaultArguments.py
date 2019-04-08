# # Default Arguments
#
# #1
# # def print_my_age(age=None):
# #     if age == None:
# #         print("You are too old to say!")
# #     else:
# #         print("Your age is", age)
# #
# # print_my_age()# cant pass argument age in here as undefined, i.e. age=None
#
# #2
# def print_my_age(age=None): # Sets default to none
#     if age == None:
#         print("You are too old to say!")
#     else:
#         print("Your age is", age)
#
# print_my_age() # prints ("You are too old to say!")
# print_my_age(35) print("Your age is", age)

# 3 - assigning a specific value
def print_my_age(age=18):
    print("Your age is", age)
print_my_age() # Your age is 18
print_my_age(35) # Your age is 35


