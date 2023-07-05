import re

def main():
    print(convert(input('Hours: ')))

def convert(s):
    #assign the regex to match and evaluate it using walrus operator
    if matches := re.search(r'^([0-9][0-2]*):?([0-5][0-9]*)? (AM|PM){1} to ([0-9][0-2]*):?([0-5][0-9]*)? (AM|PM){1}$', s):
        split_time = matches.groups()
        if int(split_time[0]) > 12 or int(split_time[3]) > 12:
            raise ValueError
        #display from and to times
        from_time = time_format(split_time[0], split_time[1], split_time[2])
        to_time = time_format(split_time[3], split_time[4], split_time[5])
        return from_time + ' to ' + to_time
    #if the input entered does not match
    else:
        raise ValueError
#This function re-does the time format and returns the new time format. 
def time_format(hr, min, period):
    if period == 'PM':
        if int(hr) == 12:
            hr1 = 12
        else:
            hr1 = int(hr) + 12
    else:
        if int(hr) == 12:
            hr1 = 0
        else:
            hr1 = int(hr)
    if min == None:
        min1 = ':00'
        time1 = f'{hr1:02}'+ min1
    else:
        time1 = f'{hr1:02}' + ':' + min
    return time1
if __name__ == "__main__":
    main()