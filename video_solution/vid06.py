# Exploring Booleans & Membership Operation

# Truthy & Falsy Values
# All non-empty values will evaluate to True in Boolean settings/context
# All empty values --> '', "", 0, [], set(), {}, None will evaluate to False in Boolean setting/context

'''
name = input("Enter your name:")
if not name: # python way of checking if a variable has an empty value
    print("Name was not given.")
else:
    print(f"Hello, {name}!")
'''

# Membership Operation
# x in a --> checks if x is in a, if found --> True
# x not in a --> checks if x is not in a, if not found --> True

if "a" in "Jasper":
    print("a is found in Jasper.")

if "Apple" not in ["Kiwi", "Blueberry", "Watermelon"]:
    print("Apple was not found in our list of fruits")

if "water" in "watermelon":
    print("water exists inside watermelon.")