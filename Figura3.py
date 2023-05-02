import turtle
import time

for i in range(4): # Ciclo para dibujar el cuadro base
    turtle.forward(100)
    ang =+ 90
    turtle.left(ang)

turtle.left(45) # Con este código se dibija el resto de la fígura
turtle.forward(141.4213)

for i in range (3):
    turtle.left(90)
    turtle.forward(70.7106)

turtle.forward(70.7106)
turtle.left(45)
    
time.sleep(5)