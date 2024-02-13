from turtle import Turtle, Screen


class Paddle:
    def __init__(self, x_pos, y_pos):
        self.paddle = Turtle(shape="square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(stretch_len=1.0, stretch_wid=5.0)
        self.paddle.goto(x_pos, y_pos)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def move(self, up_key, down_key):
        screen = Screen()
        screen.listen()
        screen.onkey(self.go_up, up_key)
        screen.onkey(self.go_down, down_key)
