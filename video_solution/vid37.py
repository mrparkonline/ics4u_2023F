# Factors List
# Create a function that returns a list of factors of the integer argument

# Prime Checker
# Create a function that returns True if the given integer argument is a prime number.

def factors(num):
    ''' creating a list of factors of a number 
    
    argument
        num: an integer, assuming it to be greater than 0
    
    return
        result: a list of the argument's factors
    '''
    result = []
    for divider in range(1, num+1):
        if num % divider == 0:
            result.append(divider)

    return result
# end of factors()

def is_prime(num):
    ''' checks if the given number is a prime
    
    argument
        num: an integer, assuming it to be greater than 0
    
    return
        a Boolean value of True if it is prime; otherwise False
    '''
    return len(factors(num)) == 2
# end of is_prime()

# testing area
print(f'Factors of 13: {factors(13)}')
print(f'Factors of 36: {factors(36)}')
print(f'Is 13 prime?: {is_prime(13)}')
print(f'Is 36 prime?: {is_prime(36)}')