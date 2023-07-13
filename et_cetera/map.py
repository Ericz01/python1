def main():
    yell('This', 'is', 'Eric')

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == '__main__':
    main()