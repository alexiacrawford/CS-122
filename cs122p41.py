'''
CS 122 Spring 2023 Project 4-1 Magic 8-Ball
Author: Alexia Crawford
Credit: N/A
Description: Starter Code for Project 4-1
'''
from turtle import *
import random

def draw_message(r, msg):
    '''(r: int, msg: str) -> None

    display the 8-ball's message

    >>> draw_msg(100, 'Hi')
    [displays Hi on turtle canvas positioned below 8-ball]
    '''
    # setup
    x = xcor()
    y = ycor()
    setpos(x, y - r)
    color('blue')

    # deliver the msg
    write(msg, align='center', font=('Arial', 50, 'normal'))

    # return turtle to previous position
    setpos(x, y)

    return

def draw_message2(r, msg):
    ''' will give a message depending on the number given
    >>>draw_message2 (r,8)
    displays message assignmed to 8 under draw_message
    '''

    #setup
    x = xcor()
    y = ycor()
    setpos (x, y-r*2)
    color ('blue')

    #deliver the msg
    write (msg, align = 'center', font=('ariel', 50, 'normal'))

    #return to previous spot
    setpos(x,y)

def draw_number(r, magic_number):
    '''(r: int, magic_number: int) -> None

    draw the magic number on an 8 ball with radius r

    >>> draw_number(100, 4)
    [displays number 4 on the 8-ball]
    '''
    x = xcor()
    y = ycor()
    setpos(x, r / 2)
    color('yellow')
    
    write(magic_number, align='center', font=('Arial', 100, 'normal'))
    
    setpos(x, y)
    
    return

def draw_8ball(r):
    '''(r: int) -> None

    draw 8-ball (filled circle) on turtle canvas

    >>> draw_8ball(100)
    [draws 8-ball with radius r]
    '''
    fillcolor('black')
    begin_fill()
    circle(r)
    end_fill()

    return

def setup():
    '''
    initial set up for 8-ball turtle and canvas

    >>> setup()
    [canvas and turtle are ready for 8-ball program]
    '''
    reset()
    clear()
    title("Magic 8 Ball")
    speed(0)
    penup()
    hideturtle()

    return

def consult_the_8ball():
    ''' driver '''

    # set up turtle and canvas
    setup()

    # set the size (radius) and color of the 8-ball
    r = 100
    color = 'black'

    # draw the ball
    draw_8ball(r)

    # shake the 8-ball to reveal a magic number 
    magic_number = random.randint(1, 8)

    # display the number and an initial message
    draw_number(r, magic_number)
    draw_message(r, 'Thinking ...')
    delay(500)

    # determine the 8-ball's message 
    if magic_number == 1:
        draw_message2(r, 'No.')
    elif magic_number == 2:
        draw_message2(r, 'Indubitably')
    elif magic_number == 3:
        draw_message2(r, 'try again later')
    elif magic_number == 4:
        draw_message2(r, 'absolutely!')
    elif magic_number == 5:
        draw_message2(r, 'maybe...')
    elif magic_number == 6:
        draw_message2(r, 'not right now')
    elif magic_number == 7:
        draw_message2(r, 'maybe later')
    elif magic_number == 8:
        draw_message2(r, 'yes.')
    return

    # display the message
    # draw_message(r * 2, msg)

def main():
    '''top-level function '''

    # ask the user for the number of predictions they want
    x = int(input('enter number of predictions wanted'))

    # call consult_the_8ball until the wanted number of predictions
    # has been generated
    for i in range(x):
        consult_the_8ball()
    return
                            
main()

