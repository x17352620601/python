import turtle
turtle.pu()
turtle.fd(-300)
turtle.pd()

turtle.pensize(10)
turtle.pencolor("red")
for i in range(10):
    turtle.seth(90+20*i)
    turtle.circle(20,100)
    turtle.circle(-20,100)
turtle.pencolor("grenn")
turtle.fd(40)
turtle.seth(180)
turtle.fd(30)
