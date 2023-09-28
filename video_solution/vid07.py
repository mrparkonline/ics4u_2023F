"""Create a program that simulates the ability check from the video game called “Baldur's Gate 3”.

An ability check in Baldur's Gate 3 is determined by first the Difficulty Class (DC). The DC is a number representing how hard a task is. When a player wants to do something uncertain, like jumping a gap or sneaking past guards, the Dungeon Master (DM) sets a DC. The player rolls a 20-sided die (D20) and adds modifiers from their character to the roll. If the total meets or beats the DC, the action succeeds. If not, it fails. The D20 introduces randomness, making even skilled characters sometimes fail in challenging situations, adding excitement to the game.

The program should take in a single integer value representing the DC then randomly roll a value from 1 to 20 inclusively. Determine if the player was successful at succeeding the ability check.
"""

# import statement
from random import randrange

# input
difficulty = int(input("Enter the DC: "))

# processing & output
player_roll = randrange(1,21) # randrange(a, b) never includes b; moreover, it goes up to b

print(f"The player has rolled {player_roll} on their D20.")

if player_roll >= difficulty:
    print(f'The player was successful as {player_roll} >= {difficulty}.')
else:
    print(f'The player was not successful as {player_roll} < {difficulty}.')
