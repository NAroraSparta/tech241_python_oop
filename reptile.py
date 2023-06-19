# Showcasing Inheritance

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()      # Initialises the parent/base class - inherit everything from Animal
        self.cold_blooded = True
        self.tetrapod = None   # Not all reptiles have 4 legs
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None    # Not true for all reptiles

    def seek_heat(self):
        print(("it's chilly outside, I need a sunbed"))

    def hunt(self):
        print("Hunting Prey")

    def use_venom(self):
        print("If I have it, may as well use it")

    def attract_mate_yhrough_scent(self):
        print("Time to put on the aftershave")

bulbasaur = Reptile()

# bulbasaur.hunt()        # Reptile method
# bulbasaur.breathe()     # Animal method