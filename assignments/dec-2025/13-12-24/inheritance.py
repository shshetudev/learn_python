# Inheritance allows us to define a class that inherits all methods and properties from another class.
# The parent class is the class being inherited from, and the child class is the class that inherits.

# Create a Parent Class
# The parent class can have properties and methods that the child class will inherit.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname  # Property: first name
        self.lastname = lname    # Property: last name

    def printname(self):
        print(self.firstname, self.lastname)  # Method to print full name

# Create an object of the Person class
x = Person("John", "Doe")
x.printname()  # Output: John Doe

# Create a Child Class
# To create a child class that inherits from the Person class, we pass the parent class as a parameter.

class Student(Person):  # Student inherits from Person
    pass  # The child class does not add any properties or methods, so we use 'pass'

# Create an object of the Student class
x = Student("Mike", "Olsen")
x.printname()  # Output: Mike Olsen (inherited from Person class)

# Add the __init__() function to the Child Class
# If we want to add properties or methods specific to the child class, we use the __init__() function in the child.

class Student(Person):
    def __init__(self, fname, lname, year):
        self.firstname = fname
        self.lastname = lname
        self.graduationyear = year  # Adding a new property for graduation year

# Create an object of the Student class with the new property
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)  # Output: 2019

# Using super() to Call the Parent's __init__() Function
# If we want to keep the inheritance of the parent’s __init__() function, we use super() to call it.

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # Call the parent class's __init__() method
        self.graduationyear = year

# Create an object of the Student class
x = Student("Mike", "Olsen", 2019)
print(x.firstname)  # Output: Mike (inherited from Person class)
print(x.graduationyear)  # Output: 2019

# Add Methods to the Child Class
# You can add methods specific to the child class as well.

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):  # New method specific to the child class
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

# Create an object of the Student class and call the new method
x = Student("Mike", "Olsen", 2019)
x.welcome()  # Output: Welcome Mike Olsen to the class of 2019

# Overriding Methods
# If the child class has a method with the same name as the parent class, the child's method will override the parent's method.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def printname(self):  # Overriding the printname method from the parent class
        print(f"{self.firstname} {self.lastname}, Graduation Year: {self.graduationyear}")

# Create an object of the Student class and call the overridden method
x = Student("Mike", "Olsen", 2019)
x.printname()  # Output: Mike Olsen, Graduation Year: 2019