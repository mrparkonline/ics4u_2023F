# Q4) Perfect Numbers (Solution Link)
 
# The proper divisors of a number are the factors of a number that is not equal to itself.
# Example → 12 has the proper divisors of: 1, 2, 3, 4, 6.
# A perfect number is defined when the sum of a number’s proper divisors equal to the number itself.
# Find the total sum of perfect numbers under 10,000.


# Solution Planning --> Adding perfect numbers
#   1. Generate numbers from [1 to 10,000)
#   2. Everytime I find a "perfect number" add it to a variable

# Solution Planning --> Finding a perfect number
#   1. Let N be a number of interest
#   2. Analyze [1, N) ... find the factors
#   3. Add up the found factors.
#       3a. If the total_sum of found factors == N --> perfect number
#       3b. If the total_sum of found factors < N --> a deficient number
#       3c. If the total_sum of found factors < N --> a abundant number

