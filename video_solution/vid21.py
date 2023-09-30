# The Most Number of Factors (Solution Link)
# From 1 to N, where N is an integer greater one. We will output the number between [1,N] that has the most factors. 
# Example: From numbers 1 to 5. → The number 4 has the most factors.

# Solution Planning
#   1. Take N is input
#   2. Set max_count to 0, set the result_num to 0 ... variable initialization
#   3. Generate numbers from [1 to N]
#   4. count the number of factors of if each numbers generated
#   5. if the new count is larger than our max_count, update max_count and result_num

upper_limit = int(input("Enter N: "))

max_count = 0
result_num = 0

for num in range(1, upper_limit+1):
    total_factors = 0 # reset this variable everytime this for loop executes the code block

    # counting the number of factors for num
    for divider in range(1, num+1):
        if num % divider == 0:
            total_factors += 1
    # end of inner for loop

    if total_factors > max_count:
        max_count = total_factors # update to hold the largest count so far
        result_num = num # update to hold num, which generated the most factors so far
# end of outer for loop

print(f"{result_num} had the most factors, with {max_count} factors.")