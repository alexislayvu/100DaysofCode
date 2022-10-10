from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")  # shape = square
            new_segment.color("green")  # color = white
            new_segment.penup()  # no drawing while moving
            new_segment.goto(position)  # set position of current segment
            self.segments.append(new_segment)  # append Turtle object to 'segments' list

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_coordinate = self.segments[seg_num - 1].xcor()
            new_y_coordinate = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_coordinate, new_y_coordinate)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
