def main():
    student = get_student()
    if student['name'] == 'Eric':
        student['house'] = 'Lenana'

    print(f'{student["name"]}: {student["house"]}')

def get_student():
    name = input('Name: ')
    house = input('House: ')

    return {'name':name, 'house':house}
if __name__ == "__main__":
    main()