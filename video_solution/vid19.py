#  Prime Number Checker

# Given an integer input greater than 1, determine if the inputted integer is a prime number.

# Solution 1: By counting the number of factors
# a prime number should only have two factors, 1 and itself
# if a number has more than 2, it is not a prime number ... it is a composite number
# so from [1 to N], increase a counter when we find factors
# after the iteration, determine if it's prime by comparing the counter

num = int(input("Enter the value of N: "))

counter = 0 # this is initialized out of for loop, so that we can manipulat it from the inside

for divider in range(1, num+1):
    if num % divider == 0:
        # then divider is a factor
        counter += 1
# end of for loop
if counter == 2:
    print(f'{num} is a prime number.')
else:
    print(f'{num} is a composite number.')

# Solution 2: Assume all numbers are prime until proven otherwise
# Steps:
    # 1. Consider a number to be prime
    # 2. Look at all numbers from [2, N-1] , let N be user input > 1
    # 3. if we find a factor from [2, N-1], then N is not a prime number
    # 4. if we don't find a factor from [2, N-1], then N is a prime number
    # Assumption that all N has a factor of itself and 1.

num2 = int(input("Enter N:"))

is_prime = True

for divider in range(2, num2):
    if num2 % divider == 0:
        # divider is a factor; therefore, num2 is not a prime
        is_prime = False
        break # this keyword allows us to exit the loop
# end of for loop

if is_prime:
    print(f'{num2} is a prime number.')
else:
    print(f'{num} is a composite number.')