#2

var1 = 0
frase = input("Introduzca la frase: ")
palabra = input("Introduzca la palabra buscada: ")

lista = frase.split(" ")

print("Lista de palabras: ", lista)

for palabra_lista in lista:
    if palabra_lista == palabra:
        var1 += 1

print("La palabra", palabra, "aparece", var1, "veces")


