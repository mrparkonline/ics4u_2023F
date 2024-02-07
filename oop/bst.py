# Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, value=None):
        if value is None:
            self.root = None
        else:
            self.root = Node(value)
    
    @property
    def size(self):
        return len(self.toList())

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            prev = None
            current = self.root

            while current is not None:
                prev = current
                if current.value > value:
                    current = current.left
                elif current.value < value:
                    current = current.right
                else:
                    return value
            
            if prev.value > value:
                prev.left = Node(value)
            else:
                prev.right = Node(value)

            return value
    # end of add()
    
    def __contains__(self, value):
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False
    
    @property
    def minimum(self):
        if self.root is None:
            return None
        else:
            current = self.root
            if current.left is None:
                return current.value
            else:
                while current.left is not None:
                    current = current.left
                return current.value
    
    @property
    def maximum(self):
        if self.root is None:
            return None
        else:
            current = self.root
            if current.right is None:
                return current.value
            else:
                while current.right is not None:
                    current = current.right
                return current.value
    
    def toList(self):
        def helper(current_node):
            if current_node is None:
                return []
            else:
                return helper(current_node.left) + [current_node.value] + helper(current_node.right)
        
        return helper(self.root)

test = BST()
test.add(10)
test.add(5)
test.add(15)
test.add(6)
test.add(13)
test.add(16)
print(test.toList())
print(13 in test)
print(7 not in test)

print(test.minimum)
print(test.maximum)
print(test.size)