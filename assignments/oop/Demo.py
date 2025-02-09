# Creating objects (instances) of the Dog class
from assignments.oop.Dog import Dog

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Accessing instance and class attributes
print(dog1.name)  # Prints: Buddy
print(dog1.species)  # Prints: Canine (Class attribute)
print(dog2.name)  # Prints: Charlie
print(dog2.species)  # Prints: Canine

# Demonstrating that class variables can be modified for all objects
Dog.species = "Hello"
Dog.species = "Feline"

print(dog1.species)  # Prints: Feline (Updated class attribute)
print(dog2.species)  # Prints: Feline (Updated class attribute)