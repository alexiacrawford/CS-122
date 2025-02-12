'''
CS 122 Spring 2023 Project 6-2
Author: Alexia Crawford
Credits: N/A
Description: testing and debugging 
'''

####
#(1) CHECK END DIGITS 
####
def check_end_digits(n):
    '''(n: int) -> bool

    [4 bugs]

    boolean function returns True when the first and last
    digits of n, a 3-digit positive integer, are different
    (100s column digit and unit column digit) 

    >>> check_end_digits(100)
    True
    >>> check_end_digits(101)
    False
    '''
    # units digit
    right = n % 10 #bug 1: where % is was a $ so I changed it to %

    # hundreds column digit
    left = n // 10
    left = left // 10 #bug 4: // left by 10 to get to ones
    if right != left: #bug 2: r and l not defined,change to right and left
        return True
    else:
        return False
    #bug 3: I removed ''' from around the if else statement
    return right == left

####
#(2) MINUTES TO YEARS
####
def minutesToHours(minutes): 
    '''(minutes: number) -> float

    [1 bug]

    called by: minutesToYears

    convert input minutes to hours;
    return hours

    >>> minutesToHours(60)
    1.0
    '''
    hours = minutes / 60
    hours = round(hours, 2)
    return hours #should return instead of print hours
                      
    
def hoursToDays(hours): 
    '''(hours: int) -> float

    [1 bug]

    called by: minutesToYears
    
    convert input hours to days;
    return days

    >>> hoursToDays(24)
    1.0
    >>> hoursToDays(30)
    1.42
    '''
    days = hours / 24
    days = round (days, 2) #round so we dont get weird decimal values
    return days

def daysToYears(days):
    '''(days: int) -> float

    [1 bug]

    called by: minutesToYears

    convert input days to years;
    return years

    >>> daysToYears(365)
    1.0
    '''
    # days us not needed
    years = days / 365
    years = round(years, 2)
    return years

def minutesToYears(m):
    '''(m: int) -> float

    [3 bugs]

    calls: minutesToHours, hoursToDays, daysToYears

    input number m minutes is converted to
    equivalent number of years. return years.
    call auxiliary functions to do each step

    >>> minutesToYears(525600)
    1.0
    '''
    # we need to define the variables
    h = minutesToHours(m)   
    d = hoursToDays(h)      
    y = daysToYears(d)

    minutesToHours(m)
    hoursToDays(h)
    daysToYears(d)
    return y

# print(doctest.testmod())


####
#(3) RAT WEIGHT
#### 
def rats(weight, p):
    '''(weight: float, p: float) -> None

    [3 bugs]
    
    Print number of weeks it will
    take for a rat to weigh 2 times
    as much as its original weight
    (weight) if it gains weight at
    rate p percent per week.

    >>> rats(10, 10)
    The rat weighs 21.4 after 8 weeks.
    '''
    weeks = 0
    final_weight = 2 * weight #added this line to calculate the final weight
    rate = p * .01
    
    while weight < final_weight: #changed this to variable name
        weight += weight * rate
        weeks = weeks + 1 #wks is not defined, changed name to weeks which is defined
        
    weight = round(weight, 1)
    print(f'The rat weighs {weight} after {weeks} weeks.')
    return
    



