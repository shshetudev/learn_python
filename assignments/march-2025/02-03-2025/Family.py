class Grandfather:
    def __init__(self, name):
        self.name = name

    def __private_method(self):
        print("This is a private method.")

    def swim(self):
        print(f"{self.name} swims very fast")

grandfather = Grandfather("Ashraf")
grandfather.swim()

class Father(Grandfather):
    def __init__(self, name, hair):
        super().__init__(name)
        self.hair = hair

    def run(self):
        print(f"{self.name} runs very fast")

father = Father("Abul", "Black")
father.swim()
father.run()

class Children(Father):
    def __init__(self, name, hair, eyes):
        super().__init__(name, hair)
        self.eyes = eyes

    def cycle(self):
        print(f"{self.name} cycles very fast")

class NextGenChildren(Children):
    def __init__(self, name, hair, eyes):
        super().__init__(name, hair, eyes)

shababJr = NextGenChildren("ShababJR", "Brown", "Blue")
shababJr.swim()
shababJr.run()
shababJr.cycle()