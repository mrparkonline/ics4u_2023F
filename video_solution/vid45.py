# Character Frequency

# Write a function that takes a string argument and returns a dictionary. The dictionary should have the alphabetical characters as keys in sorted order and each key should be assigned with the character’s frequency. Case should be ignored. 

# Example: 'helLo'

# {'e': 1, 'h'': 1, 'l': 2, 'o': 1}

def c_frequency(word):
    # assume that word is a string
    clean_word = sorted(word.lower())

    answer = {} # this is an empty dictionary

    for character in clean_word:
        if character not in answer:
            # this means that character is not a key in our dictionary answer
            answer[character] = 1
        else:
            answer[character] += 1
    
    return answer
# end of c_frequency()

result = c_frequency("HelLo")
print(f"Character Frequency of hello:\n{result}")