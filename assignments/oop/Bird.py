class Bird:
    species = "Parrot"

    def __init__(self, color, beak):
        self.color = color
        self.beak = beak

    def fly(self):
        print("This bird is flying! it is {self.color} color and it's beak is {self.beak}. It is a {self.species} bird")