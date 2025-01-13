# Built-in Math Functions

# The min() and max() functions can be used to find the lowest or highest value in an iterable:
# Example
x = min(5, 10, 25)  # Finds the smallest value among 5, 10, and 25
y = max(5, 10, 25)  # Finds the largest value among 5, 10, and 25

print(x)  # Output: 5 (smallest number)
print(y)  # Output: 25 (largest number)

# The abs() function returns the absolute (positive) value of the specified number:
# Example
x = abs(-7.25)  # Converts negative number -7.25 to positive 7.25

print(x)  # Output: 7.25

# The pow(x, y) function returns the value of x raised to the power of y (x^y):
# Example
x = pow(4, 3)  # 4 raised to the power of 3, i.e., 4 * 4 * 4 = 64, 4^3 = 64

print(x)  # Output: 64

# The Math Module
# Python has a built-in module called 'math' that extends the list of available mathematical functions.

# To use it, you must import the math module first:
import math

# The math.sqrt() method returns the square root of a number:
# Example
x = math.sqrt(64)  # Calculates the square root of 64

print(x)  # Output: 8.0 (Square root of 64)

# The math.ceil() method rounds a number upwards to its nearest integer:
# The math.floor() method rounds a number downwards to its nearest integer:
# Example
x = math.ceil(1.4)  # Rounds 1.4 upwards to 2
y = math.floor(1.4)  # Rounds 1.4 downwards to 1
z1 = round(1.4)
z2 = round(1.5)

print(x)  # Output: 2
print(y)  # Output: 1
print(z1)
print(z2)

# The math.pi constant returns the value of pi (π), which is approximately 3.14159:
# Example
x = math.pi

print(x)  # Output: 3.141592653589793 (approximation of π)