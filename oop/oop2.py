'''
Goal: Encapsulation & Setter/Getter

Encapsulation --> Hiding Data / information hiding
-- Avoid methods and attributes to be accessed, changed, or even called outside of the class scope

Setter/Getter --> Controlling how programmers access attributes
-- Controlling to attribute behaviour

'''
# Member objects will have a name and an account number associated with them
class Member:
    def __init__(self, name, account_number):
        self._name = name
        self.__acc = self.__set_acc(account_number) # Encapsultion! hid this attribute
    
    # Name getter
    @property
    def name(self):
        return self._name

    # Name setter
    @name.setter
    def name(self, assigned_value):
        self._name = assigned_value.lower().replace(" ", '')

    @property # Getter for acc attribute
    def acc(self):
        return self.__acc

    def __set_acc(self, value):
        if isinstance(value, int):
            return value
        else:
            raise ValueError(f"{value} is not an integer.")

    def __str__(self):
        return f"{self.acc}: {self.name}"
# end of class Member

member1 = Member("Jasper Park", 1)
member1.name = "M r . park"
print(member1)
print(member1.acc)