import turtle

rover = turtle.Turtle()
rover.shape("turtle")
rover.color("red")
rover.speed(5)

def move_forward():
    rover.forward(50)

def move_backward():
    rover.backward(50)

def turn_left():
    rover.left(90)

def turn_right():
    rover.right(90)

turtle.listen()

turtle.onkey(move_forward, "Up")
turtle.onkey(move_backward, "Down")
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")

turtle.done()
