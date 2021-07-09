# multi-level inheritance means a child(derived) class inherits another child(derived) class



class Organism:

    alive = True


class Animal(Organism):                 # Animal comes from Organism, HAS ALL ORGANISM METHODS (even if it isn't written)

    def eat(self):
        print("Animal is eating")


class Dog(Animal):                      # Dog comes from Animal, which comes from Organism, so STILL HAS ORGANISM METHODS

    def bark(self):
        print("Dog is barking")


dog = Dog()
print("The dog is " + str(dog.alive))       # inherits from Organism
dog.eat()                                   # inherits from Animal
dog.bark()                                  # self-defined function





















