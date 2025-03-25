#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.
lista1=[]
lista2=[]
palabra=1
palabras=int(input("intrduce la cantidad de palabras: "))
for x in range (0,palabras):
    x=input("Introduce una palabra: ")
    palabra=palabra+1
    lista1.append(x)
    lista2.append(x)
lista1.sort()
lista2.sort()
lista2.reverse()
print("lista1 contiene",lista1)
print("lista2 contiene",lista2)