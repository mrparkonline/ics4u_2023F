# Basic Statistics

# Create a function for each statistical analysis tool: mean, and median. Each function should take a single list of integers as an argument, and then output the result.

def mean(a_list):
    ''' calculation of the total average from a given list of integers
    
    argument
        a_list: list of integers
    
    return
        int: the calculated average
    '''
    return sum(a_list) / len(a_list)
# end of mean

def median(a_list):    
    ''' the middle most value in a given sorted list of integers
    
    argument
        a_list: list of integers
    
    return
        int: the middlemost value (or the average of the middle two values)
    '''
    # sorted() creates a new_list
    # a_list.sort() --> will mutate our a_list

    sorted_a_list = sorted(a_list)
    middle = len(a_list) // 2

    if len(a_list) % 2 == 0:
        # we have even number of data points
        left = sorted_a_list[middle-1]
        right = sorted_a_list[middle]
        return (left+right) / 2 
    else:
        # we have odd number of data points
        return sorted_a_list[middle]
# end of median()

# Testing
from random import seed
from random import randrange

seed(2)
data = [randrange(1,100) for _ in range(randrange(10,30))] # list comprehension
print(f'Our random dataset: {data}')
print(f'Our sorted dataset: {sorted(data)}')
print(f'Mean of our dataset: {mean(data)}')
print(f'Mean of our dataset: {median(data)}')