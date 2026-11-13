

from datetime import datetime

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
        

# Exercise 6

revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"\nTotal revenue with DictReader: ${revenue:.2f}")

# csv.reader uses column indexes which is good for simple CSV files with a fixed column order, while DictReader uses column names which makes code easier to understand when using multiple columns.

# Exercise 7
sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

print("\nSales summary by product:")

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")




# Exercise 8

current_time = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(f"{current_time} - total revenue: ${revenue:.2f}\n")

print("run log updated")
