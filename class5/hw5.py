import turtle

turtle.speed(0)
turtle.penup()
for i in range(13):
    turtle.forward(50)
    turtle.stamp()
    turtle.home()
    turtle.right(30 * i)
turtle.done()
