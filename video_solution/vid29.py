# String Palindrome Checker

# Write a function that returns True if the given string argument is a palindrome. 
# Assume that the argument will only contain alphabetical characters.

# Example → 'tacocat' is a palindrome. 'tacodog' is not a palindrome

# Analyzing Hello! indexing
#  |  H  |  e  |  l  |  l  |  o  |  !  |  H  |  e  |  l  |  l  |  o  |  !  |
# -6    -5    -4    -3    -2    -1     0     1     2     3     4     5    

# Solution 1: Explaining [::-1] slicing
    # Let a = 'Hello!'
    # Indexing grabs single characters ... a[2] --> "l"
    # Slicing grabs a pattern of characters ... a[1:5] --> 'ello'
    # reverse slice of a[::-1] --> !olleh

def is_palindrome1(text):
    ''' checks if our given argument is a palindrome
    
    argument
        text: an alphabetical based string

    return
        a boolean value, True if the text is a palindrome, False otherwise
    '''

    return text == text[::-1]
# end of is_palindrome1()

# Solution 2: Determine the midway point then check to see if the other end is the same
def is_palindrome2(text):
    ''' checks if our given argument is a palindrome
    
    argument
        text: an alphabetical based string

    return
        a boolean value, True if the text is a palindrome, False otherwise
    '''
    if not text:
        # text is an empty string
        return True
    elif len(text) < 4:
        # for strings with lengths of 1,2,3 ... as long as the first and the last characters are the same
        # it is a palindrome
        return text[0] == text[-1]
    else:
        # our text is now guaranteed to be length of 4 or greater
        midpoint = len(text) // 2
        # if the length is odd, we get to ignore the middle most character
        # 01234 ... length of 5
        # HELLO

        # 0123 ... length of 4
        # HELL
        for i in range(0, midpoint):
            left = text[i]
            right = text[-1*i -1]

            # i = 0, -1 ; i=1, -2
            if left != right:
                return False # return in a loop works like a break, where it will auto terminate the loop\
        # end of for loop
        return True 
# end of is_palindrome2()

print(is_palindrome1('tacocat'), is_palindrome2('tacocat'))
print(is_palindrome1('tacodog'), is_palindrome2('tacodog'))