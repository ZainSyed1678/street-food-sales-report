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

    
    