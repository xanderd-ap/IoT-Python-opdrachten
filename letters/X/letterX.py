import turtle  # load the turtle module

scrn = turtle.Screen()  # Create/obtain the turtle screen object.
bob = (
    turtle.Turtle()
)  # Create a turtle object, that we can use to draw. (I named it bob for some reason.)

bob.left(45)  # move forward 50 pixels
bob.forward(90)  # turn left 90 degrees
bob.right(180)
bob.forward(45)
bob.right(90)
bob.forward(45)
bob.right(180)
bob.forward(90)
turtle.done()  # cleanup
