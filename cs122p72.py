'''
CS 122 Spring 2023 Project 7-2
Author: Alexia Crawford  
Credits: N/A
create a secure password checker using strings and loops
'''
import doctest

def minimum_length(password: str) -> str:
    '''
    checks if password length is at least 5 characters
    >>> minimum_length('sam')
    False
    '''
    return len(password) >= 5

def character_check(password: str) -> str:
    '''
    checks to see if password contains e or E
    >>> character_check('hello')
    False
    >>> character_check('sammy')
    True
    '''
    for i in range (len(password)):
        if 'e' in password or 'E' in password:
            return False
        else:
            return True
    
def special_character(password: str) -> str:
    '''
    checks if password includes ! or @ or # or $ (password must include at least one of them)
    >>> special_character('sam!')
    True
    >>> special_character('sam')
    False
    '''
    for i in range (len(password)):
        if '!' in password or '@' in password or '#' in password or '$' in password:
            return True
        else:
            return False
        
def digit_check(password: str) -> str:
    '''
    checks if password contains at least two numbers
    >>> digit_check('sam67')
    True
    >>> digit_check('sam6')
    False
    '''
    digit = '0 1 2 3 4 5 6 7 8 9'

    count = 0
    for c in password:
        if c in digit:
            count += 1

    if count >= 2:
        return True
    else:
        return False

     
def password_check(password: str) -> str:
    '''
    Checks if the password contains all above requirements
    >>> password_check('sam67!')
    True
    '''
    if minimum_length(password) and character_check(password) and special_character(password) and digit_check(password):
        return True
    else:
        return False
    
    
def main():
    '''
    Calls password check and asks user to input a password. If the password is not secure it asks
    user to enter another password
    '''
    flag = True
    while flag:
        password = input('Please choose a password: ')
        secure = password_check(password)
        if secure:
            return print('This password is secure.')
        else:
            print ('Password is not secure. Try another password.')
            return main()

print(doctest.testmod())

main()

