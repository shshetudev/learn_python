# Scope in programming refers to the region in which a variable is available.
# A variable is only available from inside the region it is created. This is called scope.

# Local Scope:
# A variable created inside a function belongs to the local scope of that function, 
# and can only be used inside that function.

# Example: A variable created inside a function is available inside that function
def myfunc():
  x = 300  # Local variable x inside myfunc
  print(x)

myfunc()  # Prints 300, because x is local to myfunc

# Function Inside Function:
# As explained above, the variable x is not available outside the function, but it is available
# for any function inside the function.

# Example: The local variable can be accessed from a function inside the function
def myfunc():
  x = 300  # Local variable x
  def myinnerfunc():
    print(x)  # Accessing x from the outer function
  myinnerfunc()

myfunc()  # Prints 300, x is available inside myinnerfunc because it is in the same scope

# Global Scope:
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, both global and local.

# Example: A variable created outside of a function is global and can be used by anyone
x = 300  # Global variable x

def myfunc():
  print(x)  # Accessing the global variable x

myfunc()  # Prints 300, accessing global x inside the function

print(x)  # Prints 300, x is accessible globally

# Naming Variables:
# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables - one in the global scope and one in the local scope.

# Example: The function will print the local x, and then the code will print the global x
x = 300  # Global variable

def myfunc():
  x = 200  # Local variable inside myfunc
  print(x)  # This will print the local x

myfunc()  # Prints 200, the local x inside myfunc

print(x)  # Prints 300, the global x, outside the function

# Global Keyword:
# If you need to create a global variable but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.

# Example: Using the global keyword makes the variable global
def myfunc():
  global x  # Declaring x as global inside the function
  x = 300  # This x now belongs to the global scope

myfunc()  # After this, x is created as a global variable

print(x)  # Prints 300, x is now global

# Example: Changing a global variable inside a function using the global keyword
x = 300  # Global variable

def myfunc():
  global x  # Referring to global x inside the function
  x = 200  # Modifying the global x

myfunc()  # Now x is modified inside the function

print(x)  # Prints 200, the modified global x

# Nonlocal Keyword:
# The nonlocal keyword is used to work with variables inside nested functions.
# It allows modifying a variable from the outer function in a nested function.

# Example: Using nonlocal to modify a variable in the outer function
def myfunc1():
  x = "Jane"  # Local variable x in the outer function
  def myfunc2():
    nonlocal x  # Referring to x from the outer function
    x = "hello"  # Modifying x in the outer function
  myfunc2()  # Calling the inner function
  return x  # Returning the modified x

print(myfunc1())  # Prints 'hello', the modified x from the outer function
