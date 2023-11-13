# Smallest Multiples

# Solution 1: LCM from mathematics
from math import lcm
print(f"The LCM of all numbers 1 to 20: {lcm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20).}")

# Solution 2: Without knowing Python's LCM.
def p_factorize(num):
    answer = {}

    while num % 2 == 0:
        if 2 not in answer:
            answer[2] = 1
        else:
            answer[2] += 1
        num //= 2
    # end of while

    div = 3
    while num != 1:
        if num % div == 0:
            if div not in answer:
                answer[div] = 1
            else:
                answer[div] += 1
            num //= div
        else:
            div += 2
    return answer
# end of p_factorize
prime_factors = {}

for num in range(1,21):
    current = p_factorize(num)
    for base, exponent in current.items():
        if base in prime_factors:
            prime_factors[base] = max(prime_factors[base], exponent)
        else:
            prime_factors[base] = exponent
# end of setting up all the prime base with highest exponents

answer = 1
for base, exponent in prime_factors.items():
    answer *= (base ** exponent)
print(f"The LCM of all numbers 1 to 20: {answer}.")

# Solution 3: Brute Force
from math import factorial
def brute(num=20):
    start = factorial(num)

    for num in range(20, start, num):
        found = True
        for div in range(1, num+1):
            if num % div != 0:
                found = False
                break
        if found:
            return num
    return start
# end of brute
print(f"The LCM of all numbers 1 to 20: {brute()}.")