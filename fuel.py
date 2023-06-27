def main():
    fraction = input('Fraction: ')
    new_fraction = convert(fraction)
    result = gauge(new_fraction)
    print(result)
#expects a str as X/Y all integers. Returns the result as %ge rounded to int.
def convert(fraction):
    while True:
        try:
            fraction = fraction.split('/')
            percent = (int(fraction[0]) / int(fraction[1])) * 100
            if percent <= 100:
                return percent
            else:
                fraction = input('Fraction: ').split('/')
                pass
        except (ValueError, ZeroDivisionError):
            raise
        
#expects an int and returns a str
def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99 and percentage <= 100:
        return 'F'
    else:
        return(f'{percentage:.0f}%')
if __name__ == "__main__":
    main()
    
