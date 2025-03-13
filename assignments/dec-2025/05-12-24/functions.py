# Creating a Function
# A function is defined using the def keyword.
def my_function():
  print("Hello from a function")

# Calling a Function
# To call a function, use its name followed by parentheses.
my_function()

# Arguments
# Arguments are values passed into functions. They are defined inside the parentheses in the function.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameters vs Arguments
# - **Parameter**: A variable in the function definition.
# - **Argument**: A value passed to the function when called.

# Number of Arguments
# A function must be called with the correct number of arguments.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")  # Correct

# Arbitrary Arguments (*args)
# Use * to allow the function to take any number of arguments.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
# Arguments can be passed with the key=value syntax. This allows passing arguments in any order.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments (**kwargs)
# Use ** to pass a variable number of keyword arguments, which are stored as a dictionary.
# * asterik = List, ** asterik = Dictionary
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
# Set default values for parameters. If the function is called without arguments, the default is used.
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function()  # Uses default value "Norway"

# Passing a List as an Argument
# You can pass any data type to a function (e.g., lists, numbers, strings).
print("Printing my_funciton():")
def my_function(food):
  for x in food:
    print(x)

# fruits = ["apple", "banana", "cherry"]
fruits = "apple"
# fruits = {"furit1": "apple", "f2": "banana", "f3":"cherry"}
my_function(fruits)

# Return Values
# Use return to give a result from the function.
def my_function(x):
  return 5 * x

print(my_function(3))  # Outputs 15

# The pass Statement
# Use pass when you need to define a function but don't want to write its code yet.
def my_function():
  pass

# Positional-Only Arguments
# Add / to specify that arguments before it are positional-only.
print("Positional-Only Arguments:")
def my_function(x, /):
  print(x)

my_function(3)  # Correct

# Keyword-Only Arguments
# Add * to specify that arguments after it are keyword-only.
print("Keyword-Only Arguments:")
def my_function(*, x):
  print(x)

my_function(x = 3)  # Correct

# Combine Positional-Only and Keyword-Only Arguments
# You can mix both types in the same function.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# Recursion
# A function can call itself, which is known as recursion. It’s used to solve problems where the solution depends on solving smaller instances of the same problem.
print("Recursion:") #nested way: add(1, add(1, add(1, add(1,2))))
def tri_recursion(k):
  if k > 0:
    # Explanation: Recursion -> Stack memory: LIFO, Iteration[for/while/do..while] -> Heap memory: FIFO
    # 1st Iter: tri_recursion(6): 6 + tri_recursion(5) -> tri_recursion(6): 6 + 15 = 21
    # 2nd Iter: tri_recursion(5): 5 + tri_recursion(4) -> tri_recursion(5): 5 + 10 = 15
    # 3rd Iter: tri_recursion(4): 4 + tri_recursion(3) -> tri_recursion(4): 4 + 6 = 10
    # 4th Iter: tri_recursion(3): 3 + tri_recursion(2) -> tri_recursion(3): 3 + 3 = 6
    # 5th Iter: tri_recursion(2): 2 + tri_recursion(1) -> tri_recursion(2): 2 + 1 = 3
    # 6th Iter: tri_recursion(1): 1 + tri_recursion(0) [END] -> tri_recursion(1): 1
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

tri_recursion(6)


def add(a, b):
  return a + b

sum = add(1, add(1, add(1, add(1,2)))) 
print(sum) 