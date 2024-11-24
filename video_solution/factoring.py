# Simple Factoring Program
# Purpose: Find the factors of a number
import math

# 1. Grab an integer from the terminal by user input --> call this num
num = int(input("Enter a positive number: "))

# 2. Find a way to analyze numbers from 1 to num. 
# If any number from 1 to num can evenly divide num, then it is a factor

# a for loop (moreover a for each loop) generates a named temporary variable (in this case x)
# x will represent each number in our sequence 1 by 1 until the end of the sequence
# this ends up creating a loop because we execute our code within our for loop per each representation
#   for x
#for x in range(1, num+1): # range() generates a sequence of integers into our system memory
# stop = int(math.sqrt(num)) + 1 # alternative way
stop = int(num ** 0.5) + 1
for x in range(1, stop):
    # range(1, 10) --> 1,2,3,4,5,6,7,8,9
    # print(f"x is now: {x}")
    # print("I am looping still!")

    if num % x == 0:
        # any two numbers are evenly divisible if their remainder after their division is 0.
        print(f"{x} is a factor of {num}.")
        other = num / x
        print(f"{other} is also a factor of {num}.")

# end of for loop
#print("I am done looping.")

# Final Goal: Make it fast.