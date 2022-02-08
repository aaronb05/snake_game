from turtle import Turtle
STARTING_POS = ((-40, 0), (-20, 0), (0, 0))
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.move_speed = 20

    def draw_border(self):
        bot = Turtle()
        bot.color("white")
        bot.penup()
        bot.goto(-390, -390)
        bot.pendown()
        bot.setheading(UP)
        bot.forward(780)
        bot.setheading(RIGHT)
        bot.forward(780)
        bot.setheading(DOWN)
        bot.forward(780)
        bot.setheading(LEFT)
        bot.forward(780)
        bot.hideturtle()

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(pos)
        self.segments.append(new_block)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        self.move_speed += .5

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.move_speed)

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
            self.segments[0].setheading(RIGHT)

