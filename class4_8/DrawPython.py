#e2.1DrawPython.py
import turtle
turtle.setup(700,700,None,None)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("violet")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,90)
    turtle.circle(-40,90)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
