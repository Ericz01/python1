import sys

#one CL arg of an existent file ending with .py. Else, exit via sys.exit
if len(sys.argv) < 2:
    print('Too few command line arguments')
    sys.exit(1)
elif len(sys.argv) > 2:
    print('Too many command-line arguments')
    sys.exit(2)
codeFile = sys.argv[1]
line_count = 0
try:
    py_check = codeFile.split('.')
    if py_check[len(py_check) - 1] != 'py':
        print('Not a Python file')
        sys.exit(3)
    with open(codeFile) as file:
        lines = file.readlines()
    for line in lines:
        if line.lstrip().startswith('#'):
            continue
        elif line.strip() == '':
            continue
        else:
            line_count+=1
except FileNotFoundError:
    print('File does not exist')
    sys.exit(4)
#print line count:
print(line_count)
