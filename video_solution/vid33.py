# Duplicates finders

# Create a function that takes two string inputs, return a single sorted list of characters that are found in each string.

def duplicates(word1, word2):
    ''' looking at the characters each string shares

    arguments:
        word1: a string
        word2: a string
    
    return
        list: a lexicographically sorted list of strings
    '''
    if not word1 or not word2:
        return [] # an empty list because one or both strings are empty
    else:
        set_word1 = set(word1)
        set_word2 = set(word2) # creates a set with no duplicates of each individual characters in string of word2
        # why set? because membership operator is more efficent with sets
        
        result = [] # a list to add all duplicates
        for character in set_word1:
            if character in set_word2:
                result.append(character)
        # end of for loop
        return sorted(result)
# end of duplicates
print(duplicates('hello world', 'goodbye world'))