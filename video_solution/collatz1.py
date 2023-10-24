'''
Q19) Project Euler (Q14) - Longest Collatz sequence

“The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 

Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?”
'''
# Create a simple function that generates the "next number" following the rules of collatz
def collatz(num):
    if num % 2 == 0:
        # if num is even, divide it by 2
        return num // 2
    else:
        # if num is odd, 3 * num + 1
        return (3 * num) + 1
# end of collatz

# This function calculates how long the "num"'s collatz sequence is.
def collatz_seq(num):
    result = num
    counter = 1

    while result != 1:
        result = collatz(result)
        counter += 1
    
    return counter
# end of collatz_seq

# We are now going to generate every number's collatz sequence length and store it in a list
collatz_length = [0, 1] # index 0 has 0 length; index 1 has 1 length
for num in range(2, 1000001):
    size = collatz_seq(num)
    collatz_length.append(size)

print("Generated million collatz sequence lengths.")

# Analyze each length, then we see which number generated the longest.
answer = 0
longest_seq_size = 0
for start_num, size in enumerate(collatz_length):
    if size > longest_seq_size:
        answer = start_num
        longest_seq_size = size

print(f"{answer} generated the longest sequence with {longest_seq_size} values.")
# Answer: 837799 generated the longest sequence with 525 values.
