# Prime Factor Finder
# The prime factors of 13195 are 5, 7, 13, 29. Write a program that can find the prime factors of a number. 

# Determine the largest prime factor for the number 600851475143.  

# Solution Plan
# 1. Knowing that the smallest possible prime factor is 2. 
#       Continuously divide the number by two if possible.
# 2. The next possible prime factor is 3 and odd primes
#       Set a variable to 3 and divide by 3 as many time as possible until not divisible
#       When not divisible, increase the variable by 2 then repeat the division
#       continue to do this until number is 1. (num / num == 1)

# target = 600851475143
# answer = 6857

num = int(input("Enter a value of N:"))
num_copy = num

largest = 0

while num % 2 == 0:
    # we are checking to see if it is divisble by 2 and then continously shrink it by dividing it by 2
    #num = num // 2
    num //= 2

    largest = max(largest, 2)
# end of while

if num != 1:
    # we still have to check other primes
    factor = 3
    while num != 1:
        if num % factor == 0:
            # we have found a prime factor
            largest = max(largest, factor)
            num //= factor
        else:
            factor += 2 
            # check the next odd number ... it is guaranteed to be a prime if we were to execute the if statement

print(f'{largest} is the largest prime factor for {num_copy}.')