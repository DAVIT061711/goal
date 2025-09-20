from turtle import *

#we want to paint a house

#step 1:  draw s square
shape("turtle")
speed(1)
width(7)
color("purple")
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
color("yellow")
begin_fill()
left(90)
forward(120)    #heght of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# drawing a window

penup()
goto(200, 200)


forward(30)
color("black")
begin_fill()
left(300)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

#drawing second window

penup()
goto(60, 140)


forward(30)
color("black")
begin_fill()
right(300)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()



exitonclick()