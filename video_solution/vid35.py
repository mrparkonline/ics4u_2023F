# Some useful functions
# Comma Separated Values to List

# Create a function that takes a string argument with a comma separating different integer values. Convert the argument to a list of integers.

# Example: “1,2,3,4,5” → [1,2,3,4,5]

def csv_to_list(text):
    ''' to convert a string with numerics separated by commas to a list of integers

    argument
        text: a string csv
    
    return
        list: a list of integers
    '''
    csv = text.split(',')
    a_list = [] # add values to this list

    for item in csv:
        a_list.append(int(item))
    
    #print(csv)

    return a_list
    #return [int(item) for item in text.split(',')]
# end of csv_to_list()

# List of random integers

# Create a function that takes 3 arguments: (start, end, frequency). The function should return a list of random [frequency] many integers from [start, end].
from random import randrange

def rand_list(start, end, frequency):
    if start < end and frequency > 0:
        a_list = []
        for _ in range(frequency):
            new_value = randrange(start, end+1)
            a_list.append(new_value)
        return a_list
    else:
        return []
    
    # list comprehension method:
    # return [randrange(start, end+1) for _ in range(frequency)]
# end of rand_list

print(csv_to_list("1,2,3,4,5"))
print(rand_list(1, 1000, 30))