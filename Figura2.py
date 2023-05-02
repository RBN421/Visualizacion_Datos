import turtle
import time

for i in range(3): # COn este ciclo se genera los tres giros donde se dibuja cada cuadro
    ang =+ 22.5
    turtle.left(ang)
    for j in range(4): # Con este ciclo se genera el cuadro
        turtle.forward(100)
        ang =+ 90
        turtle.left(ang)
        time.sleep(1)

time.sleep(5)