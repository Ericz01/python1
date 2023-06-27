while True:
    
    fraction = input('Fraction: ').split('/')
    try:
        percent = (int(fraction[0]) / int(fraction[1])) * 100
        if percent <= 1:
            print('E')
        elif percent >= 99:
            print('F')
        else:
            print(f'{percent:.0f}%')
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
