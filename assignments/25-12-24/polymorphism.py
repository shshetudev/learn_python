# Polymorphism means "many forms" and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# Example of function polymorphism:
# len() function works on different objects, such as strings, tuples, and dictionaries.

# String example - len() returns the number of characters
x = "Hello World!"
print(len(x))

# Tuple example - len() returns the number of items in the tuple
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

# Dictionary example - len() returns the number of key/value pairs in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))

# Class polymorphism allows multiple classes to have the same method name, but with different behaviors.

# Defining different classes with the same method name "move()"

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

# Creating objects for each class
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Using polymorphism to execute the same method for all three classes
for x in (car1, boat1, plane1):
  x.move()

# Inheritance class polymorphism example:
# Using polymorphism with parent and child classes.

# Creating a parent class "Vehicle"
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

# Creating child classes that inherit from Vehicle and override the move() method
class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

# Creating objects for the child classes
car1 = Car("Ford", "Mustang")  # Car object
boat1 = Boat("Ibiza", "Touring 20")  # Boat object
plane1 = Plane("Boeing", "747")  # Plane object

# Using polymorphism to execute the same method for all classes, while displaying attributes
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

# In this example, the child classes inherit the properties and methods from the parent class.
# The Car class does not override the "move()" method, while Boat and Plane override the move() method.