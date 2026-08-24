import csv

file = open("data.csv","r")

reader = csv.reader(file)
next(reader)
total_sales = {}

for items in reader:
    vendor = items[0]

    try:
        price = float(items[2])
    except ValueError:
        price = 0

    try:
        quantity = int(items[3])
    except ValueError:
        quantity = 0

    
    total = price * quantity

    if vendor not in total_sales:
        total_sales[vendor] = 0

    total_sales[vendor] += total

for vendor, sales in sorted(total_sales.items(), key=lambda x: x[1], reverse=True):
    print(vendor, sales)