# Video 2: A Sample Python Script
# Date: 09-12-2023

# Purpose: Analyzing the data.txt, create a new file with students emails.
# Student Email Format: studentnumber@gapps.yrdsb.ca

# Step 1: Read the data.txt file and grab the information

with open("./data.txt" , "r") as data_file:
    # with helps us start a "scope" where we can do execute some code on something
    names = data_file.readlines() # .readlines() method generates a list

    clean_data = [] # this is an empty list
    
    for line in names: # this is a "for each loop"
        #print(line)
        example_name = line
        clean_name = example_name.split(',') # .split() returns a list by separating by the given pattern
        clean_name = clean_name[-1] # we can use negative indexing starting -1 to go backwards
        clean_name = clean_name.replace('\n', '@gapps.yrdsb.ca;')

        clean_data.append(clean_name)
    # for loop is finished
    print(clean_data)
# data_file is closed

with open("./class1.txt", "w") as email_file:
    for email in clean_data:
        email_file.write(email)
        print(email, 'has been written to our file.')
    # for loop is finished
    print("Operation Finished.")

    