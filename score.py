from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_of_A=0
        self.score_of_B=0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,250)
        self.write(self.score_of_A,False,"center",("arial",30,"bold"))
        self.goto(100,250)
        self.write(self.score_of_B, False, "center", ("arial", 30, "bold"))

    def s_update_A(self):
        self.score_of_A+=1
        self.update()
    def s_update_B(self):
        self.score_of_B+=1
        self.update()


