from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

game_is_on = True

right_paddle = Paddle(350, 0)
right_paddle.move(up_key="Up", down_key="Down")
left_paddle = Paddle(-350, 0)
left_paddle.move(up_key="w", down_key="s")
ball = Ball()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    ball.detect_collision(SCREEN_HEIGHT)

screen.exitonclick()
