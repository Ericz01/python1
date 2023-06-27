name = input('Name: ')

with open('names.txt', 'a') as file:
    file.write(f'{name}\n')
