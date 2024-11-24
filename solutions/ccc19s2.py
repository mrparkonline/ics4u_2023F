# Pretty Average Primes
# https://dmoj.ca/problem/ccc19s2

''' Sample input
4
8
4
7
21
'''

'''
Sample Output
3 13
5 3
7 7
13 29
'''

''' Find A + B = 2N where A and B are both primes. '''
from math import sqrt
# Helper Functions
def primes1(num):
    # primes <= num ... primes greater than 3

    def is_prime(num):
        if num < 2:
            return False
        elif num in {2,3}:
            return True
        elif num % 2 == 0:
            return False
        else:
            stop = int(sqrt(num)) + 1
            for i in range(3, stop, 2):
                if num % i == 0:
                    return False
            return True
    # end of is_prime()

    result = {3} | set(filter(is_prime, range(5, num, 2)))
    return result
# end of primes1()
'''algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
                set A[j] := false

    return all i such that A[i] is true.'''
def primes2(num):
    result = [False, False] + [True] * (num-1)
    stop = int(sqrt(num)) + 1
    for i in range(2, stop):
        if result[i]:
            for j in range(i**2, num+1, i):
                result[j] = False
    return result
# end of primes2()

primes = set()
def isPrime(n):
    if n < 2:
        return False
    elif n in primes:
        return True
    else:
        if n % 2 == 0:
            return False
        else:
            limit = int(n ** 0.5) + 1

            for divider in range(3, limit):
                if n % divider == 0:
                    return False

            primes.add(n)
            return True
# end of isPrime

size = int(input())

nums = []
upper_limit = 0
for _ in range(size):
    current = int(input()) * 2
    upper_limit = max(upper_limit, current)
    nums.append(current) 

for num in nums:
    start = 3
    for x in range(start, num+1, 2):
        if isPrime(x):
            diff = num - x
            if isPrime(diff):
                print(x, diff)
                break
