from turtle import *

#we want to paint a house

#step 1:   draw a square

width(7)
color("pink")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("red")
left(90)
forward(120)
right(90)
forward(50)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("green")
forward(20)
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
#end door

#first window
penup()
goto(65, 140)
pendown()

begin_fill()
right(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)

#second window
penup()
goto(140, 140)
pendown()

begin_fill()
right(180)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)






exitonclick()

