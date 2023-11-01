from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self, position):
        self.i = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.write(arg=self.i, font=('Arial', 20, 'normal'))

    def increment_score(self):
        self.clear()
        self.i += 1
        self.write(arg=self.i, font=('Arial', 20, 'normal'))
