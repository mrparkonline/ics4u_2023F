'''"FizzBuzz." 
From 1 to 50, 
    if the number is a multiple of three: print 'Fizz', 
    if the number is a multiple of five: print 'Buzz', 
    if they are multiples of both: print 'FizzBuzz' 
    otherwise print the number
'''

# range(x) --> [0,X) ... range(10) --> 0,1,2,3,4,5,6,7,8,9
# range(a,b) --> [a, b) ... range(5,10) --> 5,6,7,8,9
# range(a,b, step) --> [a, b) but it will have "step" based interval
#   range(10, 0, -1) --> 10,9,8,7,6,5,4,3,2,1
#   range(1, 10, 2) --> 1, 3, 5, 7, 9
# range() is a generator function that creates iterable integers in a given parameter

# for loops a finite loop ; "for each loop"
# for loops are most commonly used to look through values in an iterable object
for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    # end of if
# end of for
