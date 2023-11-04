# Q1. Remove Duplicates in a list
# List Version
def r_duplicates(a_list):
    result = []

    for value in a_list:
        if value not in result:
            result.append(value)
    return result
# end of r_duplicates(a_list)
print(r_duplicates([1,2,2,3,3,3,4,4,4,4]))

# Set Version
def r_duplicates2(a_list):
    #set_version = set(a_list)
    #return list(set_version)
    return list(set(a_list))
# end of r_duplicates2

print(r_duplicates2([1,2,2,3,3,3,4,4,4,4]))

# Q2. Unique Letters in Given Words
# Write a Python function that takes a list of words and returns a set containing all unique letters used in these words.
def unique_letters(a_list):
    # a_list will contain strings of words
    result_set = set() # set() is an empty set not {} ... because that is a dictionary
    for word in a_list:
        tmp_set = set(word) # convert the string word into a set
        result_set = result_set | (tmp_set) # | operator is union ... we can also use |= if we wished
    
    return result_set
# end of unique_letters

test = ["hello", "goodbye", "world", "mr. park!"]
print(unique_letters(test))

# Q3. Set Intersection Count

# Write a Python function that takes a list of sets and returns the count of elements that are common to all the sets.

def i_count(a_list):
    # a_list contains numerous sets
    if a_list:
        result_set = a_list[0] # grab the first value from a_list

        for example_set in a_list[1:]:
            result_set = result_set & example_set # & is the intersection operator
        
        return len(result_set) # len() will count how many values our result_set has.
# end of i_count
test = [{1,2,3,7}, {3,4,5,7}, {5,6,7,8}]
print(i_count(test))