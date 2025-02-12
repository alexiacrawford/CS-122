'''
CS 122 Spring 2023 Project 6-1
Twenty-one Card game
Author: Alexia Crawford
Credits: N/A
Description: coding a card game
'''
import random
import doctest
def draw_card():
    ''' will randomly generate a number to be added to total
    >>>draw_card()
    9
    '''
    n = random.randint(1, 10)
    return n

def report(card_ct_ttl):
    ''' reports total card count
    >>>report()
    9
    16
    21
    '''
    if card_ct_ttl > 21:
        print ('you lose')
    else:
        print ('you win!')
    return

def play_21():
    '''
    displays card count total and asks player to play
    >>>play_21()
    would you like to draw a card (y or n)?
    8
    would you like to draw another card (y or n)?
    '''
    total = 0
    play = 'y'
    while play == 'y':
        card = draw_card()
        total += card
        print (total)
        if total < 21:
            play = input ('would you like to draw another card (y or n)? ')
            if play == 'n':
                print ('game over')
                break
        elif total > 21:
            break
    return total
def main():
    '''driver'''
    print ('welcome to 21')
    play = input ('would you like to play a round (y or n)? ')
    while play == 'y':
        card_ct_ttl = play_21()
        report(card_ct_ttl)
        play = input ('would you like to play a round (y or n)? ')
    return
main()
