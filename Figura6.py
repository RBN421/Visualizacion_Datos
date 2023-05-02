import turtle
import time

def posicion(x, y): # Función para posicionar la tortuga
    turtle.penup() 
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

def figura(lados, avance, angulo): # Función para generar figuras
    for i in range(lados):
        turtle.forward(avance)
        ang =+ angulo
        turtle.left(ang)

posicion(-125, 0) # Pisiciona para generar el triangulo
figura(3, 50, 120) # Genera el triangulo

posicion(0, 0) # Pisiciona para generar el cuadrado
figura(4, 75, 90) # Genera el cuadrado

posicion(150, 0) # Pisiciona para generar el pentágono
figura(5, 100, 72) # Genera el pentágono

time.sleep(5)