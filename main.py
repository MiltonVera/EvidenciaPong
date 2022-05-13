from turtle import *



# Variables para almacenar los puntos de los jugadores
puntos_l = 0
puntos_r = 0

#Creamos la pantalla
pantalla = Screen()#creamos la instancia de la pantalla
pantalla.title("Pong")#Definimos el titulo de la ventana
pantalla.bgcolor("black")#Colocamos el fondo como negro
pantalla.setup(width=1000, height=600)#Definimos las dimensiones de la patalla
speed(0)

cuadradol = Turtle()#Creamos el objeto que dibujara 
cuadradol.shape("square")#Definimos que dibuje un cuadrado
cuadradol.color("white")#Indicamos el color del cuadrado como blanco
cuadradol.shapesize(stretch_wid=8, stretch_len=2)#Definimos las dimensiones del cuadrado
cuadradol.penup()#Levantamos el lapiz
cuadradol.goto(-400,0)

cuadrador = Turtle()#Se crea un segundo cuadrado
cuadrador.shape("square")
cuadrador.color("white")
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

