''' telemarketer or Not? CCC 2018 Stage 1, Junior #1
Here at the Concerned Citizens of Commerce (CCC), we have noted that telemarketers like to use seven-digit phone numbers where the last four digits have three properties. Looking just at the last four digits, these properties are:

    the first of these four digits is an 8 or 9
    the last digit is an 8 or 9
    the second and third digits are the same.

Write a program to decide if a telephone number is a telemarketer number or not, based on the last four digits. If the number is not a telemarketer number, we should answer the phone, and otherwise, we should ignore it.
'''

# input
phone = input("Enter the last 4 digits of the phone number: ")

# processing
#if phone[0] == 8 or phone[0] == 9:
if phone[0] in {'8', '9'}:
    # if you have a string, list, or a tuple. We can access the collection's individual items 
    # at a certain location, by doing indexing with square brackets [] ... first item is at location 0.
    if phone[-1] in {'8', '9'}:
        if phone[1] == phone[2]:
            print(f"The phone number with {phone} as its last four digits is a telemarketer.")
        else:
            print(f"The phone number with {phone} as its last four digits is not a telemarketer.")
    else:
        print(f"The phone number with {phone} as its last four digits is not a telemarketer.")
else:
    print(f"The phone number with {phone} as its last four digits is not a telemarketer.")