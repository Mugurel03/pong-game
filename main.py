from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

game_is_on = True

right_paddle = Paddle(350, 0)
right_paddle.move(up_key="Up", down_key="Down")
left_paddle = Paddle(-350, 0)
left_paddle.move(up_key="w", down_key="s")

while game_is_on:
    screen.update()


screen.exitonclick()
