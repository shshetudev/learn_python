# Exception Handling in Python

# The try block lets you test a block of code for errors
try:
    print(x)  # This will raise an error since x is not defined
except:
    print("An exception occurred")  # The except block handles the error

# Without try block, the program will crash and raise an error
# print(x)  # Uncomment this line to see the error in action

# You can define multiple exception blocks for specific error types
try:
    print(x)  # This raises a NameError because x is not defined
except NameError:
    print("Variable x is not defined")  # Handle NameError specifically
except:
    print("Something else went wrong")  # Handle other errors

# Use the else block to execute code if no error occurred
try:
    print("Hello")  # This will not raise an error
except:
    print("Something went wrong")  # Will not be executed
else:
    print("Nothing went wrong")  # This will be executed because no error occurred

# The finally block is always executed regardless of error
try:
    print(x)  # This raises an error
except:
    print("Something went wrong")  # Error is caught here
finally:
    print("The 'try except' is finished")  # This is always executed

# Example with file handling
try:
    f = open("demofile.txt")  # Try to open a file
    try:
        f.write("Lorum Ipsum")  # Try to write to the file
    except:
        print("Something went wrong when writing to the file")  # Handle write error
    finally:
        f.close()  # Ensure file is closed, even if an error occurs
except:
    print("Something went wrong when opening the file")  # Handle file open error

# Raising exceptions manually using 'raise'
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")  # Raise an exception if x is negative

# Raising a TypeError manually
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")  # Raise a TypeError if x is not an integer