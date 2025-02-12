'''
CS 122 Spring 2023 Project 3-1
Author(s): Alexia Crawford
Credit: N/A
Description: Intro to Python Turtle Graphics
'''
from turtle import*
def poly (num_sides, side_len, pcolor):

    '''
    function poly should use turtle commands to draw any polygon
    filled with color at turtles current position

    >>> poly(5, 100, 'purple')
    [five sided polygon with side lengths 100 filled purple]

    '''
    setheading(180)
    fillcolor(pcolor)
    begin_fill()
    for n in range (num_sides):
        print(n)
        fd(side_len)
        rt(360 / num_sides)
    end_fill()
    return

def jump(x, y):
 '''aux function sets turtle position
 without leaving pen trail
 >>> jump(100, 100)
 [turtle positioned at 100, 100]
 '''
 penup()
 setposition(x, y)
 pendown()
 return

def house():
    '''
    print poly and jump to draw a house
    '''
    jump(-50, -150)
    poly(4, 100, 'green')
    jump(-50,-50)
    poly(3, 100, 'yellow')
    return

        
    

