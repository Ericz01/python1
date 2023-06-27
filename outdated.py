#Programs to convert traditional date formats to computer recognized formats
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]
while True:
    try:
        #for '/' separated dates
        date = input('Date: ')
        month1, day1, year1 = date.split('/')
        if (int(month1) > 0) and (int(month1) <= 12):
            if (int(day1) > 0) and (int(day1) <= 31):
                break
    #space separated and invalid dates
    except:
        try:
            #split by space and change date[1] to its index
            month, day, year1 = date.split(' ')
            for i in range(len(months)):
                if month == months[i]:
                    month1 = i + 1
            #removing comma
            day1 = day.replace(',', '')
            if (int(month1) > 0) and (int(month1) <=12):
                if (int(day1) > 0) and (int(day1) <= 31):
                    break
        #go to the next lline
        except:
            print()
            pass
#print the formatted date
print(f'{year1}-{int(month1):02}-{int(day1):02}')
