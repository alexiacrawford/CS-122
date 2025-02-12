'''
CS 122 Spring 2023 Project 7-1
Author(s): Alexia Crawford
Credit: N/A
Description: transcribe DNA to RNA
'''
def transcribe(DNA: str) -> str:
    '''
    >>> transcribe('ACGT TGCA')
    'UGCAACGU'
    >>> transcribe('GATTACA')
    'CUAAUGU'
    >>> transcribe('GAtTtTACA')
    'CUAAUGU'
    >>> transcribe('TTt ACT')
    'AAUGA'
    >>> transcribe('cs5')
    ''
    '''
    RNA = ''
    for i in range(len(DNA)):
        if DNA[i] == 'A':
            RNA += 'U'
        elif DNA[i] == 'C':
            RNA += 'G'
        elif DNA[i] == 'G':
            RNA += 'C'
        elif DNA[i] == 'T':
            RNA += 'A'
        else:
            RNA += ''
    return RNA

def transcribe_alt(DNA: str) -> str:
    '''
    >>> transcribe('ACGT TGCA')
    'UGCAACGU'
    >>> transcribe('GATTACA')
    'CUAAUGU'
    >>> transcribe('GAtTtTACA')
    'CUAAUGU'
    >>> transcribe('TTt ACT')
    'AAUGA'
    >>> transcribe('cs5')
    ''
    '''
    while True:
        
        RNA = ''
        for i in range(len(DNA)):
            if DNA[i] == 'A':
                RNA += 'U'
            elif DNA[i] == 'C':
                RNA += 'G'
            elif DNA[i] == 'G':
                RNA += 'C'
            elif DNA[i] == 'T':
                RNA += 'A'
            else:
                RNA += ''

        break
    return RNA

#It is better to use the for loop for this because the while loop is just the for loop but uses more code
          


    
