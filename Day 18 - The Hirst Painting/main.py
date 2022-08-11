import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.shape("classic")
tim.speed("fastest")
tim.pensize(15)


random_movements = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color

for _ in range(1000):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(random_movements))


screen = Screen()
screen.exitonclick()
