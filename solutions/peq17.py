# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are (3+3+5+4+4) 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

table = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight', 
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve', 
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
	20 : 'twenty',
    30 : 'thirty',	
    40 : 'forty',	
    50 : 'fifty',	
    60 : 'sixty',	
    70 : 'seventy',	
    80 : 'eighty',	
    90 : 'ninety',
    100 : 'hundred',
    1000 : 'onethousand',
}

# Test
count = 0

# From 1 to 20
for num in range(1, 6):
    count += len(table[num])

print(f'There are {count} many characters used from 1 to 5.')

def num_to_word(num, mapper):
    # Designed for 1 to 999.
    if num in mapper:
        return mapper[num]
    else:
        first_digit = int(str(num)[0])
        if num >= 100:
            last_two = int(str(num)[1:])
            if last_two == 0:
                mapper[num] = table[first_digit] + table[100]
            elif last_two not in mapper:
                mapper[last_two] = num_to_word(last_two, mapper) # Recursion!
                mapper[num] = table[first_digit] + table[100] + 'and' + mapper[last_two]
            else:
                mapper[num] = table[first_digit] + table[100] + 'and' + mapper[last_two]
        elif num >= 10:
            last_digit = int(str(num)[-1])
            mapper[num] = table[first_digit*10] + table[last_digit]
        return mapper[num]
# end of num_to_word

count = 0
for num in range(1, 1001):
    count += len(num_to_word(num, table))

count += 3 # for 'one' missing in 100 --> one hundred
print(f'There are {count} many characters used from 1 to 1000.')