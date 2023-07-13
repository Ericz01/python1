class Student:
    def __init__(self, name, house, animal):
        if not name:
            raise ValueError('Missing name')
        if not house or house not in ['Nelion', 'Lenana', 'Batian', 'Sendeyo']:
            raise ValueError(f'{house} house is Invalid')
        self.name = name
        self.house = house
        self.animal = animal
    #displays a str as output
    def __str__(self):
        return f'{self.name}: {self.house}'
    #own function
    def patronus(self):
        match self.animal:
            case 'Cheetah':
                return 'grrrrr'
            case 'Lion':
                return 'rooaaarr'
            case 'Hyena':
                return 'haaaaaha'
            case _:
                return '......'

def main():
    student = get_student()

    print(student.name)
    print(student.patronus())

def get_student():
    name = input('Name: ')
    house = input('House: ')
    animal = input('Animal: ')

    return Student(name, house, animal)
if __name__ == "__main__":
    main()