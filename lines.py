import sys
def main():
    line_count = validate()
    print(line_count)
def validate():
    line_count = 0
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if '.py' not in sys.argv[1]:
        sys.exit('Not a Python file')
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
        for line in lines:
            if line.lstrip().startswith('#'):
                continue
            elif line.lstrip() == '':
                continue
            else:
                line_count += 1
        return line_count
    except FileNotFoundError:
        sys.exit('File does not exist')

if  __name__ == "__main__":
    main()
