'''
CS 122 Spring 2023 Project 4-1 Magic 8-Ball
Author: Alexia Crawford
Credit: N/A
Description: create algorithm that plays the game fizzbuzz
'''
def fizzbuzz(x):
    ''' fucntion creates number pattern. If number is perfectly divisble by 3
        it will print fizz, if perfectly divisible by 5 it will print buzz.
        if perfectly divisble by 3 and 5 it will print fizzbuzz.

        >>>fizzbuzz(5)
        [1,2,fizz,4,buzz]
        '''
    for n in range(1, x+1):
        if n % 3 == 0 and n % 5 == 0:
            print('fizzbuzz')
        elif n % 3 == 0:
            print('fizz')
        elif n % 5 == 0:
            print('buzz')
        else:
            print(n)
    print('Well done!')

    return

def main():
    '''top level function'''

    #ask user how high they want the game to go
    x = int(input('please enter a positive integer to start fizzbuzz game'))
    #call fizzbuzz until it reaches integer entered
    fizzbuzz(x)

    return

main()
