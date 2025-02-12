'''
CS 122 Spring 2023 Project 3-2
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



def sun():
    '''
    draw sun and rays at position without pen trail
    >>>sun()
    '''
    speed(10)
    jump(100,200)
    pencolor('yellow')
    fillcolor('yellow')
    begin_fill()
    circle(25)
    end_fill()
    jump(100,175)
    for s in range (36):
        print(s)
        pencolor('yellow')
        rt(10)
        fd(100)
        bk(100)
    return

def house():
    '''
    draw house from poly funciton at specific position
    draw square, jump, triangle
    ''' 
    jump(-50, -150)
    poly(4, 100, 'green')
    jump(-50,-50)
    poly(3, 100, 'yellow')
    return

def tree():
    '''
    draw tree at specific position
    wihtout pen trail
    >>>tree()
    ''' 
    pencolor('brown')
    fillcolor('brown')
    begin_fill()
    jump(100,-150)
    for t in range (2):
        print(t)
        fd(30)
        rt(90)
        fd(100)
        rt(90)
    end_fill()
    pencolor('green')
    fillcolor('green')
    begin_fill()
    jump(85,30)
    circle(50)
    end_fill()
    return

def art_show_main():
    '''
    print all previous functions in their
    designated spots
    ''' 
    house()
    sun()
    tree()
    return
    
