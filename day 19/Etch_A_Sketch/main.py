from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def counter_clock():
    tim.circle(50, 50, 50)


def clockwise():
    tim.circle(50, -30, 50)


def reset():
    tim.reset()


screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(counter_clock, "a")
screen.onkey(clockwise, "d")
screen.onkey(reset, "c")
screen.exitonclick()


