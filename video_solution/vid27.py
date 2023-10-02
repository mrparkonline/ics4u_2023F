# Functions in Python 3

# 1. To create a function --> def function_name(arg1, arg2 ... ):
# 2. Use triple quotation marks ''' ''' to write your docstrings
# 3. Use the arguments stated and create a instruction set that solves a single problem
# 4. Use return to return the data thats been processed by your function

def is_divisible(num1, num2):
    ''' checks if num1 is divisible by num2
    
    Args:
        num1: an integer, this is our numerator
        num2: an integer, this is our denominator
    
    Return:
        True if num1 is divisible by num2, otherwise False
    '''
    return num1 % num2 == 0
# end of is_divisible

def factor_count(number):
    ''' determines the number of factors the argument has

    Args:
        number: an integer needed to determine the number of its factors

    Returns:
        an integer, which is the total amount of factors the argument has
    '''
    counter = 0
    for divider in range(1, number+1):
        #if number % divider == 0:
        if is_divisible(number, divider):
            counter += 1
    # end of for loop
    return counter 
# end of factor_count()

# Problem. Determine the number of factors for each number from 1 to N.
# Let N be a user input

upper_limit = int(input("Enter N: "))

for num in range(1, upper_limit+1):
    factor_size = factor_count(num)

    print(f"{num} has {factor_size} factors.")