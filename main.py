from turtle import *
from time import *
from random import randrange


pantalla = Screen()
pantalla.title("Flappy Bird")
pantalla.bgcolor("black")
pantalla.setup(width=800, height = 600)
# pantalla.tracer(0)

#Tubos cruzados
puntaje = 0

#Dibujamos el pajaro
pajaro = Turtle()
pajaro.speed(0)
pajaro.shape("circle")
pajaro.color("white")
pajaro.penup()
pajaro.goto(0,0)
quieto = True

def caida():
    y = pajaro.ycor()
    y-=5
    pajaro.sety(y)
def subir():
    y = pajaro.ycor()
    y+=10
    pajaro.sety(y)

def dibujarObstaculo():
    rectanguloBlanco = Turtle()
    rectanguloBlanco.speed(1)
    rectanguloBlanco.shape("square")
    rectanguloBlanco.color("white")
    rectanguloBlanco.shapesize(stretch_wid=30, stretch_len=3)
    rectanguloBlanco.penup()

    margen = Turtle()
    margen.speed(1)
    margen.shape("square")
    margen.color("black")
    margen.shapesize(stretch_wid=5, stretch_len=3)
    margen.penup()
    

    
    



dibujarObstaculo()

pantalla.listen()
pantalla.onkeypress(subir,"w")

while(pajaro.ycor() > -600):
    pantalla.update()
    sleep(0.01)
    caida()

    

