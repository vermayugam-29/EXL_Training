class Animal:
    def eat(self):
        print("Animal class")

class Dog(Animal):
    def bark(self):
        print("Dog bark")

class Puppy(Dog):
    def play(self):
        print("Puppy play")

puppy = Puppy()
puppy.eat()
puppy.bark()
puppy.play()