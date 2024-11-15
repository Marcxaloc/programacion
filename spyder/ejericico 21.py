#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
a=int(input("introduce un numero"))
b=int(input("introduce otro numero"))
c=int(input("introduce otro numero"))
raiz=b**2-4*a*c
if raiz<0:
    print("La raíz no puede ser un valor negativo")
else:
    operacion1=(-b+math.sqrt(raiz))/(2*a)
    operacion2=(-b-math.sqrt(raiz))/(2*a)
    print("el valor 1 es: ",operacion1)
    print("el valor 2 es: ",operacion2)
