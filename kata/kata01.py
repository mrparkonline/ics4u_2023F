# Square and Cube of a Number Become Prime When Reversed
# https://www.codewars.com/kata/5644a69f7849c9c097000073

# The number 89 is the first positive integer that has a particular, curious property:

# The square of 89 is 7921; 89² = 7921

# The reverse of 7921 is 1297, and 1297 is a prime number.

# The cube of 89 is 704969; 89³ = 704969

# The reverse of 704969 is 969407, and 969407 is a prime number.

primes = {2}
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
# end of isPrime()

result = []
start = 1
upper = 150
while len(result) < upper:
    square = start ** 2
    reverse = int(str(square)[::-1])
    if isPrime(reverse):
        cube = start ** 3
        reverse = int(str(cube)[::-1])
        if isPrime(reverse):
            result.append(start)
            #print(start)
    
    start += 1

print(result)
    
