# Pattern Creator

# Write a function that takes an N integer greater than 0 and outputs/prints the following pattern.
# N = 5

# 1
# 10
# 101
# 1010
# 10101

def create_line(num):
    ''' returns a string of 1 and 0 based on the argument

    argument:  
        num: integer, to determine how long the string is

    return:
        text: series of 1 or 0 as a string
    '''

    text = ''
    for i in range(1, num+1): # example if num is 5, range(1,6) --> 1,2,3,4,5
        if i % 2 == 0:
            # i is even.
            text += '0'
        else:
            text += '1'

    return text
# end create_line()

def output_pattern(num):
    
    for i in range(1, num+1):
        print(create_line(i))
# end of output_pattern

v = output_pattern(5)
print(v)