# Q9) Common Factors (Solution Link)
# When given two positive integers greater than 1 which are A and B, write a program that prints all the factors that they both share.

# 10 and 24 shares:
# 1
# 2

# Solution
# the largest factor that two numbers (a,b) can share is the minimum of a and b
# generate numbers from [1 to min(a,b)] then find factors to output

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

upper_limit = min(num1, num2)

for divider in range(1, upper_limit+1):
    if num1 % divider == 0 and num2 % divider == 0:
        print(f'{num1} and {num2} share a factor of {divider}.')
# end of for loop