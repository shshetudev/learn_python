# Polymorphism: Poly = Many, Morph = Forms

# Assigning "Bird" as the Parent class
class Bird:
    def fly(self):
        print("Birds fly at different altitudes!")
    def eat(self): # Overriding the eat method
        print("Birds eat multiple kinds of food!")

# Creating sub-classes of the "Bird" Parent class with Inheritance where the sub classes inherit the "fly" and "eat" method.
class Crow(Bird):
    def fly(self): # Overriding the fly method
        print("Crows fly at a medium-high altitude.")
    def eat(self): # Overriding the eat method
        print("Crows have a very diverse diet, they usually eat nits, fruits, and other protein rich foods.")

class Parrot(Bird):
    def fly(self): # Overriding the fly method
        print("Parrots fly at a medium altitude.")
    def eat(self): # Overriding the eat method
        print("Wild Parrots usually eat seeds, fruits, vegetables, and insects. Domestic parrots on the other hand, usually eat pellets with certain nutrients and protein.")

class Robin(Bird):
    def fly(self): # Overriding the fly method
        print("Robins fly at a medium altitude.")
    def eat(self): # Overriding the eat method
        print("Robins usually have a basic diets of insects (especially beatles) and worms.")

class Quail(Bird):
    def fly(self): # Overriding the fly method
        print("Quails fly at a low altitude.")
    def eat(self): # Overriding the eat method
        print("Quails usually have a plant based diet, eating greens, leafs, and seeds. They can also have an animal based diet of insects such as beetles and ants.")

class Magpie(Bird):
    def fly(self): # Overriding the fly method
        print("Magpies fly at a low altitude.")
    def eat(self): # Overriding the eat method
        print("Magpie usually have insect based diets, eating beetles, flies, caterpillars, spiders, worms, grasshoppers, and more.")

bird = Bird()
bird.fly()
bird.eat()

crow = Crow()
crow.fly()
crow.eat()

parrot = Parrot()
parrot.fly()
parrot.eat()

robin = Robin()
robin.fly()
robin.eat()

quail = Quail()
quail.fly()
quail.eat()

magpie = Magpie()
magpie.fly()
magpie.eat()

# Applying Polymorphism
print("\n") # Printing a new line
print("Printing Bird variant names and functions (Fly, Eat)") # Making a list of Bird variants
birds = [bird, crow, parrot, robin, quail, magpie]
for bird in birds:
    bird.fly()
for bird in birds:
    bird.eat()