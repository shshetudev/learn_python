# Class definition for Dog
class Dog:
    species = "Canine"  # Class attribute shared by all instances

    def __init__(self, name, age):
        # Instance attributes that are unique to each Dog object
        self.name = name
        self.age = age

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Accessing instance and class attributes
print(dog1.name)  # Prints: Buddy
print(dog1.species)  # Prints: Canine (Class attribute)
print(dog2.name)  # Prints: Charlie
print(dog2.species)  # Prints: Canine

# Demonstrating that class variables can be modified for all objects
Dog.species = "Feline"
print(dog1.species)  # Prints: Feline (Updated class attribute)
print(dog2.species)  # Prints: Feline (Updated class attribute)

# Demonstrating inheritance with a child class (Labrador)
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")

# Creating an object of the Labrador class
lab = Labrador("Max", 4)
lab.sound()  # Prints: Labrador woofs
print(lab.name)  # Prints: Max (Inherited from Dog class)

# Demonstrating encapsulation with private attributes
class DogWithEncapsulation:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute (accessible, but discouraged)
        self.__age = age  # Private attribute (name mangled)

    def get_info(self):
        # Public method to access private attributes safely
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    def set_age(self, age):
        # Setter to modify private attribute __age
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Creating an object and using encapsulated methods
dog = DogWithEncapsulation("Buddy", "Labrador", 3)
print(dog.get_info())  # Accesses all attributes, including the private __age
dog.set_age(5)  # Sets the new age
print(dog.get_info())  # Updated age

# Example of polymorphism with method overriding
class Dog:
    def sound(self):
        print("Generic dog sound")

class Beagle(Dog):
    def sound(self):
        print("Beagle barks")

class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")

# Run-time polymorphism
dogs = [Dog(), Beagle(), Labrador()]
for dog in dogs:
    dog.sound()  # Each object calls its own version of sound()