#  Prime Number Checker

# Given an integer input greater than 1, determine if the inputted integer is a prime number.

# Solution 1: By counting the number of factors
# a prime number should only have two factors, 1 and itself
# if a number has more than 2, it is not a prime number ... it is a composite number
# so from [1 to N], increase a counter if we find a factor
# after the iteration, determine if it's prime by comparing the counter

# Solution 2: Assume all numbers are prime until proven otherwise
# Steps:
# 1. Consider a number to be prime
# 2. Look at all numbers from [2, N-1] , let N be user input > 1
# 3. if we find a factor from [2, N-1], then N is not a prime number
# 4. if we don't find a factor from [2, N-1], then N is a prime number