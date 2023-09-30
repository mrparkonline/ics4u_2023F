# Q6) Create an Nth Fibonacci number finder (Solution Link)
# Given an integer input of N greater than -1, create a program that outputs the Nth fibonacci number.
# Example.
# 0th Fibonacci number is 0, 1st Fibonnaci number is 1,  10th is 55, 19th 4181

# Formula: Fib(n) = Fib(n-1) + Fib(n-2) ;
# Fib(0) = 0; Fib(1) = 1

upper_limit = int(input("Enter N to find the Nth Fibonacci Number: "))

fib_0 = 0 # fib(0)
fib_1 = 1 # fib(1)
fib_n = 0 # not found yet ... currently N is 2

for n in range(2, upper_limit+1):
    fib_n = fib_1 + fib_0 # calculated fib(n)
    
    # prepping for the next fib(n)
    fib_0 = fib_1 # fib(n-2) becomes the current fib(n-1)
    fib_1 = fib_n # fib(n-1) becomes the current fib(n)
# end of for loop

print(f"Fibonacci({upper_limit}) is {fib_n}.")