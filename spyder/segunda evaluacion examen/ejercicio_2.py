#ejercicio 2

numero= 0
frase= input("escriba una frase: ")
palabra= input("escriba la palabra que quiere buscar: ")
lista= frase.split(" ")
print("Las palabras que ha puesto son: ", lista)
for x in lista:
    if x== palabra:
        numero= numero+1
print("La palabra", palabra, "aparece en la frase ", numero, "veces")


