import re

email = input('Email: ')

if re.search(r'.+@.+\.com', email):
    print('Valid')
else:
    print('invalid')