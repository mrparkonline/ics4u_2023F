''' Tournament Selection: Canadian Computing Competition: 2016 Stage 1, Junior #1

Each player in a tournament plays six games. There are no ties. The tournament director places the players in groups based on the results of games as follows:

if a player wins 5 or 6 games, they are placed in Group 1;
if a player wins 3 or 4 games, they are placed in Group 2;
if a player wins 1 or 2 games, they are placed in Group 3;
if a player does not win any games, they are eliminated from the tournament.

Write a program to determine which group a player is placed in.
'''

# input
# game1 = input("Enter game1 result:") # assuming that game result will be either W/L
# game2 = input("Enter game1 result:") # assuming that game result will be either W/L
# game3 = input("Enter game1 result:") # assuming that game result will be either W/L
# game4 = input("Enter game1 result:") # assuming that game result will be either W/L
# game5 = input("Enter game1 result:") # assuming that game result will be either W/L
# game6 = input("Enter game1 result:") # assuming that game result will be either W/L

win_counter = 0
for i in range(6): # range(6) --> 0,1,2,3,4,5 in computer memory
    current_result = input(f"Enter the game {i+1} result:")

    if current_result == "W":
        win_counter += 1 # win_counter = win_counter + 1
# end of for loop

# processing
group = 0 # this is called a variable initialization, creating it for future use
if win_counter > 4:
    group = 1
elif win_counter > 2:
    group = 2
elif win_counter > 0:
    group = 3

# output
if group == 0:
    print("The player is eliminated.")
else:
    print(f"The player is placed in group {group}.")
