from datetime import datetime
from typing import List
import time
import turtle
import requestxander


scrn = turtle.Screen()
xander = turtle.Turtle()
Font = ("arial", 12, "normal")


def box(color):
    xander.pendown()
    xander.fillcolor(color)
    xander.begin_fill()
    xander.forward(450)
    xander.left(90)
    xander.forward(125)
    xander.left(90)
    xander.forward(450)
    xander.left(90)
    xander.forward(125)
    xander.left(90)
    xander.end_fill()
    xander.penup()


# naar beneden met 1 vakje
def drawdown():

    xander.right(90)
    xander.forward(128)
    xander.left(90)


# startpositie
def drawpos():
    xander.setpos(-685, 263)


def text(i):
    xander.color("white")
    xander.left(90)
    xander.forward(90)
    xander.right(90)
    xander.forward(20)
    xander.write(datetime.fromtimestamp(int(trainlist[i]["time"])), font=Font)
    xander.forward(150)
    if datetime.fromtimestamp(int(trainlist[i]["delay"])).strftime("%M") != "00":

        xander.write(
            "+" + datetime.fromtimestamp(int(trainlist[i]["delay"])).strftime("%M"),
            font=Font,
        )
    xander.forward(100)
    xander.write(trainlist[i]["vehicleinfo"]["shortname"], font=Font)
    xander.forward(100)
    xander.write("platform: " + trainlist[i]["platform"], font=Font)
    xander.backward(370)
    xander.right(90)
    xander.forward(80)
    xander.left(90)
    xander.forward(20)
    xander.write(trainlist[i]["station"], font=Font)
    xander.backward(20)
    xander.right(90)
    xander.forward(13)
    xander.left(90)
    xander.color("black")


def draw():

    colours = ("cornflowerblue", "navyblue")
    i = 0
    drawpos()
    xander.penup()
    while i < 6:
        if i % 2 == 0:
            c = 1
        else:
            c = 0
        box(colours[c])
        text(i)

        i = i + 1
        drawdown()  # naar beneden met 1 vak

    drawpos()

    xander.forward(453)  # kollom opschuiven

    while i < 12:
        if i % 2 == 0:
            c = 0
        else:
            c = 1
        box(colours[c])
        text(i)

        i = i + 1
        drawdown()  # naar beneden met 1 vak

    drawpos()
    xander.forward(906)

    while i < 18:
        if i % 2 == 0:
            c = 1
        else:
            c = 0
        box(colours[c])
        text(i)
        i = i + 1
        drawdown()  # naar beneden met 1 vak


while True:
    trainlist = requestxander.request()
    xander.penup()
    xander.speed(0)
    draw()

    # time.sleep(9)
