'''
Possible Sum in a Sorted Array 

Given a list containing integers in (ascending) order as an argument of a function, and a target value as the other argument of a function, return True if two numbers add up to a target, False otherwise.

Example:
array: [1, 3, 5, 8, 12, 13, 22]
target: 16

True b/c 13 + 3 is 16.

Notes:
    The list is SORTED in ascending order. You may assume that all list argument will  be sorted
    There are NO repeated numbers in the list argument
    Your job is to answer true or false, that is, a boolean (you don't need to return the pair or the positions).
    You can't add a number with itself (these would be not valid: 1 + 1, 3 + 3, etc.)

Fun Fact: This is a question that was once asked in a Google Technical Interview.
'''

def possible_sum(a_list, target):
    ''' checks if the target can be made from two unique values in the list

    argument
        a_list : a list of integers that are sorted from least to greatest
        target: an integer value
    
    returns:
        boolean : True if possible otherwise False
    '''
    for i, value in enumerate(a_list):
        new_target = target - value
        if new_target in a_list[i+1:]:
            return True
    # end of for loop
    return False
# end of possible_sum()

# testing
test = [1, 3, 5, 8, 12, 13, 22]
target = 13

print(f"Can {target} be made from two unique values in: {test}?")
print(possible_sum(test, target))