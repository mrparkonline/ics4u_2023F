# Q3) String Consonant Counter

# Write a function that counts the number of consonants in the given string argument. Assume that for simplicity, 'aeiou' are the only set of vowels in English. The function should return an integer

# Example → 'blueberry' → 6 consonants (including 'y')

# Q3b) Extended

# Modify the function so that if the last predetermined argument is False, then the function will calculate the number of vowels instead of consonants.

# Solution Plan
# 1. Look through each individual characters of a string
# 2. if it is an alphabetical character and a consonant, increase a counter
# 3. then returned the value

def consonant_count(text, vowel=False):
    ''' returns the number of consonants in a given string

    argument
        text: a string value containing alphanumeric characters and special symbols
        vowel: it is assumed to be False when counting for consonants

    return
        an integer, a total count of all consonants in text
    '''
    ctr = 0 # this will total up all the consonants

    for character in text:
        character = character.lower()
        if character.isalpha() and character not in {'a','e','i','o','u'}:
            ctr += 1 # we found a consonant to count
    # end of for loop

    if not vowel:
        # we were not interested in counting vowels. 
        return ctr
    else:
        #return len(text) - ctr
        ctr = 0 # this will total up all the consonants

        for character in text:
            character = character.lower()
            if character.isalpha() and character in {'a','e','i','o','u'}:
                ctr += 1 # we found a consonant to count
        return ctr
# end of consonoant_count()

print(f'the count is: {consonant_count("hello, world!")}')
print(f'the count is: {consonant_count("hello, world!", True)}')