expr = input('Expression: ').split()
x = float(expr[0])
y = float(expr[2])
if expr[1] == '+':
    print(x + y)
elif expr[1] == '-':
    print(x - y)
elif expr[1] == '/':
    print(f'{(x / y):.1f}')
elif expr[1] == '*':
    print(x * y)
elif expr[1] == '%':
    print(x % y)
