due = 50
change = 0
print(f'Amount due: {due}')
while True:
    try:
        coin = int(input('Insert coin: '))
        if coin == 25 or coin == 10 or coin == 5:
            due -= coin
            if due > 0:
                print(f'Amount due: {due}')

            elif due <= 0:
                print(f'Change owed: {change - due}')
                break
        else:
            print(f'Amount due: {due}')
    except ValueError:
        print(f'Amount due: {due}')
        
