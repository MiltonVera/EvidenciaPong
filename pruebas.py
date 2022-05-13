from turtle import *



pantalla = Screen()
pantalla.title("Pong")
pantalla.bgcolor("white")
pantalla.setup(width=1000, height=600)


cuadradol = Turtle()
cuadradol.speed(0)
cuadradol.shape("square")
cuadradol.color("black")
cuadradol.shapesize(stretch_wid=8, stretch_len=2)
cuadradol.penup()
cuadradol.goto(-400,0)

cuadrador = Turtle()
cuadrador.speed(0)
cuadrador.shape("square")
cuadrador.color("black")
cuadrador.shapesize(stretch_wid=8, stretch_len=2)
cuadrador.penup()
cuadrador.goto(400,0)


def moveUpL():
    y = cuadradol.ycor()
    y += 20;
    cuadradol.sety(y)

def moveDownL():
    y = cuadradol.ycor()
    y -= 20;
    cuadradol.sety(y)

def moveUpR():
    y = cuadrador.ycor()
    y += 20;
    cuadrador.sety(y)

def moveDownR():
    y = cuadrador.ycor()
    y -= 20;
    cuadrador.sety(y)


pantalla.listen()
pantalla.onkeypress(moveUpL, "w")
pantalla.onkeypress(moveDownL, "s")

pantalla.onkeypress(moveUpR, "Up")
pantalla.onkeypress(moveDownR, "Down")

done()
