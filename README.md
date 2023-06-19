#Python Object Oriented Programming (OOP)

```python
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
```
```python
Classes

Classes are used to create user-defined data structures. Classes define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.
A class is a blueprint for how something should be defined. It doesn’t actually contain any data.

How to Define a Class
All class definitions start with the class keyword, which is followed by the name of the class and a colon. 

.__init__() sets the initial state of the object by assigning the values of the object’s properties. That is, .__init__() initializes each new instance of the class.

Creating a new object from a class is called instantiating an object. 
```
```python


Four pillars in OOPS

There are four pillars:

1. Encapsulation: To enclose something in or as if in a capsule.
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
Animal.breathe(Animal)   # One breatha at a time, in and out
cat.breathe()           # One breatha at a time, in and out


#2######## Showcasing Encapsulation (Really good for protecting important variables/objects###############

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
```
```python

2. Inheritance: To receive a quality, characteristic, etc., from your parents or family. Inheritance allows us to define a class that inherits methods and properties from another class. Let’s say you need a new class with little or no modification, and you then apply this concept.

The base class is called the parent class, and the derived class is known as a child.

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

```
```python

3. Polymorphism: The condition of occurrence in several different forms.  In programming terms, polymorphism refers to the use of a single method/operator to represent different types in different scenarios.

from snake import Snake

    class Python(Snake):

        def __init__(self):
            super().__init__()
            self.large = True
            self.two_lungs = True
            self.venom = False

        def digest_large_prey(self):
            print("ok, hand me the stretchy pants")

        def constrict(self):
            print("and...squeeeeeze")

        def climb(self):
            print("up we go")

        def shed_skin(self):
            print("I'm growing out of this now")

        def breathe(self):
            print("I am breathing but I am a Python!")

peter = Python()

peter.breathe()
peter.eat()
peter.hunt()
peter.use_tongue_to_smell()
peter._show_seek_heat()

```
```python

4. Abstraction: Abstraction hides the internal implementations of a process or method from the user. In this way, the user knows what they do but not how it is done.

Python comes with a module that fits the base for Abstract Base classes (ABC). A method becomes abstract when decorated with the keyword @abstractmethod.
```





