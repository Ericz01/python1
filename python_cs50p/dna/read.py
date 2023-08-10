import csv
import sys

list1 = []
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        list1.append(row)
    print(list1)