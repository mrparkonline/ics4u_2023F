# GCD

# In mathematics, the greatest common divisor(gcd) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. For example, the gcd of 8 and 12 is 4; the gcd of 27 and 1080 is 27.

# Create a function that returns the GCD of two integers.

def gcd(num1, num2):
    ''' calculates the gcd of num1 and num2

    arguments:
        num1: int value assumed to be greater than 0
        num2: int value assumed to be greater than 0
    
    returns:
        int: the GCD of num1 and num2
    '''
    for divider in range(min(num1,num2), 0, -1):
        if num1 % divider == 0 and num2 % divider == 0:
            return divider
    # end of for loop
    return 1
# end of gcd()

print(f"The GCD of 8 and 12: {gcd(8, 12)}")
print(f"The GCD of 27 and 1080: {gcd(27, 1080)}")

# Euclidean Algorithm using Recursion
def e_gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return e_gcd(num2, num1 % num2)
# end of e_gcd
print(f"The GCD of 8 and 12: {e_gcd(8, 12)}")
print(f"The GCD of 27 and 1080: {e_gcd(27, 1080)}")