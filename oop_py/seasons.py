from datetime import date
import sys
import inflect

words = inflect.engine()

def main():
    print(minutes(input('Date of Birth: ')))

def minutes(s):
    try:
        year, month, day = s.split('-')
        date_of_birth = date(int(year), int(month), int(day))
    except:
        sys.exit('Invalid date')
    current_date = date.today()
    diff = current_date - date_of_birth
    return words.number_to_words((diff.days) * 1440, andword='').capitalize() + ' minutes'


if __name__ == "__main__":
    main()