import random
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# penup() prevents the turtle from drawing when moving
turtle.penup()
turtle.speed('fastest')
screen.colormode(255)

x_axis = -300
y_axis = -310

turtle.setx(x_axis)
turtle.sety(y_axis)

color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

dot_count = 0
for color in range(110):
    random_color = random.choice(color_list)
    turtle.fillcolor(random_color)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.setx(x_axis)
    x_axis += 65
    dot_count += 1

    # Check if there are 10 dots across the x-axis;
    # if True then move the turtle up a row and back to the first column
    if dot_count % 11 == 0:
        x_axis = -300
        y_axis += 65
        turtle.setx(x_axis)
        turtle.sety(y_axis)

turtle.hideturtle()
screen.exitonclick()

# How the color_list was made:
# import colorgram

# Extract colors from image
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#
#     rgb_colors.append((red, green, blue))
#
# print(rgb_colors)
# Copy and pasted the rgb color tuples into color_list^^
