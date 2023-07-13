#a set returns a list with duplicates removed
students =[
    {'name': 'Eric', 'house': 'Lenana'},
    {'name': 'David', 'house': 'Nelion'},
    {'name': 'Roy', 'house': 'Lenana'},
    {'name': 'Mike', 'house': 'Sendeyo'},
    {'name': 'Job', 'house': 'Lenana'},
    {'name': 'Sly', 'house': 'Nelion'},
    {'name': 'Kyle', 'house': 'Lenana'},
]

houses = set()

for student in students:
    houses.add(student['house'])
for house in sorted(houses):
    print(house)
