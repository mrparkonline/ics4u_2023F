# CCC '04 J1 - Squares

"""
Gigi likes to play with squares. She has a collection of equal-sized square tiles. Gigi wants to arrange some or all of her tiles on a table to form a solid square. 

What is the side length of the largest possible square that Gigi can build?
For example, when Gigi has 9 tiles she can use them all to build a square whose side length is 3.

But when she has only 8 tiles, the largest square that she can build has side length 2.

Write a program that inputs the number of tiles and then prints out the maximum side length. 

You may assume that the number of tiles is less than ten thousand.
"""

# Note: 
# When optimizing the side length of a square, we can square root the tiles to get the best side length

# import statements
from math import sqrt, floor

# input
tiles = int(input()) # int() is a type casting function that converts its argument to integer

# processing

# answer = tiles ** 0.5
# answer = floor(sqrt(tiles))
answer = sqrt(tiles)
answer = floor(answer)

# output
print(f"The largest square had a side length {answer}.")