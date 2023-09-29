'''
Factor Finder

Given an integer input greater than 0 (Assume that your input is greater than 0), print all its factors.
'''

# Solution Brainstorm
# 1. Get an integer as user input
# 2. Need to generate all numbers from 1 upto user_input
# 3. Check if any numbers generated are factors (if num is divisible by the generated numbers, we have a factor)
# 4. if true... print the number out

# 1. Get an integer as user input
num = int(input("Enter an integer greater than 0: "))

# 2. Need to generate all numbers from 1 upto user_input
for divider in range(1, num+1):
    print(f"divider variable is: {divider}.")

    # 3. Check if any numbers generated are factors (if num is divisible by the generated numbers, we have a factor)
    if num % divider == 0:
        # we have a factor!
        print(f"{divider} is a factor for {num}.")
        # 4. if true... print the number out