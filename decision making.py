
"""
INTRODUCTION TO DECISION MAKING IN PYTHON
------------------------------------------------------>
SUBMITTED TO  @MRichardN
################################
Here we are goin to disccus on conditional statements which will include:
    if statement
    if else statements 
    nested if statement 
    if ..elif..else ladder
"""
#IF STATEMENTS
"""
Simple decision making staemnt and decides whiether the condition is executed or not;ie
if condition is true block is executed otherwise it is not;
SYNTAX;
        if <condition>:
        <statement>
<condition> evaluates to a boolean, True or False.
<statement>valid python statement.
"""
#EXAMPLE CODE 1

y = 32
z = 44
if y < z:
    print("real fact")

if y > z:
    print("Incorrect")
#EXAMPLE CODE 2
age = 23
if (age > 34):
    print("You are old enough")
print("Condition out of if")

#IF ELSE STATEMENTS
"""
If statement alone tells us that if the condition is false the 
block of code is not exectued but ig its true th code is
executed.Including the else statement in the code will execute the code even
if  the condition is false 
SYNTAX;
        <statement a>
            ...
        <statement a>
    else:
        <statement b>
If it evaluates to TRUE the staement a is executed but if it evaluates to false,
the second condition is executed.
"""
#EXAMPLE CODE 1

a = 20
b = 32
if a > b:
    print("a is the number to be used")
    print("We choose integer a")
else:
    print("a was mistaken")
    print("Choose b to be the integer number")
print("We are both in if else")
#EXAMPLE CODE 2
num = 40
if (num <= 45):
    print("Use num as the naming number")
else:
    print("Ignore num ")
    print("Use another number")
print("We go by either condition")

#NESTED IF 
"""
This is simply and if statement inside another if statement
python supports such code execution.
SYNTAX;
if (condition a):
   <first statement>
   if (condition b): 
      <second statement>
   # if Block a ends here
else:
    <third statement>
# if Block y ends here

If condtion a evaluated to TRUE a is executed,if condition b evaluates to TRUE ,b is executed 
if evaluates to FALSE the third staement is executed.

"""
#EXAMPLE CODE 
a = 21
if(a == 21): #FIRST IF STATEMENT
    if a > 31: #NESTED IF STATEMENT 
        print("a is greater than 31") #WILL EXECUTE IF CONDITION IS TRUE
    if a <= 42:
        print("a is in the range to 42")
else:
    print("a is equal to 21 only")


#IF..ELIF..ELSE STATEMENT/LADDER
"""
Here, we can decide among multiple Conditions. If a certain <condition a> is True,
then the corresponding <statement a1> is executed, if False, 
it is skipped and the next condition to be cheked.
If none of the conditions is true, then
the final else statement will be executed.
SYNTAX;
    if (condition):
        statement
    elif (condition):
        statement
    ...
    else:
        statement
Statements are executed form top to down.As long as conditions are true execution 
continues and if it is false the statement is skipped.If all conditions are false then
 the last statement is executed
"""
#EXAMPLE CODE
sum1 = 34
sum2 = 44
if sum1 > sum2:
    print("Consider sum1 as first priority")
elif sum1 == sum2:
    print("Consider both sum1 and sum2")
elif sum2 > sum1:
    print("Consider sum2 as first priority") 
else:
    print("Both sum1 and sum2 are not conisdered")
print("End of execution process")
