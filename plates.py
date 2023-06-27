def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):
    #checking length of plate
    if len(s) < 2 or len(s) > 6:
        return False
    #first two elements must be letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    #the first number cannot be '0'
    i = 0
    while i < len(s):
        if s[i].isdigit():
            index = s.index(s[i])
            if s[i] == '0' and s[index:].isdigit():
                return False
            else:
                break
        i += 1

    #elements are numeric and alpha only
    for i in s:
        if i.isalnum() == False:
            return False

    #return true if all above is met
    return True

if __name__ == "__main__":
    main()
