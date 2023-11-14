# CCC '00 S4 - Golf

# imports
from math import inf

# Input Handling
distance = int(input())
c = int(input())
clubs = []

for _ in range(c):
    clubs.append(int(input()))
# End of Input Handling

# Memoization table initialization
memo_table = [0] + [inf for _ in range(1, distance+1)]

# Calculate minimum stroke to reach all possible distances
for i, stroke in enumerate(memo_table):
    if i == 0:
        for club in clubs:
            memo_table[club] = 1
    elif stroke != inf:
        new_stroke = stroke + 1
        for club in clubs:
            if i + club <= distance:
                memo_table[i+club] = min(memo_table[i+club], new_stroke)
# end of memo_table setup

if memo_table[-1] == inf:
    print("Roberta acknowledges defeat.")
else:
    print(f"Roberta wins in {memo_table[-1]} strokes.")
