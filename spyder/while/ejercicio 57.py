#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random 
numero=0
var=random.randint(1,5)
while not var==numero:
    numero=int(input("adivina mi numero entre 1 y 5: "))
print("has adivinado, el numero era el",var)