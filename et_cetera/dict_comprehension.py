students = ['Eric', 'Roy', 'Job']

#lenanas = [{'name': student, 'house': 'Lenana'} for student in students]
lenanas = {student: 'Lenana' for student in students}
print(lenanas)