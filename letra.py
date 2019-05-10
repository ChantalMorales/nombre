import time
import turtle
t=turtle.Pen()

def nombre(tam):
	for x in range(1,4):
		t.backward(tam)
		t.left(90)

tam = int(input("Ingrese el tamaño para la letra"))


nombre(tam)