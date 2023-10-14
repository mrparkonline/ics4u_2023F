# Remove Duplicates

# Create a function that removes duplicates from the given list argument.
# Example: ["a","b", "c", "c", "b", "c", "a", "a", "d"] → ["a", "b", "c", "d"]

def remove_duplicates(a_list):
    ''' a function that is used to maintain a single copy of each unique values in a list

    argument
        a_list: a list of various objects

    return
        new_list: a list containing all unique values
    '''
    new_list = []

    for item in a_list:
        if item not in new_list:
            new_list.append(item)

    # simplist solution to write: is to convert the argument to a set and then convert it back to a list

    return new_list
# end of remove_duplicates
test = ["a","b", "c", "c", "b", "c", "a", "a", "d"]
print(f'test list: {test}')
print(f'duplicates removed: {remove_duplicates(test)}')