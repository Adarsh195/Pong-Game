from turtle import  Turtle
l=[290]
class Line(Turtle):
    def __init__(self,y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 0.5, 1)
        self.color("white")
        self.goto(0,y)

