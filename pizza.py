import sys
import csv
from tabulate import tabulate

def main():
    errors()
    convert()

def errors():
    #handle input errors
    if len(sys.argv) < 2:
        sys.exit('Too few command-line argument')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')

def convert():
    try:
        pizza = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizza.append(row)
        print(tabulate(pizza, headers='keys', tablefmt='grid'))
    except FileNotFoundError:
        sys.exit('File does not exist')

if __name__ == "__main__":
    main()
