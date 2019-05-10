Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Pen()
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(90)
>>> t.left(90)
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(90)
>>> turtle.getscreen()._root.mainloop()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    turtle.getscreen()._root.mainloop()
  File "C:\Users\ESFOT\AppData\Local\Programs\Python\Python37\lib\tkinter\__init__.py", line 1280, in mainloop
    self.tk.mainloop(n)
KeyboardInterrupt

>>> t.reset()
>>> for x in range(1,9):
	t.forward(100)
	t.left(225)

	
>>> t.reset()
>>> for x in range(1,38):
	t.forward(100)
	t.left(175)

	
>>> t.reset()
>>> def micuadrado(size):
	for x in range(1,5):
		t.forward(size)
		t.left(90)

		
>>> micuadrado(90)
>>> def estrella(n):
	t=(90/n)+90
	for x in range(1,n):
		t.forward(100)
		t.left(t)

		
>>> estrella(5)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    estrella(5)
  File "<pyshell#31>", line 4, in estrella
    t.forward(100)
AttributeError: 'float' object has no attribute 'forward'
>>> t.reset()
>>> estrella(5)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    estrella(5)
  File "<pyshell#31>", line 4, in estrella
    t.forward(100)
AttributeError: 'float' object has no attribute 'forward'
>>> def estrella(n):
	ang=(90/n)+90
	for x in range(1,n):
		t.forward(100)
		t.left(ang)

		
>>> estrella(10)
>>> estrella(10)
>>> t.reset()
>>> estrella(10)
>>> def estrella(n):
	ang=(90/n)+90
	for x in range(1,n+2):
		t.forward(100)
		t.left(ang)

		
>>> estrella(10)
>>>  def estrella(n):
	ang=(-360/n)+180
	for x in range(n):
		t.forward(100)
		t.left(ang)
		
SyntaxError: unexpected indent
>>> def estrella(n):
	ang=(-360/n)+180
	for x in range(n):
		t.forward(100)
		t.left(ang)

		
>>> t.reset()
>>> estrella(10)
>>> def estrella(n):
	ang=(90/n)+90
	for x in range(n):
		t.forward(100)
		t.left(ang)

		
>>> t.reset()
>>> estrella(10)
>>> def estrella(n):
	ang=(90/n)+90
	for x in range(n+1):
		t.forward(100)
		t.left(ang)

		
>>> t.reset()
>>> estrella(10)
>>> t.reset()
>>> estrella(20)
>>> t.reset()
>>> estrella(4)
>>> def estrella(tam,n):
	for x in range(n):
		t.forward(tam)
		t.left(ang)
tamaño = int(input("Ingrese el tamño para la estrella"))
SyntaxError: invalid syntax
>>> def estrella(tam,n):
	for x in range(n):
		t.forward(tam)
		t.left(ang)
tam= int(input("Ingrese el tamño para la estrella"))
SyntaxError: invalid syntax
>>> 
