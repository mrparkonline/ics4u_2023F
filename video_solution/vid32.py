# Anagram

# Create a function that checks if the two strings arguments are anagrams. The function should return True if the two strings are anagrams.

# Example:
# bored and robed are anagrams
# jake and jasper are not anagrams

# Anagram: a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Solution 1 Idea
# 1. length of each string must be equal
# 2. each letter must occur the same number of times and all letters must be within each other


def anagram(word1, word2):
    ''' determines if the two arguments are anagrams of each other

    argument
        word1: a string value... expected to have only alphabetical lowercased characters
        word2: a string value... expected to have only alphabetical lowercased characters
    
    return
        boolean: True if the arguments are anagram, False if not
    '''
    if len(word1) != len(word2):
        return False # not an anagram
    else:
        # Look through all the letters
        for character in word1:
            if word1.count(character) != word2.count(character):
                return False # not an anagram
        # end of for loop
        return True # we were not able to prove that it is not an anagram therefore --> True
# end of anagram
result1 = anagram("bored", "robed")
result2 = anagram("jake", "jasper")
result3 = anagram("hello", "maybe")
result4 = anagram("cinema", "iceman")

print(result1, result2, result3, result4) # expecting True False False True

# Solution 2 Idea
# If lengths are not equal --> False
# Else:
#   Sort each string from a > z
#   Starting at index 0, if the characters are mismatched --> False
#   If we reach the end then, it is confirmed to be an anagram
def anagram2(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        list_word1 = sorted(word1) 
        # sorted sorts a string lexicographically and 
        # stores each individual characters as items in a list
        list_word2 = sorted(word2)

        for i, character in enumerate(list_word1):
            if list_word2[i] != character:
                return False
        # end of for loop
        return True # we have an anagram
# end of anagram2

# end of anagram2()
result1 = anagram2("bored", "robed")
result2 = anagram2("jake", "jasper")
result3 = anagram2("hello", "maybe")
result4 = anagram2("cinema", "iceman")

print(result1, result2, result3, result4) # expecting True False False True