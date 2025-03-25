#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra
import random
listapalabras=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
palabra= random.choice(listapalabras)
pregunta=input("Introduce la palabra secreta: ")
while palabra!=pregunta:
    print("SIGUE JUGANDO")
    pregunta=input("Introduce la palabra secreta: ")
else:
    print("ACERTASTE")