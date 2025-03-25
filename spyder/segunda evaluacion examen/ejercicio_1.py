#1

nueva_lista = []
lsiata1= []
lista = input("Introduzca 6 números separados por guiones: ")

lista1= list(map(int, lista.split("-")))

print("Números ingresados:", lista1)

lista1.sort()

print("Máximo:", max(lista1))
print("Mínimo:", min(lista1))

promedio = sum(lista1) / len(lista1)

print("Promedio:", promedio)

# for x in range (0,6):
    #numeros=input("introduce...)
    #lista.append(int(numeros))

