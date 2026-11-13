

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


# Exercise 5

original_count = 0 
written_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as new_file:
        writer = csv.writer(new_file)
        writer.writerow(["Product", "price", "quantity", "total"])

        for row in reader:
            original_count += 1
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count += 1

print(f"Rows written: {written_count}")
print(f"Original rows: {original_count}")
        

