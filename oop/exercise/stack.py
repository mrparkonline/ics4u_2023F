class Stack:
    def __init__(self):
        self.__storage = []
    
    @property
    def length(self):
        return self.size()
    
    def push(self, value):
        self.__storage.append(value)
    
    def pop(self):
        return self.__storage.pop()
    
    def peek(self):
        return self.__storage[-1]
    
    def size(self):
        return len(self.__storage)
    
    def isEmpty(self):
        return len(self.__storage) == 0
    
    def __str__(self):
        if self.isEmpty():
            return "<>"
        else:
            output = ", ".join(map(str, self.__storage))
            return f"<{output}>"

        # output = '<'
        # for i, data in enumerate(self.__storage):
        #     if i == len(self.__storage)-1:
        #         output += f"{data}>"
        #     else:
        #         output += f"{data}, "
        # return output
    
    def __repr__(self):
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
