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

#启动画面
screen.fill((0, 0, 0))
screen.drawRect(50,50,60,10,7)
screen.drawRect(50,50,10,60,7)
screen.drawRect(50,100,60,10,7)
screen.drawRect(90,60,10,10,7)
screen.drawRect(80,70,10,10,7)
screen.drawRect(70,80,10,10,7)
screen.drawRect(60,90,10,10,7)
sleep(3)

#欢迎
screen.fill((168,218,241))
screen.text("welcome!",30,30)
sleep(3)

#主界面
screen.fill((168,218,241))
screen.text("Ready",0,0)
'''
if buttons == 1:
    while True:
        screen.fill((168,218,241))
        screen.text("buttons test",10,0)
        if buttons != 0:
            screen.text("pressed:",10,10)
            screen.text("the {text} button is pressed"format(text=buttons),10,20)
elif buttons == 2:
    while True:
        screen.fill((168,218,241))
        screen.text("file test",10,0)
        fi = read("file.txt","r")
        li = fi.readlines()
        screen.text("file:",10,10)
        screen.text(li,10,20)'''