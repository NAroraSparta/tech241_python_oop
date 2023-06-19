# Animal class

class Animal:

    def __init__(self):     #when it's made do this thin

        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breatha at a time, in and out")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("Time to find a mate")

    def move(self):
        print("Onwards and upwards")

cat = Animal()
Animal.breathe(Animal)      # One breatha at a time, in and out
cat.breathe()               # One breatha at a time, in and out