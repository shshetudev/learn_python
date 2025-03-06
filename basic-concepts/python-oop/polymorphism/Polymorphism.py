# Polymorphism: Poly = Many, Morph = Forms

# Animal class is called super class/Parent class here
class Animal:
    def sound(self):
        print("Animal makes sound")

# All of these are subclasses/Child class/Derived class of Animal
class Tiger(Animal):
    def sound(self): # Overriding the sound method
        print("Tiger roars Halum")

class Deer(Animal):
    def sound(self): # Overriding the sound method
        print("Deer sounds Ma Ma")

class Dog(Animal):
    def sound(self): # Overriding the sound method
        print("Dog Barks")

class Cat(Animal):
    def sound(self): # Overriding the sound method
        print("Cat sounds Mew Mew")

class Duck(Animal):
    def sound(self): # Overriding the sound method
        print("Duck sounds Quack Quack")

animal = Animal()
animal.sound()

tiger = Tiger()
tiger.sound()

deer = Deer()
deer.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

duck = Duck()
duck.sound()

# Creating list of animals
# animals = [Tiger(), Deer(), Dog(), Cat(), Duck()] # This is also valid
print("\n")
print("Printing Animal names in list:")
animals = [tiger, deer, dog, cat, duck]
for animal in animals:
    animal.sound()