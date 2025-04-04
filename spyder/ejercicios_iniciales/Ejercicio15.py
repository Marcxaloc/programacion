import math
radio = int(input("Introduce radio: "))
altura = int(input("Introduce altura: "))
areacirculo= math.pi*radio**2
perimetrocirculo=math.pi*radio*2
base=perimetrocirculo
arearectangulo= altura*base
areatotal=areacirculo*2+arearectangulo
volumen= areacirculo*altura
print("el area del cilindro es:",round(areatotal,2))
print("el volumen del cilindro es:",round(volumen,2))
