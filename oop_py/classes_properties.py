class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError('Missing name')
        self.name = name
        self.house = house
    #displays a str as output
    def __str__(self):
        return f'{self.name}: {self.house}'
    #getter
    @property
    def house(self):
        return self._house

    #setter
    @house.setter
    def house(self, house):
        if not house or house not in ['Nelion', 'Lenana', 'Batian', 'Sendeyo']:
            raise ValueError(f'{house} house is Invalid')
        self._house = house

   
def main():
    student = get_student()
    #trying to modify house will result to a Value error as per line18
    student.house = 'Bijiwe'
    print(student)

def get_student():
    name = input('Name: ')
    house = input('House: ')

    return Student(name, house)
if __name__ == "__main__":
    main()