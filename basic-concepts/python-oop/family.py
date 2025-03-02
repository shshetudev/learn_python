class Grandfather:
    def __init__(self, name):
        self.__name = name

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print(f"The family member's name is {self.__name}")
        self.__private_method()

Grandfather = Grandfather("Ashraf", "5'7")
Grandfather.display()

class Father(Grandfather):
    def __init__(self, name, hair):
        super().__init__(name)
        self.hair = hair


def display(self):
    self.public_method()


Father = Father("Abul", "5'6", "Black")
Father.display()

class Shabab(Father):
    def __init__(self, name, eyes):
        super().__init__(name)
        self.eyes = eyes



Shabab = Shabab("Shabab", "5'6", "Black")
Shabab.display()