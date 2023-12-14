# Encapsulation
# Hiding/Protecting Mileage

class Car:
    # This is from exercise 1
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = mileage
    
    # Creating a getter
    # 1. apply @property tag
    # 2. create a method that returns the encapsulated attribute
    # now the .mileage is able to accessed by this getter.
    @property
    def mileage(self):
        return self.__mileage
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
        print(f" -- Mileage: {self.mileage} km.") # self.mileage is gettable due to our getter
# end of class Car

# Using class Car to create a car object
car1 = Car("Honda", "Civic", "2022", 23000)
print(f"car1 mileage: {car1.mileage}")
car1.display_info()

# changing the mileage will cause an error
car1.mileage = 200