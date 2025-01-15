#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
vocales=""
consonantes=""
palabra=input("introduce una palabra: ")
palabra=palabra.lower()
for recorrer in range (len(palabra)):
    if palabra[recorrer].isalpha():
       
        if palabra[recorrer]=="a" or palabra[recorrer]=="e" or palabra[recorrer]=="i" or palabra[recorrer]=="o" or palabra[recorrer]=="u":
            vocales=vocales+(palabra[recorrer])
        else:
            consonantes=consonantes+(palabra[recorrer])
print("Las vocales de la palabra",palabra,"son:",vocales)
print("Las consonantes de la palabra",palabra,"son:",consonantes)