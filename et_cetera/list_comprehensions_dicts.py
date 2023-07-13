#a list_comprehension returning Lenana students
students =[
    {'name': 'Eric', 'house': 'Lenana'},
    {'name': 'David', 'house': 'Nelion'},
    {'name': 'Roy', 'house': 'Lenana'},
    {'name': 'Mike', 'house': 'Sendeyo'},
    {'name': 'Job', 'house': 'Lenana'},
    {'name': 'Sly', 'house': 'Nelion'},
    {'name': 'Kyle', 'house': 'Lenana'},
]

lenanas = [
    student['name'] for student in students if student['house'] == 'Lenana'
]
for lenana in sorted(lenanas):
    print(lenana)