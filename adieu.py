import inflect
p = inflect.engine()
list = []
for i in range(0, 3):
    print(f'Item {i}: ', end = ' ')
    item = input()
    list.append(item)
print('List: ', list)
