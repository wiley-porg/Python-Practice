# Blueprint:
class Car:

    def __init__(self, size, brand, year, color):
        self.size = size             # Self simply refers to the instance of the object that you're working on
        self.brand = brand           # So it ends up being like "car_1.model = *model*"
        self.year = year             # Don't need to pass in anything for self argument
        self.color = color


    def drive(self):
        print("This " + self.brand + " is driving")

    def stop(self):
        print("This " + self.brand + " is stopping")



# Example:
car_1 = Car("Large", "Chevy", 2021, "Red")          #create own object by passing in inputs
car_2 = Car("Small", "Ford", 2022, "Blue")


car_1.drive()       #Don't need to pass an argument for "self"
car_1.stop()


car_2.drive()
car_2.stop()









