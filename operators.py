# OPERATORS
# ================
"""
Here we are going to look at the various operators
used in python programming
"""
# Arithmetic operators
# assign variables an integer numbers
a = 44
b = 32
# a and b are variables assigned to operators 44 and 32
# operands are (+, -, * , /, //, **)
# Multiplication
ans1 = a * b
print(ans1)  # returns 1480

# Addition
ans2 = a + b
print(ans2)  # returns 76

# Subtraction
ans3 = a - b
print(ans3)  # returns 12

# Division
ans4 = a / b
print(ans4)  # returns 1.375

# Modulus
ans5 = a % b
print(ans5)  # returns 12

# Exponentiation
ans6 = a ** b
print(ans6)  # returns 38948043605095874909133313198566681249887133248782336

# Floor Division
ans7 = a // b
print(ans7)  # returns 1

# Relational Operators
# compares two instances and returns True or False
# ===========
a, b = 12, 15
# greater than
a > b  # False
# less than
a < b  # True
# equal to
b == a  # False
# less than or equal to
a <= b  # True
# greater than or equal to
b >= a  # True
# not equal to
a != b  # True

# Logical Operators
#======================
# Use of (and, not, or)
(31 > 21) and (31 < 20) # Both sides True,returns True
(31 == (20 + 11)) or (31 < 34) # returns True

(44 < 31 ) and (41 == 31) # returns False
(44 > 31) or (44 <=31) # returns True

not (44 < 31) # returns True
not (44 > 31) # return False

# Membership operators
#========================
num = 9
num2 = 7
num3 = 7
a = "I LOVE PYTHON LANGUAGE"
list = (4,5,6,7,8,4,2,4,8,9,7)
if num  in list:
    print(True)
elif num3 is not  list: # returns true
    print(f"the number is {num3}") # returns num3 (7)
elif a is not list:
    print("NO COMPARISON") # returns the message in print function
else:
    print("INVALID FORMATS") # returns the message in print function




