from operator import truediv
from turtle import *
from time import *
from random import randrange



pantalla = Screen()
pantalla.title("Flappy Bird")
pantalla.bgcolor("black")
pantalla.setup(width=800, height = 600)

yins = []
yfins = []
rectangulos1 = []
rectangulos2 = []


#Tubos cruzados
puntaje = 0

#Dibujamos el pajaro
pajaro = Turtle()
pajaro.speed(0)
pajaro.shape("circle")
pajaro.color("yellow")
pajaro.penup()
pajaro.goto(0,0)

score = Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-200, 200)
score.write("DISTANCIA  0",align="center", font=("Fixedsys", 24, "bold"))


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
    rectangulo1.color("green")
    rectangulo1.shapesize(stretch_wid=30, stretch_len=3)
    

    rectangulo2 = Turtle()
    rectangulo2.speed(0)
    rectangulo2.penup()
    rectangulo2.goto(x,altura-margen-600)
    rectangulo2.shape("square")
    rectangulo2.color("green")
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
activados = [False,False,False,False]

while(True):
    pantalla.update()

    if (pajaro.ycor()+300 < 0 or pajaro.ycor()+300 > 600):
        break

    if(frame%25 == 0 or frame == 1):
        
        rectangulo1,rectangulo2,yin,yfin = dibujarObstaculo()

        rectangulos1.append(rectangulo1)
        rectangulos2.append(rectangulo2)

        yins.append(yin)
        yfins.append(yfin)



        if(activados[0]):
            if(activados[1]):
                if(not activados[2]):
                    activados[2] = True
                # else:
                #     activados[3] = True
            else:
                activados[1] = True
        else:
            activados[0] = True
            
    if(frame < 25):
        if((pajaro.ycor()+300 < yins[0] or pajaro.ycor()+300 > yfins[0]) and rectangulos1[0].xcor() < 15):
            #vivo = False 
            break
        
    else:
        if((pajaro.ycor()+300 < yins[1] or pajaro.ycor()+300 > yfins[1]) and rectangulos1[1].xcor() < 15):
            #vivo = False
            break
        else:
            puntaje+=1

            

    
    #Garbage collector
    if (activados[0]):
        moverObstaculo(rectangulos1,rectangulos2,0)
    if (activados[1]):
        moverObstaculo(rectangulos1,rectangulos2,1)
    if (activados[2]):
        moverObstaculo(rectangulos1,rectangulos2,2)
    if(rectangulos1[0].xcor() < pajaro.xcor()-300):
        rectangulos1[0].reset()
        rectangulos2[0].reset()
        rectangulos1.pop(0)
        rectangulos2.pop(0)
        yins.pop(0)
        yfins.pop(0)
        activados.pop(0)
        activados.append(False)
    
    #Score
    score.clear()
    score.write("DISTANCIA  {}".format(puntaje),align="center", font=("Fixedsys", 24, "bold"))
    

    sleep(0.01)#0.01
    caida()
    frame+=1

#Hacer señal de que perdiste
perder = Turtle()
perder.speed(0)
perder.color("red")
perder.penup()
perder.hideturtle()
perder.goto(0, 300)
perder.clear()
perder.write("PERDISTE",align="center", font=("Fixedsys", 24, "bold"))
done()

