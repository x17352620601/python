import turtle
#turtle.pensize(10)
#turtle.fd(100)
for i in range(1,10):
    turtle.circle(20*i)
    turtle.seth(-90)
    turtle.penup()
    turtle.fd(20)
    turtle.pendown()
    turtle.seth(0)
