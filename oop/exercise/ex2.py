# Inheritance
# Exercise 2 Electric Car inheriting from Car

class Car:
    # This is from exercise 1
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
        print(f" -- Mileage: {self.mileage} km.")
# end of class Car

class ElectricCar(Car):
    # Overriding the parent's initialization method to add a new attribute
    def __init__(self, brand, model, year, mileage, battery_capacity):
        # super() targets the first parent class to access attributes and methods
        super().__init__(brand, model, year, mileage)
        self.battery_capacity = battery_capacity
    
    # Overriding the display_info() for battery capacity info
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
        print(f" -- Mileage: {self.mileage} km.")
        print(f" -- Battery Capacity: {self.battery_capacity} kWh")
# end of electric car class

# Using class Car to create a car object
car1 = Car("Honda", "Civic", "2022", 23000)
car1.display_info()

car2 = ElectricCar("Tesla", "S", "2018", 100000, 100)
car2.display_info()