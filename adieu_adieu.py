import inflect
p = inflect.engine()

list = []
while True:
    try:
        name = input('Name: ')
        list.append(name)
    except EOFError:
        list1 = p.join((list), final_sep = '')
        print(f'Adieu, adieu, to {list1}')
        break
