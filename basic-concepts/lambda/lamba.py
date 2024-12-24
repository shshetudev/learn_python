# A lamba function is a small anonymous function which take any number of arguments but can only have one expression.

# General function
def add(a,b):
    return a + b # function body

print(add(5, 10))

# Lambda function Syntax -> lambda arguments : expression
x = lambda a, b : a + b 
print(x(5, 10))
