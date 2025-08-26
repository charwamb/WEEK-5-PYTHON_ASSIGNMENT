# Base class
class Animal:
    def move(self):
        raise
NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def move(self):
        print("Dog is running")

class Bird(Animal):
    def move(self):
        print("Bird is flying")

class Fish(Animal):
    def move(self):
        print("Fish is swimming")

# polymorphism in action
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move() # Each behaves differently