from turtle import Turtle, Screen

tim = Turtle()

# tim.shape("turtle")
# tim.color("green")

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)


# for i in range(10):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.pd()


def triangle():
    tim.color("green")
    tim.forward(100)
    tim.right(120)
    tim.forward(100)
    tim.right(120)
    tim.forward(100)


def square():
    tim.color("red")
    tim.left(150)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)


def pentagon():
    tim.color("purple")
    tim.right(162)
    tim.forward(100)
    for i in range(4):
        tim.right(72)
        tim.forward(100)


def hexagon():
    tim.color("orange")
    for i in range(6):
        tim.right(60)
        tim.forward(100)


def heptagon():
    tim.color("pink")
    for i in range(7):
        tim.right(51.42857142857143)
        tim.forward(100)


def octagon():
    tim.color("pink")
    for i in range(8):
        tim.right(45)
        tim.forward(100)


def nonagon():
    tim.color("brown")
    for i in range(9):
        tim.right(40)
        tim.forward(100)


def decagon():
    tim.color("black")
    for i in range(10):
        tim.right(36)
        tim.forward(100)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

screen = Screen()
# screen.exitonclick()