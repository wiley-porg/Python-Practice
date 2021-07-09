# multiple inheritance = when a child class is derived from more than one parent class


class Prey:

    def flee(self):
        print("Animal fleeing")



class Predator:

    def hunt(self):
        print("Animal is hunting")



class Rabbit(Prey):     # inherits from Prey Class
    pass

class Hawk(Predator):     # inherits from Predator Class
    pass

class Fish(Prey, Predator):     # inherits from BOTH CLASSES
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# hawk.hunt()               #inherit from one class
# Rabbit.flee()
fish.flee()
fish.hunt()                 #fish can inherit from multiple classes


















