"""
The program takes 2 user inputs:
    start → the amount of money we had before selling cookies
    String of b or c
    num_cookies → a string of character 'c's to denote the number of cookies sold
    Example: 'cccccc' → 6 cookies!
    num_big → a string of character 'b's to denote the number of big cookies sold
    Example: 'bbb' → 3 big cookies!

The program should output:
    Number of total cookies sold
    
    Profit (which is calculated as profit = sales - cost of cookie)
    Total amount of money after selling cookies

Cost of Normal Cookie per cookie → $1.25
Cost of Big cookie per cookie → $2.00
    To make a normal cookie → $0.50
    To make a big cookie → $0.75
"""

# input
start_money = float(input()) # float() helps to cast its argument to a real number
cookies_sold = input() 

# processing
# big_cookies = 0 # this is an example of variable initialization
# cookies = 0
big_cookies = cookies_sold.count('b')
cookies = cookies_sold.count('c')

# for current_cookie in cookies_sold:
#     #print(current_cookie)
#     if current_cookie == "c":
#         #cookies = cookies + 1
#         cookies += 1
#     elif current_cookie == "b": # this is an else if condition
#         big_cookies += 1
#     else:
#         print(f"{current_cookie} is not a valid sale item.")
# end of for

total_cookies = big_cookies + cookies
profit = (big_cookies * 1.25) + (cookies * 0.75)
end_day = start_money + profit

# output
print(f"We sold {total_cookies} cookies. We made ${profit}. We now have ${end_day}.")
