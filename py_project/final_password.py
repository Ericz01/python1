import re
import random
import string
import secrets

MINI_LENGTH = 8
PASSWORD_SUGGESTIONS = 3
MAX_LENGTH = 20

def main():
    users_password = input('Password: ')

    if validate(users_password) == True:
        print('Password validated')
    if not users_password:
        empty_string('users_password')
def validate(s):
    matches = re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$', s)
    if matches:
        return True

def empty_string(s):
    alpha = string.ascii_letters
    digits = string.digits
    punctuation  = string.punctuation
    raw_password = alpha + digits + punctuation
    generated_password = ''
    print('Empty password. You may like one of these:')
    for i in range(PASSWORD_SUGGESTIONS):
        for _ in range(MINI_LENGTH):
            generated_password += ''.join(secrets.choice(raw_password))
        print(generated_password)
        generated_password = ''
'''''
        else:        
            regex2 = re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]+$', s)
            if regex2:
                if len(s) >  MAX_LENGTH:
                    #where password is too long, cut the extra characters
                    recommended_length = len(s) - MAX_LENGTH
                    generated_password = s[:20]
                    print('Your password is too long. Try this:')
                    print(generated_password)
                elif len(s)  < 8:
                    #short password
                    recommended_length = MINI_LENGTH - len(s)
                    generated_password = s 
                    print('Your password is too short. You may like one of these:')
                    for i in range(PASSWORD_SUGGESTIONS):
                        for _ in range(recommended_length):
                            generated_password += ''.join(secrets.choice(raw_password))
                        print(generated_password)
                        generated_password = s
            else:
                upper = ''
                lower = ''
                symbol = ''
                digit = ''
                for char in range(len(s)):
                    if s[char].isupper():
                        upper += s[char]
                    elif s[char].islower():
                        lower += s[char]
                    elif s[char].isdigit():
                        digit += s[char]
                    else:
                        symbol += s[char]
                if symbol:
                    if lower:
                        if digit: 
                            if not upper:
                                print('Password must contain at least one uppercase character. Try any of these:')
                                for _ in range(PASSWORD_SUGGESTIONS):
                                    print(s + random.choice(string.ascii_uppercase))
                elif symbol:
                    if digit:
                        if upper:
                            if not lower:
                                print('Password must contain at least one lowercase character. Try any of these:')
                                for _ in range(PASSWORD_SUGGESTIONS):
                                    print(s + random.choice(string.ascii_lowercase))
                elif symbol:
                    if upper:
                        if lower:
                            if not digit:
                                print('Password must contain at least one digit. Try any of these:')
                                for _ in range(PASSWORD_SUGGESTIONS):
                                    print(s + random.choice(string.digits))
                elif upper:
                    if lower:
                        if digit:
                            if not symbol:
                                print('Password must contain at least one special character. Try any of these:')
                                for _ in range(PASSWORD_SUGGESTIONS):
                                    print(s + random.choice(string.punctuation))
                else:
                    recommended_length = 12
                    generated_password = s 
                    print('Your password is invalid. You may like one of these:')
                    for i in range(PASSWORD_SUGGESTIONS):
                        for _ in range(recommended_length):
                            generated_password += ''.join(secrets.choice(raw_password))
                        print(generated_password)
                        generated_password = s
                        '''
if __name__ == '__main__':
    main()