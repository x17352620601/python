import turtle
c=['white','black','grey','darkgreen','gold','violet','purple']
turtle.setup(700,700,None,None)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(20)
turtle.seth(-40)

turtle.pencolor("black")
turtle.circle(40,80)
turtle.circle(-40,80)

turtle.pencolor("grey")
turtle.circle(40,80)
turtle.circle(-40,80)

turtle.pencolor("darkgreen")
turtle.circle(40,80)
turtle.circle(-40,80)

turtle.pencolor("gold")
turtle.circle(40,80)
turtle.circle(-40,80)

turtle.pencolor("violet")
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)

