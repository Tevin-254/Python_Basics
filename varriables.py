# Variables
"""
This is a program to show some basic variables in
python how they are called and how they are used
in python programming
"""
name = "Abbie" # String
print(name)

weight = 75.76 # floating point number
print(weight)

female = True # boolean

num1 = 2 # Integers
num2 = 4
total = num1+num2 # operations
print(total)

a = 23  # Global variable

print(id(a))  # Prints the id of the variable (a)

def willS():  # defines another function called a

    a = 44  # Local variable,called inside a function

    y = globals()['a']  # Global variable called inside a function using a special command called globals()

    print(id(y)) #prints the id of (y) whic the same as the id of (a) since they arre both global varriables

    print(a) #prints the local varriable


willS()

print(a) #Prints the global varraible,
