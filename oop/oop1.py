# Dogs & Cats

class Dog:
    # We can set attributes in a initialization method
    # Attributes are data associated with an object
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    # Methods are actionable code/item that an object can execute
    def bark(self):
        print("Bark!")
    
    def sniff(self, object):
        if object.name:
            print(f"{self.name} is curious about {object.name}")
        else:
            print(f"{self.name} is curious about {object}")
# end of class Dog

class Cat:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def meow(self):
        print("Meow.")

    # to make objects printable we must override two base functions:
    # 1. __str__() --> print(), str()
    # 2. __repr__() --> our custom obj having a printable representation inside other objects

    def __str__(self):
        # this needs to return a string
        return f"{self.breed} named {self.name}."
    
    def __repr__(self):
        return f"Cat(name={self.name}, breed={self.breed}, age={self.age})"

# Main portion of our code using our classes to create objects

dog1 = Dog("Marshall", "Westie", 3) # this is a instance of our Dog class; dog1 is a Dog object
print(f"{dog1.name} is a {dog1.breed}")
dog1.bark()
cat1 = Cat("Garfield", "Tabby", 10)
print(f"{cat1.name} is a {cat1.breed}")
cat1.meow()
dog1.sniff(cat1)

text = str(cat1)
print(text)
print(repr(cat1))