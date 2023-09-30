# Iterations Lesson

# While Loop --> a loop to use when we don't know when to end.
# 1. initialize a condition variable to make the loop run
# 2. make sure that the condition variable turns False so that we can exit the loop at one point
# 3. the condition variable should have the potential to change within the code block

condition_variable = True
password = "poop"

while condition_variable:
    user_input = input("Guess the password: ")

    if user_input == "poop":
        print("Correct guess!")
        condition_variable = False # condition variable turned false making our while terminate
    else:
        print("Incorrect guess!")
# end of while loop
print('\n')

# For loop --> 
# a loop that looks at each value in a iterable object and assigns it to its iterating variable one by one until the end

user_input = input("Search for a fruit: ")

fruits = ['Apple', 'Banana', 'Kiwi', 'Strawberry']
found = False

for fruit_name in fruits:
    if fruit_name == user_input:
        print(f"{user_input} is found!")
        found = True
# end of for loop

if not found:
    print(f"{user_input} is not found...")