#41. Imprime el siguiente patrón utilizando for:
numero="54321"
longitud=len(numero)
longitud=range(longitud)
for contador in longitud:
    print(numero)
    numero=numero[1:len(numero)]