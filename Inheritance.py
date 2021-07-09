# Inheritance:
# Classes can "inherit" attributes and methods from other classes

class Animal:
    alive = True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")


##      SUB/"INHERITOR" CLASSES         ##

class Rabbit(Animal):  # Rabbit will now "inherit" all of the METHODS (functions) of the "Animal" Class!!!!
    def run(self):
        print("Rabbit is running")      # but can still add its own methods too
    pass

class Fish(Animal):         # Fish has both the main methods, but also its own:
    def swim(self):
        print("Fish is swimming")
    pass

class Bird(Animal):
    def fly(self):
        print("Bird is flying")
    pass


rabbit = Rabbit()
fish = Fish()
bird = Bird()

# Can still use the original class functions:
print(rabbit.alive)
fish.eat()
bird.sleep()

# As well as their own individual functions:
rabbit.run()
fish.swim()
bird.fly()









