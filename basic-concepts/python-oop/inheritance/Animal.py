class Animal:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def __private_method(self):  # Private method
        print("This is a private method.")

    def public_method(self):
        print(f"The animal's name is {self.__name}")
        self.__private_method()


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


def display(self):
    self.public_method()


# Creating an instance of Dog
dog = Dog("Buddy", "Golden Retriever")
dog.display()