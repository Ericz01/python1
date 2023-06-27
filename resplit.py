import re
m = input('Plates: ')
m1 = re.split('(\d.*)', m)
for c in m1[-2]:
    if c.isalpha():
        print(m1[1])
