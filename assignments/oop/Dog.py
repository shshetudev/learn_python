class Dog:
    species = "Canine"  # Class attribute shared by all instances

    # Constructor: First thing to be called when and object is created
    def __init__(self, name, age):
        # Instance attributes that are unique to each Dog object
        self.name = name
        self.age = age

    # Method
    def printDogName(self):
        print(f"This dog's name is {self.name}")