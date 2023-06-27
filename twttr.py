def main():
    string = input('Input: ')
    print(shorten(string))
def shorten(word):
    output = ""
    for i in word:
        if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
            i = ''
            output += i
        else:
            output += i
    return output

if __name__ == "__main__":
    main()
