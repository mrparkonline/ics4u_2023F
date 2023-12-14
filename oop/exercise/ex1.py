# Simple Class
# Exercise 1 Car Class

class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
        print(f" -- Mileage: {self.mileage} km.")
# end of class Car

# Using class Car to create a car object
car1 = Car("Honda", "Civic", "2022", 23000)
car1.display_info()