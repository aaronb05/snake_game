import time
import turtle as t
import snake as s
import food as f
import scoreboard as sb

screen = t.Screen()
snake = s.Snake()
food = f.Food()
scoreboard = sb.Scoreboard()
screen.setup(width=815, height=900)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
snake.draw_border()

playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect if snake ate food
    if snake.head.distance(food) < 15:
        food.move_food()
        snake.extend()
        scoreboard.keep_score()

    # Detect wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        scoreboard.game_over()
        playing = False

    # Detect tail
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 1:
            playing = False
            scoreboard.game_over()

screen.exitonclick()


