from project import validate_password, suggest_password, add_information

def test_validate_password():
    '''Tests the validate_password function.'''
    assert validate_password('passw0rd') == 'password must contain at least one uppercase letter.'
    assert validate_password('password') == 'password must contain at least one digit.'
    assert validate_password('P@ssw0rd') == 'Password is valid.'

def test_suggest_password():
    '''Tests the suggest_password function.'''
    assert suggest_password('P@ss3') == 'Make your password at least 8 characters long.'
    assert suggest_password('password') == 'Add at least one digit to your password. Include at least one uppercase letter in your password. Include at least one special character in your password (e.g. ?!@#$%).'
    assert suggest_password('P@ssw0rd') == 'Valid password'

def test_add_information():
    '''Tests the add_information function'''
    information = {'site':'google.com', 'username':'Eric', 'password':'P@ssword123'}
    assert add_information(information) == 0
    