# PROJECT.PY
#### Video Demo: https://youtu.be/xHT29rQoL_g
#### Description:
This is **SafeLock**, a safe lock for passwords that belong to all the websites the user is registered to, accompanied by their respective usernames. This program solves the problem of having to save these paswords to one's browser which poses a risk when an unathorized individual gains access to ones device as this means unlimited access to any website.

SafeLock is developed using Python language and hence we are assured of it's compatibility with majority of devices. It includes the use of python library(Sys, Re and Csv) as well as third party libraries Pandas and Tabulate. The user must log in using their credentials in order to access the information stored. For new users, the program checks whether the username exists and if not, the user is asked to sign up using a unique username and a password that is rejected if not strong enough.

#### Installing and Running SafeLock
The program is run via the command line. It comes with a single file, **Project.py**. When run, it creates two additional csv files: __Verify.csv__ which verifies the user and __information.csv__ which stores the user's website information.
__Project.py__ has 12 functions, excluding __main__. These functions are implemented in user verification user's data archiving.

#### How to Use the Program
To use SafeLock, one has to sighn up for an account or log in if the account already exists. When this stage is successful, the program opens to a menu that helps the user navigate to different sections of the project. These include adding up a website info, viewing, editing and deleting. The program gives the user tips on how to use it and results to re-prompts where the user fails to use it as explained. 

#### Files
The program comes with the main file that contains the main function and all the other functions.
Upon execution, it creates two additional csv files that store user's data and user's added information. The program hence should be run in an IDE that supports real-time operation on csv files.

#### Tests
The program comes with a unit test file that is implemented via pytest. It tests three of functions as per below:

#### test_validate_password():
    '''Tests the validate_password function.'''
    assert validate_password('passw0rd') == 'password must contain at least one uppercase letter.'
    assert validate_password('password') == 'password must contain at least one digit.'
    assert validate_password('P@ssw0rd') == 'Password is valid.'

#### test_suggest_password():
    '''Tests the suggest_password function.'''
    assert suggest_password('P@ss3') == 'Make your password at least 8 characters long.'
    assert suggest_password('password') == 'Add at least one digit to your password. Include at least one uppercase letter in your password. Include at least one special character in your password (e.g. ?!@#$%).'
    assert suggest_password('P@ssw0rd') == 'Valid password'

#### test_add_information():
    '''Tests the add_information function'''
    information = {'site':'Hogwarts.com', 'username':'Harry', 'password':'P@ssword123'}
    assert add_information(information) == 0
     