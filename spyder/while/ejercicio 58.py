# 58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random 
cont=0
numero=0
var=random.randint(1,5)
while cont<3:
    cont=cont+1
    numero=int(input("adivina mi numero entre 1 y 5: "))
    if numero==var:
        print("has adivinado, el numero era el",var)
        break
else:
    print("mala suerte,no lo has adibinado")