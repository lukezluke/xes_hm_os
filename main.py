from meowbit import *
from time import *

#变量
buttons = 0 

#中断
def up_pressed():
    global buttons
    buttons = 1
    sleep_ms(50)

def down_pressed():
    global buttons
    buttons = 2
    sleep_ms(50)

def left_pressed():
    global buttons
    buttons = 3
    sleep_ms(50)

def right_pressed():
    global buttons
    buttons = 4
    sleep_ms(50)

def a_pressed():
    global buttons
    buttons = 5
    sleep_ms(50)

def b_pressed():
    global buttons
    buttons = 6
    sleep_ms(50)

sensor.btnTrig['up'] = up_pressed
sensor.btnTrig['down'] = down_pressed
sensor.btnTrig['left'] = left_pressed
sensor.btnTrig['right'] = right_pressed
sensor.btnTrig['a'] = a_pressed
sensor.btnTrig['b'] = b_pressed

sensor.startSchedule()