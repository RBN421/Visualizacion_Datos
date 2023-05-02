import turtle
import time

def posicion(x, y): # Definir función de posición
    turtle.penup() 
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

posicion(-100, 50) # Posicionar para la primera flecha
for i in range(10): # Ciclo para trazar la primera flecha
    turtle.forward(15)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

posicion(-100, -50) # Posicionar para la segunda flecha
for i in range(10): # Ciclo para trazar la segunda flecha
    turtle.forward(15 + (2 * i))
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

time.sleep(5)