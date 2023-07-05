import re
import sys

def main():
    print(convert(input('Hours: ')))

def convert(s):
    if matches := re.search(r'^([0-9][0-2]*):?([0-5][0-9]*)? (AM|PM){1} to ([0-9][0-2]*):?([0-5][0-9]*)? (AM|PM){1}$', s):

        if matches.group(3) == 'PM':
                if int(matches.group(1)) == 12:
                    hour = 12
                else:
                    hour = int(matches.group(1)) + 12
        elif matches.group(3) == 'AM':
            if int(matches.group(1)) == 12:
                hour = 0
            else:
                hour = int(matches.group(1))
        if matches.group(6) == 'PM':
            if int(matches.group(4)) == 12:
                hour2 = 12
            else:
                hour2 = int(matches.group) + 12
        elif matches.group(6) == 'AM':
            if int(matches.group(4)) == 12:
                hour2 = 0
            else:
                hour2 = int(matches.group(4))
        if matches.group(2) == None:
            minute = ':00'
            time = f'{hour:02}' + minute
        elif int(matches.group(2)) < 59:
            minute = matches.group(2)
            time = f'{hour:02}:' + minute
        if matches.group(5) == None:
            minute2 = ':00'
            time2 = f'{hour2:02}' + minute2
        elif int(matches.group(5)) < 60:
            minute2 = matches.group(5)
            time2 = f'{hour2:02}:' + minute2
        return time + ' to ' + time2
    else:
        raise ValueError

if __name__ == "__main__":
    main()