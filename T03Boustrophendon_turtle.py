import turtle

def make_turtle(tray):
    tray.pensize(10)
    tray.speed(8)
    tray.color('red')
    tray.left(90)
    tray.penup()
    tray.forward(5)
    tray.left(90)
    tray.forward(5)
    tray.right(90)
    tray.pendown()

    for i in range(10):
            tray.forward(190)
            tray.left(90)
            tray.forward(10)
            tray.left(90)
            tray.forward(190)
            tray.right(90)
            tray.forward(10)
            tray.right(90)

    tray.forward(190)




def make_square(t):
    """
    makes a square
    :return:

    """

    for i in range(2):
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(211)

def main():
    win = turtle.Screen()
    square_turtle = turtle.Turtle()


    make_square(square_turtle)
    make_turtle(square_turtle)
    win.exitonclick()

main()