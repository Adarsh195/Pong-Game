from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1, 1)
        self.color("white")
        self.goto(x_cor, y_cor)

    def go_up(self):
        y=20
        if self.ycor()>=240:
            y=0
        self.goto(self.xcor(), self.ycor() + y)

    def go_down(self):
        y = 20
        if self.ycor() <= -240:
            y = 0
        self.goto(self.xcor(), self.ycor() - y)
