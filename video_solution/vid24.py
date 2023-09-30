# Longest Name. (Solution Link)
# Create a program that takes an unknown amount of names and outputs the longest name. You will know that the inputs are done when the user has inputted a string of X

# Solution plan

# 1. Different kind of infinite loop, condition: while name != 'X'
# 2. initialize, name that creates the longest length, the longest length value
# 3. analyze each input, grab the length via len(), compare and update if needed

# Solution

# variable initializations

name = '' # this is an empty string ... this is made for while loop

longest_length = 0 # for the answer
longest_name = '' # for the answer

while name != 'X':
    # get name as user input
    name = input("Enter your name or 'X' to exit.: ")

    if name != 'X':
        current_length = len(name)

        if current_length > longest_length:
            longest_length = current_length
            longest_name = name
        # end of if
    else:
        print("End of the inputs.")
# end of while loop

if longest_name:
    print(f'The longest name with {longest_length} characters is {longest_name}.')
else:
    print('Not enough data.')