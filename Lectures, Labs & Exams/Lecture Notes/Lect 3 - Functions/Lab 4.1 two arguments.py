# Lab 4.1 X00152190

# 1. Create a definition called “print_range” that has two arguments. The definition should print
# all numbers from the first argument up to and including the second argument.
# Test this definition with the values 3, 9 as arguments

def print_range(number1=3, number2=9):
    while number1 < number2: # seems to go in range from above so either number needs to be set as +1 or while loop < instead of <=
        number1 += 1
        print(number1)

print_range()
