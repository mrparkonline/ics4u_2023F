'''Creating a Rock Paper Scissors Game.

Create a program that takes two inputs of Rock, Paper, or Scissors to simulate a 1v1 rock paper scissors game between two people.
'''

# import statement
from random import choice

# input
invalid = True
player = '' # variable initialization

while invalid:
    # code block for the while loop starts here
    player = input("Enter a choice of (rock, paper, or scissors): ")

    if player in {'rock', 'paper', 'scissors'}:
        # we use in operator in python often with sets because of its faster execution speed
        invalid = False
# end of while loop

# processing
cpu = choice(['rock', 'paper', 'scissors'])
print(f"The CPU chose {cpu}.")

# game logic starts here
if player == cpu:
    print("Tie Game.")
else:
    # Guaranteed that one player has won the game.
    if player == 'rock':
        if cpu == 'paper':
            print("The CPU has won the game.")
        else:
            print("The Player has won the game.")
    elif player == 'paper':
        if cpu == 'scissors':
            print("The CPU has won the game.")
        else:
            print("The Player has won the game.")
    else:
        # player chose scissors
        if cpu == 'rock':
            print("The CPU has won the game.")
        else:
            print("The Player has won the game.")
# end of the game logic conditions