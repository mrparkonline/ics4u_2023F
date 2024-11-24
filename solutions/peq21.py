# Amicable Numbers
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divides evenly into n).

Two numbers A and B are amicable numbers and are considered to be an amicable pair if the following is true:
	
	d(A) = B and d(B) = A
where 
A != B.

For example:
d(220) = 284 → sum([1,2,4,5,10,11,20,22,44,55,110]) is 284
d(284) = 220 → sum([1,2,4,71,142]) is 220

Therefore 284 and 220 are amicable pairs and amicable numbers.

Find the total sum of all amicable numbers under 10000.
'''

#def proper_div(num):
    # return a list of proper divisors
#    return [divider for divider in range(1, num) if num % divider == 0]
# end of proper_div()
from math import sqrt

# Optimized proper_div() function
def proper_div(num):
    upper_limit = int(sqrt(num)) + 1
    result = {1}
    for div in range(2, upper_limit):
        if num % div == 0:
            result.add(div)
            result.add(num // div)
    return result

factor_sum = {0:0, 1:1}

for num in range(1, 10000):
    factor_sum[num] = sum(proper_div(num))

amicables = set()
for key, value in factor_sum.items():
    if key not in amicables and key != value:
        if value < 10000 and factor_sum[value] == key:
            amicables.add(key)
            amicables.add(value)

print(f"Sum of all amicable numbers are {sum(amicables)}.")