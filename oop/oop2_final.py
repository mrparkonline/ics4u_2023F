'''
Goal: Encapsulation & Setter/Getter

Encapsulation --> Hiding Data / information hiding
-- Avoid methods and attributes to be accessed, changed, or even called outside of the class scope

Setter/Getter --> Controlling how programmers access attributes
-- Controlling to attribute behaviour

_varName --> Private
__varName --> Private & Protected
'''
# Member objects will have a name and an account number associated with them
class Member:
    def __init__(self, name, account_number):
        self._name = name
        self.__acc = self.__set_acc(account_number)
    
    # Name Attribute Getter
    @property
    def name(self):
        return self._name
    
    # Name Attribute Setter
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    # Account Number Getter
    @property
    def acc(self):
        return self.__acc
    
    # Account Number Private Setter
    def __set_acc(self, value):
        if isinstance(value, int):
            return value
        else:
            raise ValueError("Improper Data Type for Account Number.")

    def __str__(self):
        return f"{self.acc}: {self.name}"
# end of class Member

member1 = Member("Jasper Park", 2)
#member1.acc = 2
print(member1)