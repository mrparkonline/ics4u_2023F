# Recursion
# Creating a solution to a problem by relying upon earlier solutions.

# The main concept: 
#   "A problem with input of N may be too large and difficult to solve"
#   "Maybe we can solve a smaller version of the problem when N gets small enough"
#   "We will shrink the problem by calling the function on an argument smaller than N ... called X for example. 
#       If f(x) is solvable, then maybe we can use that to solve f(n)."

# The hardest parts of Recursion
# 1. How to identify when a recursion can be used.
''' Some Problem Classifications:
        Divide and Conquer Problems
        Tree and Graph Structures
        Nested Structures
        Backtracking
        Dynamic Programming
'''
# 2. How to construct a recursive statement

# Given Problem: Add all numbers from 1 to N; where N is a positive integer
''' 
Let N be 5
    f(5) --> 5 + 4 + 3 + 2 + 1
    f(4) --> 4 + 3 + 2 + 1

    therefore, f(5) = 5 + f(4)
    f(4) = 4 + f(3)
    f(3) = 3 + f(2)
    f(2) = 2 + f(1)
    f(1) = 1

    then maybe ... f(N) = N + f(N-1)
'''

# recipes for creating a recursive function
# 1. Create a base case (the simplest versions of the problem which have simple solutions)

# 2. If the given argument for the function is not one of the base case:
#   2a. Design how to work towards one of the base cases
#   2b. Get to the base case by calling the function itself with a smaller 

def r_sum(num):
    # Base Case 1 , num is 0
    if num == 0:
        return 0
    # Base Case 2, num is 1
    elif num == 1:
        return 1
    else:
        return num + r_sum(num-1)
# end of r_sum

print(f"Sum of all numbers from 1 to 10: {r_sum(10)}")