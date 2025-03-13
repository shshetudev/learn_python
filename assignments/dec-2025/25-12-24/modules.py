# What is a Module?
# A module is a file containing a set of functions and variables you want to include in your application.
# Consider a module as the same as a code library.

# Create a Module:
# To create a module, simply save the code you want in a file with the .py extension.

# Example: Create a simple module named mymodule.py with a greeting function:
def greeting(name):
  print("Hello, " + name)

# Use a Module:
# Now we can use the module we just created by using the import statement.

# Example: Import the module named mymodule, and call the greeting function:
import mymodule  # Import the module

mymodule.greeting("Jonathan")  # Call the greeting function from the mymodule

# Note: When using a function from a module, use the syntax: module_name.function_name.

# Variables in Module:
# A module can contain not only functions but also variables of all types (arrays, dictionaries, objects, etc.).

# Example: Save a dictionary in the module file mymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Example: Import the module and access the person1 dictionary:
import mymodule  # Import the module

a = mymodule.person1["age"]  # Access the "age" key in the dictionary
print(a)  # Print the age from the dictionary

# Naming a Module:
# You can name the module file whatever you like, but it must have the .py extension.

