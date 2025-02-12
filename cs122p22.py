'''
CS 122 Spring 2023 Project 2-2
Author(s): Alexia Crawford
Credit: N/A
Description: Python functions; minimum payment function
'''

import math
def payment(balance):
    min_payment1 = balance * .021 # *.021 because it is 2.1% of the balance
    min_payment2 = 10 # 10 = $10 charge
    payment = max(min_payment1, min_payment2) # need maximum to charge grater value
    payment = math.ceil(payment) # rounds to nearest integer
    if max(10, balance*.021) > balance:
        print('minimum payment for balance is $', balance)
    print('minimum payment for balance is $', payment)

    
