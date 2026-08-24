import csv

file = open("data.csv")

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

for vendor in total_sales:
    print(vendor,total_sales[vendor])