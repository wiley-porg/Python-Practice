# Blueprint:
class Car:

    wheels = 4      #Class Variable - all objects have this by default

    def __init__(self, size, brand, year, color):
        self.size = size             # Instance Variable: can change for each object
        self.brand = brand           # Instance Variable
        self.year = year             # Instance Variable
        self.color = color           # Instance Variable

car_1 = Car("Large", "Ford", 2021, "Red")
car_2 = Car("Small", "Honda", 2022, "Blue")

# Both cars have the same default "wheels" value
print("Before changes, Car_1 has " + str(car_1.wheels) + " wheels")
print("Before changes, Car_2 has " + str(car_2.wheels) + " wheels")

Car.wheels = 2      # Changing this Class Variable affects both instances
print("After changes, Car_1 has " + str(car_1.wheels) + " wheels")
print("After changes, Car_2 has " + str(car_2.wheels) + " wheels")

