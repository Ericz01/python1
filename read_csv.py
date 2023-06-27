import csv

nyagas = []
with open('names.csv') as file:
    reader = csv.reader(file) 
    for name, team in reader:
        nyagas.append({'name': name, 'team': team})
for nyaga in sorted(nyagas, key=lambda nyaga: nyaga['name']):
    print(f"{nyaga['name']}---{nyaga['team']}")
