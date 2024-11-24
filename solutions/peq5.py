# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
SOLUTION BREAKDOWN
    1. Find the prime factors of all numbers for 2 to 20. (1 is skipped due to not having prime factors)

    2. For each numbers from 1 to 20. Determine the highest exponent for each prime factors.

        Explanation:
            2 generates a prime factor of 2 ^ 1
            4 generates a prime factor of 2 ^ 2
            8 generates a prime factor of 2 ^ 3
            16 generates a prime factor of 2 ^ 4

            From 2 to 20, prime factor of 2 must have an exponent of 4
    
    3. Multiply all the prime powers (prime factors raised to their highest exponent) to determine the LCM of all numbers from 1 to 20.

    Source: https://openstax.org/books/prealgebra-2e/pages/2-5-prime-factorization-and-the-least-common-multiple

'''
def brute_force(a_list):
    # a_list has all the required factors
    largest = 1
    for num in a_list:
        largest *= num
    
    answer = 0
    for value in range(20, largest+1):
        found = True
        for divider in a_list:
            if value % divider != 0:
                found = False
                break
        if found:
            answer = value
            break
    
    return answer
# end of brute_force

print("Brute Forcing:")
test = [x for x in range(1,21)]
print("Answer:", brute_force(test))

def prime_factors(num):
    ''' return a dictionary of primes and exponents (its number of occurance as factors)

    arg:
        num : positive integer
    
    returns:
        dictionary : a prime to factor frequency pairing
    '''
    if num == 1:
        return {}

    result = {} # empty dictionary

    while num % 2 == 0:
        if 2 in result:
            result[2] += 1
        else:
            result[2] = 1
        
        num //= 2
    # end of while
    
    if num == 1:
        return result
    else:
        divider = 3

        while num != 1:
            if num % divider == 0:
                if divider in result:
                    result[divider] += 1
                else:
                    result[divider] = 1
                
                num //= divider
            else:
                divider += 2
        # end of while
        return result
# end of prime_factors

table = {}

for i in range(2, 21):
    current_table = prime_factors(i)

    for key, value in current_table.items():
        if key not in table:
            table[key] = value
        else:
            table[key] = max(table[key], value)

answer = 1

for key, value in table.items():
    answer *= (key ** value)

print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:\n{answer}.")

