# -*- coding: utf-8 -*-
"""
@Time    : 2022/5/18 14:26
@Author  : jackyLiu
@Address : https://gitee.com/Onedragon424
@Reference:
    code                https://pythondex.com/python-program-to-wish-happy-birthday-with-code
    import mp3 media    https://blog.csdn.net/weixin_42581655/article/details/124789762
@source:
    birthday song       https://www.1happybirthday.com/
"""
# import lib
import turtle
import random
import time
import os
import sys
from pygame import mixer


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        #base_path = os.path.abspath(".")
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# Adding music is optional as per your choice.
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load(resource_path(os.path.join('res','happy_birthday.mp3'))) #add your music file name or path

# sets background
bg = turtle.Screen()
bg.bgcolor("black")
mixer.music.play()

# tutle setting
turtle.speed(0.51)

# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)
bg.bgcolor("lightgreen")

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
bg.bgcolor("lightblue")

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
bg.bgcolor("orange")

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

bg.bgcolor("black")

# Happy Birthday message

turtle.penup()
turtle.goto(-150, 50)
turtle.color("pink")
turtle.pendown()

# ENTER YOUR NAME IN THE NAME PLACE
turtle.write(arg=f" Happy Birthday !", align="left", font=("jokerman", 24, "normal"))

time.sleep(35)