from oop_part1 import Shape
from oop_part1 import Rectangle
from oop_part1 import Circle
from oop_part1 import Line
import turtle
from turtle import Turtle

screen = turtle.Screen()
screen.bgcolor('White')
turtle.setup(width=600, height=600, startx=0, starty=0)

housebody = Rectangle(300, 200, turtle, "Black", -230,-230)
leftroof = Line(210, turtle, "Black", -230,-30, 43)
rightroof = Line(210, turtle, "Black", 70,-30, 137)

door = Rectangle(80, 130, turtle, "Black", -230,-230)
doorhandle = Circle(5, turtle, "Black", -173, -170)

head = Circle(20, turtle, "Black", 150,-80)

body = Line(100, turtle, "Black", 150,-80, 270)
leftarm = Line(50, turtle, "Black", 150,-90, 230)
rightarm = Line(50, turtle, "Black", 150,-90, 310)
leftleg = Line(60, turtle, "Black", 150,-180, 245)
rightleg = Line(60, turtle, "Black", 150,-180, 295)

housebody.draw()
rightroof.draw()
leftroof.draw()

door.draw()
doorhandle.draw()

head.draw()

body.draw()
leftarm.draw()
rightarm.draw()
leftleg.draw()
rightleg.draw()

turtle.done()
