

# Exercise 2

# import csv 

# with open("data/sales.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# Exercise 3


import csv


with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)

    for row in reader:
        print(row)