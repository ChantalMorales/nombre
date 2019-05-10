import time
import turtle
t=turtle.Pen()

def estrellapar(tam,n):
	for x in range(n):
		t.forward(tam)
		t.left(ang)

tam = int(input("Ingrese el tamño para la estrella"))
n= int(input("Ingrese un numero par"))

ang= (-360/n)+180

estrellapar(tam,n)
