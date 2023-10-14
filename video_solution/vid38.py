# String Compression

# Implement a function that performs basic string compression using the counts of repeated characters. Return the string if the compression is longer or the same length as the argument.

# For example, "aabcccccaaa" would become "a2b1c5a3."

def str_zip(text):
    result = ''
    ctr = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            # same character detected, increase the frequency
            ctr += 1
        else:
            # a new character detected, concatenate the previous character and its frequency
            result += text[i-1]
            result += str(ctr)
            # can be done as: result += text[i-1] + str(ctr)
            ctr = 1 # reset to one, it will be counting the new character analyzed
    
    # our final iteration of the loop does not account for the collection ending, so ...
    # we must concatenate the last character and its frequency.
    result += text[-1] + str(ctr)

    # if the length of the compression is less than the original text, return the compression
    if len(result) < len(text):
        return result
    else:
        return text
# end of str_zip()    

test = [
    "aabcccccaaa", "abcde", "aaabb", 
    "aabbccddddeeeee", "a", "aaaaaaaaaaabbbbbbbbbbb"
]
expected = ["a2b1c5a3", "abcde", "a3b2", "a2b2c2d4e5", "a", "a11b11"]

for i, test_value in enumerate(test):
    output = str_zip(test_value)
    print(f'Test {i+1}:')
    print(f'Inputted Value: {test_value}')
    print(f'Outputted Value: {output} & Expected Value: {expected[i]}')
    print(f'Test Passed: {output == expected[i]}')
    print('-'*25)