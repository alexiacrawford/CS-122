'''
CS 122 Spring 2023
Author: Alexia Crawford
Description: wordle helper - intro to opeing files
'''
import doctest
def report(word_ctr, wordle_ctr):
    '''
    will report the amount of words in the file and total number
    of words that match criteria

    >>> report (12, 4)
    The total number of words is 12
    The total number of good words is 4
    '''
    print('The total number of words is', word_ctr) #total words in file
    print('The total number of good words is', wordle_ctr) #total good words
    return


def vowel_ctr(word: str) -> str:
    '''
    Counts how many different vowels are in a word
    >>> vowel_ctr('banana')
    1
    '''
    vowel = 'a e i o u y'
    count = 0
    duplicate = '' #looks for duplicate vowels
    for c in word:
        if c in vowel:
            if c not in duplicate:
                count += 1
                duplicate += c
                
    return count

def wordle_helper(fname, vowels, verbose):
    '''
    (fname:str) -> str:
    opens files and uses vowel_ctr and report to locate
    words that match all the criteria

    >>> wordle_helper('words_short.txt', 3, True)
    helpful initial guess words
    babbitted
    <BLANKLINE>
    The total number of words is 30
    The total number of good words is 1

    >>> wordle_helper('words_short.txt', 5, False)
    helpful initial guess words
    The total number of words is 30
    The total number of good words is 0
    '''
    word_ctr = 0
    wordle_ctr = 0
    with open (fname) as f:
        print('helpful initial guess words')
        f.readline() #skips first line to read rest of file
        for words in f:
            word_ctr += 1
            if vowel_ctr(words) == vowels:
                wordle_ctr += 1
                if verbose == True:
                    print(words)
                    
        report(word_ctr,wordle_ctr)

    return

    
def main():
    '''wordle helper program driver'''
    wordle_helper('words_short.txt', 2, True)

    return

#print(doctest.testmod())
main()





