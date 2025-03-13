# A lambda function is a small anonymous function that can take any number of arguments but has only one expression.

# Syntax: lambda arguments: expression

# Example 1: Add 10 to the argument
x = lambda a: a + 10
print(x(5))  # Output: 15

# Example 2: Multiply two arguments
x = lambda a, b: a * b
print(x(5, 6))  # Output: 30

# Example 3: Sum three arguments
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))  # Output: 13

# Why use lambda functions?
# Lambda functions are often used as anonymous functions inside other functions.

# Example 4: Function that multiplies a number with a given multiplier (doubles the number)
def myfunc(n):
    return lambda a: a * n  # Returns a lambda that multiplies 'a' with 'n'

mydoubler = myfunc(2)  # Create a function that doubles the number
print(mydoubler(11))  # Output: 22

# Example 5: Function that triples the number
mytripler = myfunc(3)  # Create a function that triples the number
print(mytripler(11))  # Output: 33

# Example 6: Both functions in the same program
mydoubler = myfunc(2)  # Function to double
mytripler = myfunc(3)  # Function to triple

print(mydoubler(11))  # Output: 22
print(mytripler(11))  # Output: 33