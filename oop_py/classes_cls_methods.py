import random

class Hat:
    houses = ['Lenana', 'Nelion', 'Sendeyo', 'Batian']

    @classmethod
    def sort(cls, name):
        print(name, 'is in', random.choice(cls.houses))
Hat.sort(input('Name: '))