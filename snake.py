# Showcasing Encapsulation (Really good for protecting important variables/objects

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()      # Initialises the parent/base class - inherit everything from Animal/reptile
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

# Types of modifiers in Python -

# Public - Anyone, anywhere can use it
# Private- Accessible only within the class itself
# Protected - accessible within the class and it's subclasses'

    def use_tongue_to_smell(self):
        print("Do I say it smells nice, or tastes nice...?")

sidney = Snake()

sidney.breathe()  # Animal method
sidney.seek_heat()      #Reptile method
sidney.use_tongue_to_smell()    # Sname method