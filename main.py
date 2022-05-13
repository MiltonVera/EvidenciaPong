from operator import truediv
from turtle import *
from time import *
from random import randrange


#Creamos la pantalla
pantalla = Screen()
pantalla.title("Flappy Bird")
pantalla.bgcolor("blue")
pantalla.setup(width=800, height = 600) #se define el ancho y alto de la pantalla en 800 x 600 

#Definimos listas por defecto
yins = [] #se define una lista con las alturas de los rectangulos menos el margen por el que pasa el pajaro
yfins = [] #se define otra lista con las alturas de los rectangulos a partir de la parte superior del margen
rectangulos1 = [] #lista con los rectangulos de arriba
rectangulos2 = [] #lista con los rectangulos de abajo

#Inicialización del puntaje
puntaje = 0

#Dibujamos el pajaro
pajaro = Turtle()
pajaro.speed(0)
pajaro.shape("circle")
pajaro.color("yellow")
pajaro.penup()
pajaro.goto(0,0)

#Dibuajamos el recuadro de score
score = Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-200, 200)
score.write("DISTANCIA  0",align="center", font=("Fixedsys", 24, "bold"))

#Funcion que realiza la caida del pajaro
def caida():
    y = pajaro.ycor()
    y-=5
    pajaro.sety(y) # las coordenadas del pajaro bajan en 5 unidades en y por cada vez que se aplique caida
#Funcion que sube el pajaro
def subir():
    y = pajaro.ycor()
    y+=10 #cada vez que se aplica la funcion subir las coordenadas del pajaro aumentan en 10 unidades 
    pajaro.sety(y)
    
#Funcion que dibuja los obstaculos y retorna los dos dibujos
def dibujarObstaculo():
    x = 300 #se define la coordenada en x de inicio de todos los rectángulos en 300 unidades
    altura = randrange(300,600,10) # las alturas máximas de los rectángulos pueden variar entre 300, 600 o 10 unidades
    margen = 200 #se declara un margen de altura constante por el que puede pasar el pajaro

    yin = altura-margen #se define la altura inferior como la altura seleccionada menos el margen
    yfin = altura #la altura superior simplemente es la altura elegida por el programa

    rectangulo1 = Turtle()
    rectangulo1.speed(0)
    rectangulo1.penup()
    rectangulo1.goto(x,altura)#se dibuja el primer rectangulo en la coordenada x y la altura elegida por el programa
    rectangulo1.shape("square")
    rectangulo1.color("green")
    rectangulo1.shapesize(stretch_wid=30, stretch_len=3) #se declara la altura y anchura de los rectangulos. Cada valor de wid y len está multiplicado por 20 al dibujarse
    
    rectangulo2 = Turtle()
    rectangulo2.speed(0)
    rectangulo2.penup()
    rectangulo2.goto(x,altura-margen-600)#se hace un ajuste manual de -600 unidades en la altura del rectangulo
    rectangulo2.shape("square")
    rectangulo2.color("green")
    rectangulo2.shapesize(stretch_wid=30, stretch_len=3)

    #Margen de 200 pixeles
    return rectangulo1,rectangulo2,yin,yfin


#Hacemos que la pantalla escuche los clicks
pantalla.listen()
pantalla.onkeypress(subir,"w")

#Mueve los obstaculos y usa como objeto de entrada el obstaculo
def moverObstaculo(rectangulos1,rectangulos2, i):
    xrectangulo1 = rectangulos1[i].xcor()
    xrectangulo2 = rectangulos2[i].xcor()

    xrectangulo1 -=10 #Por cada aplicacion de la funcion moverobstaculo los rectangulos se mueven 10 unidades a la derecha
    xrectangulo2 -= 10 #

    rectangulos1[i].setx(xrectangulo1)
    rectangulos2[i].setx(xrectangulo2)

# Medidor de frames
frame = 0
# Lista para los diferentes obstáculos que habrá activos en todo momento
activados = [False,False,False,False]

#Ciclo while que corre el programa completo
while(True):
    #Actualiza la pantalla
    pantalla.update()
    #Detecta si el pajara se salio de los limites
    if (pajaro.ycor()+300 < 0 or pajaro.ycor()+300 > 600):
        break
        
    if(frame%25 == 0):
        
        # Obtenemos la posición de los 2 rectángulos y del área libre entre ellos
        # mediante esta función
        rectangulo1,rectangulo2,yin,yfin = dibujarObstaculo()

        # Agregamos los elementos anteriores a su respectiva lista
        rectangulos1.append(rectangulo1)
        rectangulos2.append(rectangulo2)
        yins.append(yin)
        yfins.append(yfin)


        # De esta forma activamos nuestra "pool" de rectángulos (obstáculos)
        if(activados[0]):
            if(activados[1]):
                if(not activados[2]):
                    activados[2] = True
            else:
                activados[1] = True
        else:
            activados[0] = True
            
    if(frame < 25):
        # Si el pájaro está por debajo de donde empieza el área "segura", entonces salimos del ciclo
        if((pajaro.ycor()+300 < yins[0] or pajaro.ycor()+300 > yfins[0]) and rectangulos1[0].xcor() < 30):
            break
        
    else:
        # Si el pájaro está por encima de donde termina el área "segura", entonces salimos del ciclo
        if((pajaro.ycor()+300 < yins[1] or pajaro.ycor()+300 > yfins[1]) and rectangulos1[1].xcor() < 30):
            break
        else:
            puntaje+=1
            
    
    #Mueve los objetos dependiendo del estado del activador
    if (activados[0]):
        moverObstaculo(rectangulos1,rectangulos2,0)
    if (activados[1]):
        moverObstaculo(rectangulos1,rectangulos2,1)
    if (activados[2]):
        moverObstaculo(rectangulos1,rectangulos2,2)
    #Elimina los rectangulos si se pasan de la linea
    if(rectangulos1[0].xcor() < pajaro.xcor()-300):
        rectangulos1[0].reset()#Se eliminan los rectangulos una vez se pasan de 300 uniades de la posicion del pajaro
        rectangulos2[0].reset()
        rectangulos1.pop(0)
        rectangulos2.pop(0)
        yins.pop(0)
        yfins.pop(0)
        activados.pop(0)
        activados.append(False)
    
    #Acutaliza
    score.clear()
    score.write("DISTANCIA  {}".format(puntaje),align="center", font=("Fixedsys", 24, "bold"))
    
    # Así hacemos que juego vaya más lento
    sleep(0.01)#0.01

    # La pelota siempre cae por default
    caida()

    frame+=1


#Hacer señal de que perdiste después de haber salido del ciclo While
perder = Turtle()
perder.speed(0)
perder.penup()
perder.color("red")
perder.hideturtle()
perder.goto(0, 0)
perder.write("PERDISTE",align="center", font=("Fixedsys", 24, "bold"))
done()