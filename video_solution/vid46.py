# Q9) Words to Length Relationship

# Write a function that returns a dictionary. The function will be given a list of strings as its argument. The key should be the strings themselves and the values should be the length of the string.
# ["apple", "banana", "cherry", "date"] = {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}

def word_length(a_list):
    # assuming a_list contains strings
    # result = {} # empty dictionary
    # for word in a_list:
    #     result[word] = len(word)
    # return result
    
    # Using Dictionary Comprehension
    return {key : len(key) for key in a_list}
# word_length()

print(word_length(["apple", "banana", "cherry", "date"]))

# Q10) Fibonacci Dictionary (Revisited)

# Create a function that returns a dictionary given an integer argument. Store nth value as a key and nth fibonacci values within the key’s location.

# Assume that initially the dictionary starts as = {0:0, 1:1}

def d_fib(num):
    result = {0:0, 1:1}
    if num in result:
        return result
    else:
        for i in range(2, num+1):
            result[i] = result[i-1] + result[i-2]
        
        return result
# end of d_fib()

print(d_fib(10))