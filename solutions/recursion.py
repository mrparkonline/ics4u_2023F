# Recursion Problem Set Solution

# Q1. Non-Tail Factorial Recursive Solution
def factorial(num):
    if num in {0,1}:
        return 1
    else:
        return num * factorial(num-1)
# end of factorial()

# Tail Recursion w. Factorial
def factorial2(num, tail=1):
    if num == 0:
        return tail
    else:
        return factorial2(num-1, tail*num)
# end of factorial2()

# Q2. Exponentiation --> non-tail version
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent-1)
# end of power()

# Exponentiation tail recursion
def power(base, exponent, tail=1):
    if exponent == 0:
        return tail
    else:
        return power2(base, exponent-1, tail*base)
# end of power2()

# Q3. Palindrome | Assuming our inputs are all constant cases without spaces
def is_palindrome(word):
    if len(word) <= 1: # Base Case 1: Empty and Single Length Strings are palindromes
        return True
    elif len(word) <= 3: # Base Case 2: Two/Three Character strings are a palindrome if the first and last are equal
        return word[0] == word[-1]
    else: # Recursive Case: All Strings are palindromes if their first and last characters are equal and the inner portion is a palindrome
        return word[0] == word[-1] and is_palindrome(word[1:-1])
# end of is_palindrome()

def is_palindrome2(word, tail=True): # We assume all words are palindrome until proven otherwise
    if not tail: # At any point tail turns False, we can end the loop
        return tail
    elif not word: # An empty string is a palindrome, so compare with status of tail
        return True and tail 
    else:
        # tail is now assigned to the comparison of first and last character
        # word loses its first and last character
        return is_palindrome2(word[1:-1], word[0] == word[-1])
# end of is_palindrome2()

# Q4. Reverse a String
def str_reverse(word):
    if len(word) <= 1:
        return word
    else:
        return word[-1] + str_reverse(word[:-1])
# end of str_reverse()

def str_reverse2(word, result=''):
    if not word:
        return result
    else:
        return str_reverse2(word[:-1], result + word[-1])
# end of str_reverse2()

# Q5. Maximum Value in an Array
# Tailed
def largest(array):
    def helper(a_list, tail):
        if not a_list:
            return tail
        else:
            if a_list[0] > tail:
                return helper(a_list[1:], a_list[0])
            else:
                return helper(a_list[1:], tail)
    # end of helper()
    if not array:
        return -1 # error
    elif len(array) == 1:
        return array[0]
    else:
        return helper(array[1:], array[0])
# end of largest()

# Non-Tailed
def largest2(array):
    def helper(a_list, start, end):
        if start == end:
            return array[start]
        else:
            mid = (start+end) // 2

            left_max = helper(a_list, start, mid)
            right_max = helper(a_list, mid+1, end)

            if left_max > right_max:
                return left_max
            else:
                return right_max
    # end of helper()
    return helper(array, 0, len(array)-1)
# end of largest2()

# Q6. Merge Two Sorted Lists
def merge(a_list, b_list):
    if not a_list and not b_list:
        # both lists are empty
        return []
    elif not a_list:
        return b_list
    elif not b_list:
        return a_list
    else:
        if a_list[0] < b_list[0]:
            return [a_list[0]] + merge(a_list[1:], b_list)
        else:
            return [b_list[0]] + merge(a_list, b_list[1:])
# end of merge()

def merge2(a_list, b_list, answer=[]):
    if not a_list and not b_list:
        # both lists are empty
        return answer
    elif not a_list:
        return answer + b_list
    elif not b_list:
        return answer + a_list
    else:
        if a_list[0] < b_list[0]:
            return merge2(a_list[1:], b_list, answer+[a_list[0]])
        else:
            return merge2(a_list, b_list[1:], answer+[b_list[0]])
# end of merge2()

#Q7. Prime Checker
def is_prime(num):
    def helper(num, divider):
        if num == divider:
            return True
        else:
            if num % divider == 0:
                return False
            else:
                return helper(num, divider+2)
    
    if num == 1:
        return False
    elif num in {2,3}:
        return True
    elif num % 2 == 0:
        return False
    else:
        return helper(num, 3)
# end of is_prime()

def is_prime2(num, divider=3, tail=True):
    if not tail:
        return False
    elif num == divider:
        return tail
    elif num <= 1:
        return False
    elif num in {2,3}:
        return True
    elif num % 2 == 0:
        return False
    else:
        if num % divider == 0:
            return is_prime2(num, divider, False)
        else:
            return is_prime2(num, divider+2, True)
# end of is_prime2()

# Q8. Prime Factors of a Number
def prime_factors(num, divider=2):
    if num == 1:
        return []
    elif num == divider:
        return [num]
    else:
        if num % divider == 0:
            return [divider] + prime_factors(num//divider, divider)
        else:
            return prime_factors(num, divider+1)
# end of prime_factors()

def prime_factors2(num, divider=2, tail=[]):
    if num == 1:
        return tail
    elif num == divider:
        return tail + [num]
    else:
        if num % divider == 0:
            return prime_factors2(num//divider, divider, tail+[divider])
        else:
            return prime_factors2(num, divider+1, tail)
# end of prime_factors2()

#Q9. Climbing Stairs
def stairs(steps):
    if steps in {0,1,2}:
        return steps
    else:
        return stairs(steps-1) + stairs(steps-2)
# end of stairs()

# Climbing Stairs is related to the fibonacci sequence
def fib_tail(n, fib1=1, fib0=0):
    if n == 0:
        return fib0
    elif n == 1:
        return fib1
    else:
        return fib_tail(n-1, fib1+fib0, fib1)
# end of fib_tail

# Q10. String Binary Number to Integer Digits
def to_int(binary):
    if not binary:
        return 0
    elif binary == '1':
        return 1
    elif binary == '0':
        return 0
    else:
        if binary[0] == '1':
            exponent = len(binary)-1
            return 2**exponent + to_int(binary[1:])
        else:
            return to_int(binary[1:])
# end of to_int()

def to_int2(binary, tail=0):
    if not binary:
        return tail
    else:
        if binary[0] == '1':
            exponent = len(binary)-1
            return to_int(binary[1:], tail + 2**exponent)
        else:
            return to_int(binary[1:])
# end of to_int2()

# Q11. Twenty Questions
def twentyQ(start=1, end=100, q=0):
    if q == 20:
        print("I lose!")
        return False
    else:
        mid = (start+end) // 2
        user = input(f"Is your number {mid}? (Y/N): ")
        q = q + 1

        if user in 'Yy':
            print(f"I win with {q} questions asked!")
            return True
        else:
            user = input(f"Is your number higher or lower than {mid}? (H/L): ")
            q = q + 1
            if user in 'Hh':
                return twentyQ(mid+1, end, q)
            else:
                return twentyQ(start, mid-1, q)
# end of twentyQ()
