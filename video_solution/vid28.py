# String Cleaning Function
# Write a function that removes non-alphabetical characters from the given string and returns it as a lowercase version of the cleaned string.

# Example → 'H E L L 0O!' = 'hello'

# Function:
# 	1 argument string

# Returns:
# 	1 string object

# Solution planning
# 1. the function should take a single argument and return a string
# 2. look through each character of the string ... grab only alpha characters or remove non-alphacharacters
# 3. grow an empty string to a string filled with alphabetical characters

# String method to use: .isalpha() ... returns True if the string has only "Letter" characters from the ASCII table

def string_cleaner(text):
    ''' to clean a string with non alpha characters and put them all in lowercased

    arguments
        text : a string argument that is to be cleaned

    returns
        a string object with only alphabetical lowercased character
    '''
    result = '' # initialized an empty string
    for character in text:
        # since strings are immutable, I cannot mutate and remove characters that I don't want
        #print(character)
        if character.isalpha():
            #result = result + character.lower()
            result += character.lower()
            # .lower() makes a string all lowercased
            # + operator is a concatenation operator to combine strings

    return result
# end of string_cleaner()

value = string_cleaner('hELL0, wORLD!')
print(f"Value is: {value}")