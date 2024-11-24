class Stack:
    def __init__(self):
        self.__storage = []
    
    def push(self, value):
        pass
    
    def pop(self):
        pass
    
    def peek(self):
        pass
    
    def size(self):
        pass
    
    def isEmpty(self):
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        # Completed repr
        return f"<Stack Object @{str(hex(id(self)))}>"
# end of Stack

s = Stack()
print(f"Size of Stack: {s.length}")
print(f"Is the stack empty?: {s.isEmpty()}")
print("-"*32)
print("Pushing Values of: 3, 1, 4, 1, 5, 9 into the stack.")
s.push(3)
s.push(1)
s.push(4)
s.push(1)
s.push(5)
s.push(9)

print(f"Current Stack: {s}") # Testing __str__()
print("-"*32)
a = repr(s)
print(f"Testing __repr__(): {a}")
print("-"*32)

print(f"Last value of the stack: {s.peek()}")
print(f"Is the stack empty?: {s.isEmpty()}")

v = s.pop()
print(f"Testing Pop: {v}")

v2 = []
while not s.isEmpty():
    v2.append(s.pop())

print(f"v2 list: {v2}")
print(f"Is the stack empty?: {s.isEmpty()}")
print(f"Current Stack: {s}")
