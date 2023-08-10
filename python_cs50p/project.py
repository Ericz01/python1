'''
Websites' Passwords SafeLock
Name: Eric Nyaga
Residence: Nairobi, Kenya
LinkedIn: https://www.linkedin.com/in/eric-nyaga-587846232
'''
import csv
import pandas as pd
import re
import sys
from tabulate import tabulate

MINI_LENGTH = 8
MAX_LENGTH = 20

def logging_in():
    '''
    #Calls the result, put and sugest_password1 functions
    #Accepts no arguments and returns no arguments    
    '''
    logins = {}
    username1 = input('Enter username to sign up or log in: ')
    while True:
        password1 = input('Enter password: ')
        logins = {'username1':username1, 'password1':password1} 
        result = validate_password(password1)
    
        if result != 'Password is valid.':
            print(result)
            print(suggest_password(password1))
        else:
            put(username1, logins)
            print(f'Hello {username1}. Select an activity to proceed to SafeLock:')
            welcome()
def validate_password(password1):
    '''
    :Validates a password and gives tips for improving it if it's invalid
    :Param password1: password to be verified
    :return: tips to improve password as string
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

def suggest_password(password1):
    '''
    :Provides suggestions to improve a password.
    :param password1: password to be verified
    :return: string suggestions
    '''
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
        suggestions.append('Include at least one special character in your password (e.g. ?!@#$%).')

    if suggestions:
        return ' '.join(suggestions)
    
    return 'Valid password'

def add_logins(logins):
    '''Writes the login details to a csv file'''
    with open('verify.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=logins.keys())
        writer.writerow(logins)
def put(username1, logins):
    '''
    :Checks whether user exists for log in or new for sign up
    :param username1: user's username
    :param logins: user's login details
    '''
    verification_list = []
    with open('verify.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username1'] == username1:
                verification_list.append(row)
    if len(verification_list):
        print(f'{username1} username already exists.')
        while True:
            choice = input(f'Press "Enter" to log in or "Q" to quit: ').lower()
            if choice == '':
                password1 = input(f'Enter {username1}\'s password to login: ')
                if password1 == verification_list[0]['password1']:
                    break
                else:
                    print('Wrong password.', end='')
            elif choice == 'q':
                sys.exit()
            else:
                continue
    else:
        add_logins(logins)

def main_frame():
    '''Calls add_information and menu functions'''
    while True:
        site = input('Enter the website\'s name: ').rstrip()
        username = input('Enter the website\'s username: ').rstrip()
        info = []
        with open('information.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Website'] == site and row['Username'] == username:
                    info.append(row)
        if len(info):
            print(f'{site} exists with the same username. View the main menu for more options.')
            break
        else:
            password = input('Enter the website\'s password: ').rstrip()
            information = {'site':site, 'username':username, 'password':password}
            add_information(information)
        menu()

def welcome():
    '''
    :Displays menu
    :calls main_frame, read_information, edit and delete functions
    '''
    print(tabulate({'Key': ['A', 'V', 'E', 'D', 'Q'],
                'Activity': ['Add a website', 'View website information', 'Edit website information', 'Delete website information', 'Quit']}, headers='keys', tablefmt='grid'))
    key_press = input('Enter key: ').lower().rstrip()
    if key_press == 'a':
        main_frame()
    elif key_press == 'v':
        read_information() 
    elif key_press == 'e':
        edit()
    elif key_press == 'd':
        delete()
    elif key_press == 'q':
        sys.exit()
    else:
        print('Invalid key. ', end='')
        menu()

def add_information(information):
    '''Writes added website information to a csv file and returns 0'''
    with open('information.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=information.keys())
        writer.writerow(information)
    print('Website added successfully. Select a key to continue: \n')
    return 0
def read_information():
    '''Reads information contained in information.csv csv file
    :calls menu function
    '''
    view = input('Enter "A" to view all and "S" to view a specific website: ').lower()
    info = []
    with open('information.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            info.append({'website':row['Website'], 'username':row['Username'], 'password':row['Password']})
        if view == 'a':
            print('\nHere\'s a list of websites you are registered to: ')   
            print(tabulate(info, headers='keys', tablefmt='grid'))
        elif view == 's':
            info = []
            website = input('To view a website\'s info, enter the website name: ').lower()
            with open('information.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Website'] == website:
                        info.append(row)
                if info:
                    print((tabulate(info, headers='keys', tablefmt='grid')))
                elif not info:
                    print(f'{website} not in your websites. Select "A" in Main Menu to add it')
    menu()
def delete():
    delete_list = []
    '''Deletes a website and its related information and calls menu function'''
    while True:
        deleted = input('Enter website to delete: ')
        with open('information.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Website'] == deleted:
                    delete_list.append(row)
        if len(delete_list):
            affirm = input(f'Are you sure you want to delete {deleted}? Enter "Y" to delete and "N" to cancel: ').lower()
            if affirm == 'yes' or affirm == 'y':
                df = pd.read_csv('information.csv', index_col='Website')
                df = df.drop(deleted)
                df.to_csv('information.csv', index=True)
                print('Website deleted\n')
                menu()
        else:
            print(f'{deleted} not in your websites list')
            menu()
def edit():
    '''Edits a website's information'''
    web = input('Enter the website to edit: ')
    edit_list = []
    with open('information.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Website'] == web:
                edit_list.append(row)
    if len(edit_list):
        options = input('Enter "U" to edit the website\'s username or "P" to edit password: ').lower()
        while True:
            if options == 'u':
                new_username = input('Enter the new username: ')
                df = pd.read_csv('information.csv')
                df.loc[df['Website'] == web, 'Username'] = new_username
                df.to_csv('information.csv', index=False)
                break
            elif options == 'p':
                new_pass = input('Enter new password: ')
                df = pd.read_csv('information.csv')
                df.loc[df['Website'] == web, 'Password'] = new_pass
                df.to_csv('information.csv', index=False)
                break
            else:
                options = input('Invalid input. Enter "W" to edit the website name, "U" to edit the username or "P" to edit password: ')
        print('Update was successful\n')
    else:
        print(f'{web} not in your websites list.')
    while True:
        menu()
def menu():
    '''Calls welcome function that displays the program's segments and functionalities'''
    while True:
        menu = input('Press Enter to view main menu or "Q" to quit: ').lower()
        if menu == '':
            welcome()
        elif menu == 'q':
            sys.exit()
        else:
            print('Invalid choice. ', end='')
            continue
def main():
    '''Calls all the main functions'''
    logging_in()
    print('Welcome to SafeLock. Select an activity: ')
    information = {}
    welcome()
if __name__ == '__main__':
    main()