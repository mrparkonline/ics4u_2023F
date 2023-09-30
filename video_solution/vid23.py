# Q7) Average Calculator (Solution Link)
# Create a program that calculates the averages of the marks that user inputs. 
# The user is allowed to input any amount of marks as long as it is 0 to 100.

# Solution Plan

# 1. Create an infinite loop with a variable set to True
# 2. Set the variable false when user input is "exit"
# 3. add valid marks to a variable, count the number of valid marks
# 4. After exiting the loop when possible, then calculate the average

# mean = sum of data / the amount of data

loop = True

total_sum = 0
counter = 0

while loop:
    # as long as the loop variable is True, we execute the code block

    user_input = input("Enter the mark -OR- \"Exit\" to stop inputting marks: ")

    if user_input.lower().capitalize() == "Exit":
        loop = False
        break # exit the loop
    else:
        mark = int(user_input)
        if 0 <= mark <= 100:
            # we have a valid mark
            total_sum += mark
            counter += 1
        else:
            print("Invalid input")
# end of while loop

average = total_sum / counter

print(f"Your average is: {average}.")
