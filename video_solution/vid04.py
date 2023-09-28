"""
You are to create a program that determines how many paint cans we'd need.

Each plank of the fence requires one paint can.

Your supplier only sells paint cans by the dozen (12) for $14.95. 

There are 3 fenced sections, and their length will be denoted by a series of 'F' for each fence plank.

Output how many cans you'd need, how many paint cans you have leftover, and how much it would cost.

Sample Input:
FF
FFFF
FFFFFF

Sample Output:
12
0
14.95
"""
# import statement
from math import ceil

# input
section1 = input("Enter section 1: ")
section2 = input("Enter section 2: ")
section3 = input("Enter section 3: ")

# processing
cans = len(section1) + len(section2) + len(section3)

boxes = ceil(cans / 12)
leftover = 12*boxes - cans

total_cost = 14.95 * boxes

# output
print(f"We needed {cans} paint cans.")
print(f"We have {leftover} leftover.")
print(f"The project costs ${total_cost}.")