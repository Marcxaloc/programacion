#ejercicio 1

lista2= []
lista= input("Introduzca 6 números separados por guiones: ")
lista2= list(map(int, lista.split("-")))
print("los numeros que has puesto son:", lista2)
lista2.sort()
maximo=max(lista2)
minimo=min(lista2)
print("el numero maximo es:", maximo)
print("el numero minimo es:", minimo)
longuitud=len(lista2)
suma=sum(lista2)
promedio=suma/longuitud
print("el promedio de los numeros es: ", promedio)