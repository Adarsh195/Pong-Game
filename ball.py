from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.n_xcor=1
        self.n_ycor=1
        self.sp=1
    def move(self):
        x_cor=self.xcor()+self.n_xcor
        y_cor=self.ycor()+self.n_ycor
        self.goto(x_cor,y_cor)
    def bounce_y(self):
        self.n_ycor*=-1
        self.sp+=100
        self.speed(self.sp)
    def bounce_x(self):
        self.n_xcor*=-1
        self.sp += 100
        self.speed(self.sp)
    def reset_g(self):
        self.goto(0,0)
        self.bounce_x()
        self.bounce_y()
