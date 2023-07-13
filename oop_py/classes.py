class Student:
    ...

def main():
    student = get_student()
    if student.name == 'Eric':
        student.house = 'Lenana'

    print(f'{student.name}: {student.house}')

def get_student():
    student = Student()
    student.name = input('Name: ')
    student.house = input('House: ')

    return student
if __name__ == "__main__":
    main()