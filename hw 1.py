'''
CS 122 Spring 2023 Project 2-2
Author(s): Alexia Crawford
Credit: N/A
Description: Python functions; minimum payment function
'''

def max_trans1(a,b,c):
     print(min(a,b,c)) # input values for a,b,c in shell
    
    
def max_trans2(a,b,c,d,e):
    group1 = min(a,b,c)
    group2 = min(d,e)
    print(max(group1,group2)) # input values for a,b,c,d,e in shell
    

import math
def payment(balance):
    min_payment1 = balance * .021 # *.021 because it is 2.1% of the balance
    min_payment2 = 10 # 10 = $10 charge
    payment = max(min_payment1, min_payment2) # need maximum to charge grater value
    payment = math.ceil(payment) # rounds to nearest integer
    print('minimum payment for balance is $', payment)

    
