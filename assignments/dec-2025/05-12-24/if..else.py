# Python supports logical conditions
"""a == b  # Equals: Checks if a is equal to b
a != b  # Not Equals: Checks if a is not equal to b
a < b   # Less than: Checks if a is less than b
a <= b  # Less than or equal to: Checks if a is less than or equal to b
a > b   # Greater than: Checks if a is greater than b
a >= b  # Greater than or equal to: Checks if a is greater than or equal to b
"""
# if statement checks a condition and executes code based on the result
a = 33
b = 200
if b > a:  # If b is greater than a, execute the following block
    print("b is greater than a")

# Indentation is important in Python as it defines the scope of the code blocks
# An error will occur if indentation is not used correctly
# if b > a:
# print("b is greater than a")  # This will raise an error due to lack of indentation

# elif is used to check additional conditions if the previous ones are False
a = 33
b = 33
if b > a:  # First condition: Check if b is greater than a
    print("b is greater than a")
elif a == b:  # elif condition: Check if a is equal to b
    print("a and b are equal")

# else is used to handle all other cases not caught by if or elif
a = 200
b = 33
if b > a:  # First condition: Check if b is greater than a
    print("b is greater than a")
elif a == b:  # elif condition: Check if a is equal to b
    print("a and b are equal")
else:  # Else block will execute if no other conditions are true
    print("a is greater than b")

# You can have an else without using elif
a = 200
b = 33
if b > a:  # Check if b is greater than a
    print("b is greater than a")
else:  # Else will execute if b is not greater than a
    print("b is not greater than a")

# Short Hand If: If only one statement needs to be executed, it can be placed on the same line
if a > b: print("a is greater than b")

# Short Hand If ... Else (Ternary Operator): Executes one of two statements based on a condition
a = 2
b = 330
print("A") if a > b else print("B")  # Print "A" if a is greater than b, otherwise print "B"

# Multiple conditions on one line: Using multiple conditions with short hand if-else
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")  # Print based on multiple comparisons

# Using logical operators
# 'and' checks if both conditions are True
a = 200
b = 33
c = 500
if a > b and c > a:  # Check if a is greater than b and c is greater than a
    print("Both conditions are True")

# 'or' checks if at least one condition is True
if a > b or a > c:  # Check if either a is greater than b, or a is greater than c
    print("At least one of the conditions is True")

# 'not' reverses the condition (checks if a is NOT greater than b)
a = 33
b = 200
if not a > b:  # Check if a is NOT greater than b
    print("a is NOT greater than b")

# Nested If statement: An if statement inside another if statement
x = 41
if x > 10:  # Check if x is greater than 10
    print("Above ten,")
    if x > 20:  # Nested condition: Check if x is also greater than 20
        print("and also above 20!")
    else:  # If x is not greater than 20
        print("but not above 20.")

# The pass statement can be used if an if statement has no content
# It prevents an error from occurring when an if block is empty
a = 33
b = 200
if b > a:  # If b is greater than a, no action taken (pass)
    pass