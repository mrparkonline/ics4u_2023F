# Factorial Question Solution

# Problem input:
num = int(input("Enter a value of N: "))

# Solution 1 --> While Loop
total_product = 1
multiplier = 1

while multiplier <= num:
    # We indent for start of while loop code block
    # this solutions goes from [1 to N]
    total_product = total_product * multiplier;
    # faster way --> total-product

    multiplier = multiplier + 1
    # multiplier += 1
# end of while loop ... # we unindented to end the while loop's code block
print(f"Factorial of {num} is {total_product}.")

# Solution 2 --> For Loop
# This solutions goes from [N to 0)

answer2 = 1

for i in range(num, 0, -1):
    answer2 *= i
# end of for loop

print(f"Factorial of {num} is {answer2}.")

# Solution 3 --> For Loop going upwards with range ... much easier
answer3 = 1
for j in range(1, num+1):
    answer3 *= j

print(f"Factorial of {num} is {answer3}.")