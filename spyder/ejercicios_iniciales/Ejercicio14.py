import math
diametro = int(input("Introduce diametro: "))
radio = int(diametro/2)
area= math.pi*radio**2
perimetro=2*math.pi*radio
print("el area del circulo es:",round(area,1))
print("el perimetro del circulo es:",round(perimetro,1))
