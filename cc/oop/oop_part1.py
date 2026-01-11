# define classes to create shapes
from turtle import Turtle as t


class Shape:
   def __init__(self, t, color):
       self.t = t.Turtle()
       self.color = color
   def getColor(self):
       print(self.color)
   def setColor(self, newcolor):
       self.color = newcolor

class Rectangle(Shape):
   def __init__(self, length, width, t, color, xcorner_location, ycorner_location):
       Shape.__init__(self, t = t, color = color)
       self.length = length
       self.width = width
       self.xcorner_location = xcorner_location
       self.ycorner_location = ycorner_location
   def draw(self):
       self.t.penup()
       self.t.setpos(self.xcorner_location, self.ycorner_location)
       self.t.pendown()
       self.t.forward(self.length)
       self.t.left(90)
       self.t.forward(self.width)
       self.t.left(90)
       self.t.forward(self.length)
       self.t.left(90)
       self.t.forward(self.width)
       self.t.penup()

class Circle(Shape):
   def __init__(self, radius, t, color, xcenter, ycenter):
       Shape.__init__(self, t = t, color = color)
       self.radius = radius
       self.xcenter = xcenter
       self.ycenter = ycenter
   def draw(self):
       self.t.penup()
       self.t.setpos(self.xcenter, self.ycenter)
       self.t.pendown()
       self.t.circle(self.radius)
       self.t.penup()

class Line(Shape):
   def __init__(self, length, t, color, xstart_point, ystart_point, angle):
       Shape.__init__(self, t = t, color = color)
       self.length = length
       self.xstart_point = xstart_point
       self.ystart_point = ystart_point
       self.angle = angle
   def draw(self):
       self.t.penup()
       self.t.setpos(self.xstart_point, self.ystart_point)
       self.t.pendown()
       self.t.setheading(self.angle)
       self.t.forward(self.length)
       self.t.penup()
