# Amicable Numbers

# imports
from math import sqrt

def p_factors(num):
    factors = {1} # 1 is always a factor
    upper_limit = int(sqrt(num)) + 1
    for i in range(2, upper_limit):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors
# end of p_factors

amicables = set()
for num in range(1, 10000):
    current = p_factors(num)
    total_sum = sum(current)

    if num != total_sum: # checking for perfect numbers
        other = p_factors(total_sum)
        other_sum = sum(other)

        if other_sum == num:
            amicables |= {other_sum, total_sum}
    else:
        print(f"{num} is a perfect number not an amicable number.")

print(f"Our amicable numbers: {amicables}.")
print(f"Total sum: {sum(amicables)}.")