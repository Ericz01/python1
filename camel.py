camel = input('camelCase: ')
snake_case = ""
for c in camel:
    if c.isupper():
        snake_case += '_'
        snake_case += c
    else:
        snake_case += c
print(f'Snake_case: {snake_case.lower()}')
