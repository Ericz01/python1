import csv

with open('names.csv', 'w') as file:
    writ:er = csv.writer(file)
    for name, team in writer:
        name, team = line.rstrip().split(',')
        if name == 'Eric':
            team == 'Chelsea Fc'
        print(f"{name} -- {team}")
