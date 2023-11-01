from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
scorecard_l = Scorecard((20, 240))
scorecard_r = Scorecard((-20, 240))
ball = Ball()
screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game = True
while game:
    time.sleep(ball.speed_of_ball)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ((ball.distance(paddle1) < 70 and ball.xcor() > 330) or
            (ball.distance(paddle2) < 70 and ball.xcor() < -330)):
        ball.bounce_x()
    # Detecting when the ball goes out
    if ball.xcor() > 380:
        scorecard_r.increment_score()
        ball.ball_is_out()
    elif ball.xcor() < -380:
        # print("ball is out")
        scorecard_l.increment_score()
        ball.ball_is_out()
screen.exitonclick()
