import turtle
import time
import math
t = turtle.Turtle()
s = 100.0
anguloTriangulo =120
anguloCuadrado =90

#CUADRADO
t.forward(s) 
t.left(anguloCuadrado) 
 
t.forward(s) 
t.left(anguloCuadrado) 
 
t.forward(s) 
t.left(anguloCuadrado) 
 
t.forward(s) 
t.left(anguloCuadrado) 

t.goto(0,s)
#TRIANGULO
 
t.forward(s) 
t.left(anguloTriangulo) 

t.forward(s) 
t.left(anguloTriangulo) 

t.forward(s) 
t.left(anguloTriangulo) 

#DIAGRONALES
diagonal = math.sqrt(2*(s*s))
#print(diagonal)
#t.goto(s,0)
t.right(anguloCuadrado/2) 
t.forward(diagonal) 

#t.goto(0,0)

t.left(anguloCuadrado/2) 
t.forward(-s) 

t.left(anguloCuadrado/2) 
t.forward(diagonal)


time.sleep(5)