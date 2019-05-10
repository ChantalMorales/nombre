import turtle
import tkinter
import pygame
import time

numeroLados=int(input("Ingresar numero impar de lados"))
t=turtle
t=turtle.Pen()

angulo = ((-360/numeroLados+180)*2)

def estrella(size):
	for i in range(1,(numeroLados+1)):
		t.forward(300)
		t.left(size)

t.reset()
estrella(angulo)
turtle._getscreen()._root.mainloop()



