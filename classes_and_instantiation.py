# Classes

# creating a class - this is like a template

class Dog:

    animal_kind = "canine"      #class variable

    def bark(self): # class function = methods
        return "woof"

print(Dog.animal_kind)
print(Dog.bark(Dog))

#Instantiation of a class

fido = Dog()
lassie = Dog()

print(type(fido))     #<class '__main__.Dog'>
print(type(lassie))     #<class '__main__.Dog'>
print(fido.animal_kind)     #canine
print(lassie.animal_kind)       #canine
print(fido.bark())          #woof
print(lassie.bark())         #woof

# Class variables can be overwritten

fido.animal_kind = "Big Dog"
print(fido.animal_kind)      #Big Dog
print(lassie.animal_kind)      #canine

Dog.animal_kind = "Dolphin"

print(fido.animal_kind)     #Big Dog
print(lassie.animal_kind)   #Dolphin

print(lassie.bark())        #woof
