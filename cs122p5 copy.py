'''
CS 122 Spring 2023 Project 5
Author(s): Alexia Crawford
Credit: N/A
Description: Einstein's Math Trick
'''
def check_positive_int(n):
    '''
    checks to see if n is positive, will return True or Fl=alse statement
    >>>check_positive_int(4)
    Trues
    '''
    if n > 0:
        return True
    else:
        return False
        
def check_3_digits(n):
    '''
    checks to see if value is three digits
    >>> check_3_digits(123)
    True
    '''
    if n > 99 and n <= 999:
        return True
    else:
        return False

def check_end_digits(n):
    '''
    checks to see if end digit and first digit are the same
    >>> check_end_digits(121)
    False
    '''
    x = n % 10
    y = n // 10
    y = y // 10

    if x != y:
        return True
    else:
        return False

def check_number(n):
    '''
    makes sure number inputted is a valid number
    >>>check_number(167)
    True
    '''
   
    if check_positive_int(n) and check_3_digits(n) and check_end_digits(n):
        return True
    else:
        return False

def reverse(n):
    '''
    takes valid number and reverses it
    >>>reverse(456)
    654
    '''
    ones = n % 10
    tens = n % 100
    tens = tens // 10
    hundreds = n // 100
    sum_digits = hundreds
    sum_digits += tens * 10
    sum_digits += ones * 100
    return sum_digits

def einstein(n):
    '''
    prints your number and all values of previous functions
    '''
    z = reverse(n)
    if z > n:
        x = z - n
    else:
        x = n - z
    y = x + reverse (x)
    print('number is' , n)
    print('reverse is' , reverse(n))
    print('difference is' , x)
    print('the reverse is' , reverse (x))
    return print('your number is...' , y, 'tada!')

def main():
    '''driver for einstein program'''
    
    magic_number = 1089

    n = input('Enter a 3-digit positive number (different 1st and last digits): ')
    n = int(n)
    
    valid_number = check_number(n)
    if not valid_number:
        print('Invalid number')
    else:
        einstein(n)
    
    return

main()
