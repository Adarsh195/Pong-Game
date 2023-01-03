from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
from line import Line
import time
l=290
s = Screen()
s.setup(1000, 600)
s.bgcolor("black")
s.title("Pong")

s.tracer(0)
pad1 = Paddle(-460, 0)
pad2 = Paddle(460, 0)
ball = Ball()
score = Score()
for i in range(17):
    line=Line(l)
    l-=40

s.listen()
s.onkey(pad1.go_up, "w")
s.onkey(pad1.go_down, "s")
s.onkey(pad2.go_up, "Up")
s.onkey(pad2.go_down, "Down")
sp = 0.005
while True:
    time.sleep(sp)
    s.update()
    ball.move()
    # Detect collision
    if ball.ycor() >= 288 or ball.ycor() <= -288:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.xcor() >= 440 and ball.distance(pad2) <= 50 or ball.xcor() <= -440 and ball.distance(pad1) <= 50:
        ball.bounce_x()
        sp *= 0.9

    # Detect Ball Missing
    if (ball.xcor() >= 490):
        ball.reset_g()
        score.s_update_A()
        sp = 0.005
    if ball.xcor() <= -490:
        ball.reset_g()
        score.s_update_B()
        sp = 0.005

s.exitonclick()
