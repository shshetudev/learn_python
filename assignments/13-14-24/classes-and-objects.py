# Python is an object-oriented programming language, and everything in Python is an object with properties and methods.
# A class serves as a blueprint to create objects.

# Create a class using the 'class' keyword
class MyClass:
    x = 5  # Property x is set to 5

# Create an object of MyClass
p1 = MyClass()  # p1 is now an instance of MyClass
print(p1.x)  # Output: 5 (accessing the property x of p1)

# The __init__() function
# The __init__() function is called automatically when a new object is created.
# It is used to initialize object properties.

class Person:
    def __init__(self, name, age):
        self.name = name  # Assign name to the object
        self.age = age    # Assign age to the object

# Create an object of the Person class
p1 = Person("John", 36)
print(p1.name)  # Output: John
print(p1.age)   # Output: 36

# The __str__() function
# This function is used to return a string representation of an object when it is printed.

# Without __str__() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1)  # Output: <__main__.Person object at 0x7f8d3d4e0f10> (default string representation)

# With __str__() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"  # Custom string representation

p1 = Person("John", 36)
print(p1)  # Output: John(36)

# Object Methods
# Objects can have methods (functions that belong to the object)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):  # Method for greeting
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()  # Output: Hello my name is John

# The 'self' Parameter
# 'self' refers to the current instance of the class and is used to access its properties and methods.
# You can name it something other than 'self', but it must be the first parameter in any method.

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):  # Using 'abc' instead of 'self'
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()  # Output: Hello my name is John

# Modify Object Properties
# You can modify properties of objects like this:
p1.age = 40  # Change p1's age to 40

# Delete Object Properties
# You can delete object properties using the 'del' keyword
del p1.age  # Delete the 'age' property of p1

# Delete Objects
# You can delete an entire object using 'del'
del p1  # Delete the p1 object

# The pass Statement
# If a class has no content, you can use 'pass' to avoid errors.
class Person:
    pass  # No content in the class, but no error occurs due to 'pass'