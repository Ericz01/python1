import csv
import pandas as pd
from tabulate import tabulate

site = input('Enter the website\'s name: ').rstrip()
username = input('Enter the website\'s username: ').rstrip()
info = []
with open('information.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Website'] == site and row['Username'] == username:
            info.append(row)
if len(info):
    print(info)
else:
    print('No info added')
    #print(f'{site} exists with the same username. View the main menu for more options.')