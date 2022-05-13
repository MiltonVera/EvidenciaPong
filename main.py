from operator import truediv
from turtle import *
from time import *
from random import randrange

import asyncio


pantalla = Screen()
pantalla.title("Flappy Bird")
pantalla.bgcolor("black")
pantalla.setup(width=800, height = 600)

yins = []
yfins = []
rectangulos1 = []
rectangulos2 = []



#margenes = []
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
    x = 300
    altura = randrange(300,600,10)
    margen = 200

    yin = altura-margen
    yfin = altura

    rectangulo1 = Turtle()
    rectangulo1.speed(0)
    rectangulo1.penup()
    rectangulo1.goto(x,altura)
    rectangulo1.shape("square")
    rectangulo1.color("white")
    rectangulo1.shapesize(stretch_wid=30, stretch_len=3)
    

    rectangulo2 = Turtle()
    rectangulo2.speed(0)
    rectangulo2.penup()
    rectangulo2.goto(x,altura-margen-600)
    print(altura-margen-600)
    rectangulo2.shape("square")
    rectangulo2.color("white")
    rectangulo2.shapesize(stretch_wid=30, stretch_len=3)

    #Margen de 200 pixeles
    return rectangulo1,rectangulo2,yin,yfin



pantalla.listen()
pantalla.onkeypress(subir,"w")

def moverObstaculo(rectangulos1,rectangulos2, i):
    xrectangulo1 = rectangulos1[i].xcor()
    xrectangulo2 = rectangulos2[i].xcor()

    xrectangulo1 -=10
    xrectangulo2 -= 10

    rectangulos1[i].setx(xrectangulo1)
    rectangulos2[i].setx(xrectangulo2)

frame = 1
index = 0

activados = [False,False,False]

while(pajaro.ycor() > -600):
    pantalla.update()
    if(frame%30 == 0 or frame == 1):
        
        rectangulo1,rectangulo2,yin,yfin = dibujarObstaculo()

        rectangulos1.append(rectangulo1)
        rectangulos2.append(rectangulo2)
        yins.append(yin)
        yfins.append(yfin)
        
        print(activados)
        if(activados[0]):
            if(activados[1]):
                if(not activados[2]):
                    activados[2] = True
            else:
                activados[1] = True
        else:
            activados[0] = True
            
    if (activados[0]):
        moverObstaculo(rectangulos1,rectangulos2,0)
    if (activados[1]):
        moverObstaculo(rectangulos1,rectangulos2,1)
    if (activados[2]):
        moverObstaculo(rectangulos1,rectangulos2,2)

    

    sleep(0.01)
    caida()
    frame+=1


    

