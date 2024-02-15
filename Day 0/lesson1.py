from turtle import * 

speed(30)
width(5)
shape("turtle")

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

penup()
goto(80, 0)
pendown()
color("blue")

begin_fill()
right(180)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()

#drawing roof

penup()
goto(200, 200)
pendown()
color("cyan")

begin_fill()
right(145)
forward(170)
left(110)
forward(170)
end_fill()

#drawing windows

penup()
goto(180, 180)
pendown()
color("purple")

begin_fill()
right(55)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(70, 180)
pendown()

begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()
