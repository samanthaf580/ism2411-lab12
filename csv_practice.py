

# Exercise 2

import csv 

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Exercise 3


import csv


with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)

    for row in reader:
        print(row)



# Exercise 4

revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        revenue += total

        print(f"{product}: {quantity} units x {price:.2f} = ${total:.2f}")
        
        
print(f"\nTotal revenue: ${revenue:.2f}")
   