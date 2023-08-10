import re
import csv

MINI_LENGTH = 8
MAX_LENGTH = 20

def logging_in():
    logins = {}
    username1 = input('Enter username: ')
    while True:
        password1 = input('Enter password: ')
        logins = {'username1':username1, 'password1':password1} 
        result = validate_password1(password1)
    
        if result != 'Password is valid.':
            print(result)
            print(suggest_password1(password1))
        else:
            put(username1, logins)
            break
def validate_password1(password1):
    '''
    #Validates a password and gives tips for improving it if it's invalid
    '''
    if len(password1) < MINI_LENGTH:
        return 'password must be at least 8 characters long.'
    if len(password1) > MAX_LENGTH:
        return 'Your password is too long'
    if not re.search(r'\d', password1):
        return 'password must contain at least one digit.'
    if not re.search(r'[A-Z]', password1):
        return 'password must contain at least one uppercase letter.'
    if not re.search(r'[a-z]', password1):
        return 'password must contain at least one lowercase letter.'
    if not re.search(r'\W|_', password1):
        return 'password must contain at least one special character.'
    return 'Password is valid.'

def suggest_password1(password1):
    '''Provides suggestions to improve a password.'''
    suggestions = []
    if len(password1) < 8:
        suggestions.append('Make your password at least 8 characters long.')
    if len(password1) > 20:
        suggestions.append('password should have a maximum length of 20')
    if not re.search(r'\d', password1):
        suggestions.append('Add at least one digit to your password.')
    if not re.search(r'[A-Z]', password1):
        suggestions.append('Include at least one uppercase letter in your password.')
    if not re.search(r'[a-z]', password1):
        suggestions.append('Include at least one lowercase letter in your password.')
    if not re.search(r'\W|_', password1):
        suggestions.append('Include at least one special character in your password (e.g. ?!@#$%)<.;')

    if suggestions:
        return ' '.join(suggestions)
    
    return 'Valid password1'

def add_logins(logins):
    with open('verify.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=logins.keys())
        writer.writerow(logins)
def put(username1, logins):
    verification_list = []
    with open('verify.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username1'] == username1:
                verification_list.append(row)
    if len(verification_list):
        choice = input(f'{username1} exists. Press "Enter" to log in or "Q" to quit').lower()
        if choice == 'q':
            sys.exit()
    else:
        add_logins(logins)