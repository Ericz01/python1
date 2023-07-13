students =[
    {'name': 'Eric', 'house': 'Lenana'},
    {'name': 'David', 'house': 'Nelion'},
    {'name': 'Roy', 'house': 'Lenana'},
    {'name': 'Mike', 'house': 'Sendeyo'},
    {'name': 'Job', 'house': 'Lenana'},
    {'name': 'Sly', 'house': 'Nelion'},
    {'name': 'Kyle', 'house': 'Lenana'},
]

def is_lenana(s):
    return s['house'] == 'Lenana'

lenanas = filter(is_lenana, students)

for lenana in sorted(lenanas, key=lambda s: s['name']):
    print(lenana['name'])