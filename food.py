from turtle import Turtle
from snake import Snake
import random as r
SCORE = 0


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("red")
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        random_x = r.randint(-370, 370)
        random_y = r.randint(-370, 370)
        self.goto(random_x, random_y)

