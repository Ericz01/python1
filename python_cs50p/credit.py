import re

def main():
    #4003600000000014
    while True:
        try:
            credit_number = input('Number: ')
            print(validate(credit_number))
            break
        except ValueError:
            pass
def validate(number):
    checksum = 0
    reverse_number = number[::-1]#reversing the strin of input number
    checksum1 = reverse_number[1:len(reverse_number):2]#get numbers from second-last as string
    checksum2 = reverse_number[0:len(reverse_number):2]#get the other numbers
    #get sum of numbers
    for i in checksum1:
        if int(i) < 5:
            checksum += int(i)*2
        elif int(i) >= 5:
            i = int(i) * 2
            i = str(i)
            checksum += (int(i[0]) + int(i[1]))
    for i in checksum2:
        checksum += int(i)
    if (checksum % 10)  == 0:
        #assert if it's visa
        if re.search(r'^4\d{12}(?:\d{3})?$', number):
            return 'VISA'
        #American Express
        elif re.search(r'^34|37\d{13}$', number):
            return 'AMEX'
        #Mastercard
        elif re.search(r'^51|52|53|54|55\d{14}$', number):
            return 'MASTERCARD'
    return 'INVALID'
if __name__ == '__main__':
    main()