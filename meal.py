def main():
    converted = input('What is the time? ')
    time = convert(converted)
    if time >= 7.0 and time <= 8.0:
        print('Breakfast time')
    elif time >= 12.0 and time <= 13.0:
        print('Lunch time')
    elif time >= 18.0 and time <= 19.0:
        print('Dinner time')

def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)/60.0
    return hours + minutes
if __name__ == "__main__":
    main()
