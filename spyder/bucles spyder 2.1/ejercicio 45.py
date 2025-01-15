#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:
vocales=""
consonantes=""
palabra=input("introduce una palabra: ")
for recorrer in range (len(palabra)):
    if palabra[recorrer].isalpha():
       
        if palabra[recorrer]=="a" or palabra[recorrer]=="e" or palabra[recorrer]=="i" or palabra[recorrer]=="o" or palabra[recorrer]=="u":
            vocales=vocales+(palabra[recorrer])
        else:
            consonantes=consonantes+(palabra[recorrer])
print("Las vocales de la palabra",palabra,"son:",vocales)
print("Las consonantes de la palabra",palabra,"son:",consonantes)
