class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError('Missing name')
        if not house or house not in ['Nelion', 'Lenana', 'Batian', 'Sendeyo']:
            raise ValueError(f'{house} house is Invalid')
        self.name = name
        self.house = house

def main():
    student = get_student()
    if student.name == 'Eric':
        student.house = 'Lenana'

    print(f'{student.name}: {student.house}')

def get_student():
    name = input('Name: ')
    house = input('House: ')

    return Student(name, house)
if __name__ == "__main__":
    main()