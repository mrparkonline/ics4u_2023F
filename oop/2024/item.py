# Inventory & Item Class Python

class Item:
    def __init__(self, name, price=None, desc=None, quantity=None):
        self.__name = str(name)
        self.__price = price
        self.__desc = desc
        self.__quantity = quantity
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def desc(self):
        return self.__desc

    @property
    def quantity(self):
        return self.__quantity
    
    
    @price.setter
    def price(self, value):
        try:
            if not isinstance(value, int) and not isinstance(value, float):
                raise ValueError("Value must be a numeric data type")
            self.__price = value
        except ValueError as e:
            print(f"Error: {e}")
    # end of price.setter

    @desc.setter
    def desc(self, text):
        try:
            if not isinstance(text, str) :
                raise ValueError("Description must be a String")
            self.__desc = text
        except ValueError as e:
            print(f"Error: {e}")
        
    @quantity.setter
    def quantity(self, value):
        try:
            if not isinstance(value, int):
                raise ValueError("Value must be an integer")
            self.__quantity = value
        except ValueError as e:
            print(f"Error: {e}")

# end of Item()

product1 = Item("Coca Cola")
print(product1.name)
product1.price = "$20" # raises an error since we tried to set price to $20
print(f"Product: {product1.name}, price: {product1.price}")
