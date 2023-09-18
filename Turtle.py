import turtle
import math
# SRP each class is responsible for only a single shape
# open/closed. the script is closed to changing the values that make up the pre established shapes while being open to adding new shapes with the same design
# LSP each shape can substitute each other
# ISP independednt shape classes

# DIP base class for shapes
class shape_dip:
    def __init__(self,scale,color):
        # initialize a turtle object for drawing
        self.t=turtle.Turtle()
        # set the shapes size
        self.scale=scale
        # set the shapes color
        self.t.color(color)
    def draw(self):
        # this method is abstract and will be overridden by subclasses
        pass

class star(shape_dip):
    def __init__(self,scale,color):
        self.t=turtle.Turtle()
        self.scale=scale
        self.t.color(color)
    def draw(self):
        # draw the empty star
        for i in range(5):
            self.t.forward(self.scale)
            self.t.left(36-180)
            self.t.forward(self.scale)
            self.t.left(180-108)

class star_interconnected(shape_dip):
    def __init__(self,scale,color):
        self.t=turtle.Turtle()
        self.scale=scale
        self.t.color(color)
    def draw(self):
        # draw the interconnected star
        for i in range(5):
            self.t.forward(self.scale)
            self.t.left(36-180)

class rhombus(shape_dip):
    def __init__(self,scale,color):
        self.t=turtle.Turtle()
        self.scale=scale
        self.t.color(color)
    def draw(self):
        # draw the rhombus
        self.t.forward(self.scale)
        self.t.left(45)
        self.t.forward(self.scale)
        self.t.left(135)
        self.t.forward(self.scale)
        self.t.left(45)
        self.t.forward(self.scale)
        self.t.left(135)

class custom_shape(shape_dip):
    def __init__(self,scale,points,color):
        self.t=turtle.Turtle()
        self.scale=scale
        self.points=points
        self.t.color(color)
    def draw(self):
        # draw a shape with the given number of sides
        i=0
        while i<self.points:
            self.t.forward(self.scale/self.points)
            self.t.left(360/self.points)
            i=i+1

# initialize and draw shapes
star=star(50,"red")
star.draw()

star_interconnected=star_interconnected(100,"yellow")
star_interconnected.draw()

rhombus=rhombus(50,"green")
rhombus.draw()

shape=custom_shape(200,5,"blue")
shape.draw()
