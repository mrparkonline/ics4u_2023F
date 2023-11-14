# Analyzing Waterloo Data

with open("./data.csv", "r") as csv_file:
    for line in csv_file.readlines():
        print(line.split(","))