# Palindromic Number

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Correct Answer: 906609

def is_palindrome(text):
    # this should return true for all palindromes
    return text == text[::-1] # [::-1] an slicing identity to quickly reverse a slicable object

palindromic_numbers = []

for num1 in range(999, 99, -1):
    for num2 in range(999, 99, -1):
        current_product = num1 * num2

        if is_palindrome(str(current_product)):
            # we have a palindromic number
            palindromic_numbers.append(current_product)
# end of our for loops
print(f"The largest palindromic number in our list is: {max(palindromic_numbers)}")