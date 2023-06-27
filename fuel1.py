def main():
        percentage = convert()
        gauge(percentage)
#expects a str as X/Y all integers. Returns the result as %ge rounded to int.
#if x or y not int or x > y, convert should raise valueError
#if y is 0, raise ZeroDivisionError
def convert():
    while True:
        fraction = input('Fraction: ').split('/')
        try:
            percent = (int(fraction[0]) / int(fraction[1])) * 100
            return percent
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        
#expects an int and returns a str, ie:
    #'E' if the int is less or equal to 1
    #'F' if te int >= 99
    #else 'Z%', where z is the int's percent
def gauge(percentage):
    if percentage <= 1:
        print('E')
        return('E')
    elif percentage >= 99 and percentage <= 100:
        print('F')
        return('F')
    elif percentage > 100:
        convert()
    else:
        print(f'{percentage:.0f}%')
        return(f'{percentage:.0f}%')
if __name__ == "__main__":
    main()
    
