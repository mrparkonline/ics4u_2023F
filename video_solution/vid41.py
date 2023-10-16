# List of Prime Numbers under N

# Create a function that takes N as an argument where N is a positive integer.  The program will store and return the list that stores all the prime numbers that are less than N.

def factors_list(num):
    result = []
    for divider in range(1, num+1):
        if num % divider == 0:
            result.append(divider)

    return result
# end of factors()

def is_prime(num):
    return len(factors_list(num)) == 2
# end of is_prime()

def prime_list(upper_limit):
    '''
    argument:
        upper_limit: an integer value assumed to be a positive value greater than 1

    returns:
        a list: list of all primes under upper_limit
    '''
    primes = [2]
    
    if upper_limit == 2:
        return primes
    else:
        for num in range(3, upper_limit, 2):
            if is_prime(num):
                primes.append(num)

        return primes
# end of prime_list

print(f"List of all primes under 10: {prime_list(10)}")
print(f"List of all primes under 3: {prime_list(3)}")
print(f"List of all primes under 100: {prime_list(100)}")