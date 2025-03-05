class Grandfather:
    def __init__(self, name):
        self.__name = name

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print(f"The family member's name is {self.__name}")
        self.__private_method()

    def display(self):
        self.public_method()

grandfather = Grandfather("Ashraf")
grandfather.display()

class Father(Grandfather):
    def __init__(self, name, hair):
        super().__init__(name)
        self.hair = hair

    def display(self):
        self.public_method()

father = Father("Abul", "Black")
father.display()

class Shabab(Father):
    def __init__(self, name, hair, eyes):
        super().__init__(name, hair)
        self.eyes = eyes

    def display(self):
        self.public_method()

shabab = Shabab("Shabab", "Black", "Brown")
shabab.display()