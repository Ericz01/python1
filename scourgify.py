import sys
import csv

def main():
    file_open_error()
    after()
def file_open_error():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if sys.argv[1] != 'before.csv' and sys.argv[2] != 'after.csv':
        sys.exit(1)
def after():
    try:
        after = []
        #open before file in read mode
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name1, name2 = row['name'].split(',')
                after.append({'first': name2.lstrip(), 'last': name1.lstrip(), 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
    #write new file
    with open(sys.argv[2], 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=['first', 'last', 'house'])
        writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
        for row in after:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})
        print(sys.argv[2])
        

if __name__ == "__main__":
    main()
