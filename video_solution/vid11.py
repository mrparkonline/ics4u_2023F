''' Quadrant Selection 2017 Stage 1, Junior #1

A common problem in mathematics is to determine which quadrant a given point lies in. There are four quadrants, numbered from 1 to 4

Your job is to take a point and determine the quadrant it is in. You can assume that neither of the two coordinates will be 0
'''

# input

# original input
# x = int(input())
# y = int(input())

# modified input
point = input() # in a format of: "10 -11"

point = point.split(' ') # we running the .split() from the string object class, and argument is a whitespace
# "10 -11" --> ["10", "-11"]

""" a long form solution to converting a list with numeric strings to list of integers
fixed_point = []
for value in point:
    fixed_point.append(int(value))
"""
point = list(map(int, point)) # --> point is ["10", "-11"] --> iterable(10, -11) --> [10, -11]
print(point)

# variable unpacking.
x, y = point
print(f'x is {x}.')
print(f'y is {y}.')

# quadrant selection
if x > 0:
    #pass # this is a placeholder code in python
    if y > 0:
        print(f'The point of ({x},{y}) is in Quadrant 1.')
    else:
        print(f'The point of ({x},{y}) is in Quadrant 4.')
else:
    if y > 0:
        print(f'The point of ({x},{y}) is in Quadrant 2.')
    else:
        print(f'The point of ({x},{y}) is in Quadrant 3.')